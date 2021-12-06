<div align="center" ><img src="https://flask-sqlalchemy.palletsprojects.com/en/2.x/_images/flask-sqlalchemy-title.png" width=1500></div>  

----------  

>> Flask_sqlalchemy遵循MVC原則  
>> 主要含有三大元素 Model、Controller、View  
>> Model主要負責創建模型，對應Database中的欄位  
>> View主要負責作呈現，可使用Marshmallow做序列化呈現  
>> Controller主要負責創建供使用者視覺化操作之部分  


### 創建以及初始化  
## flask_sqlalchemy  
```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(configname) #載入設定檔案，須有一個configname.py檔案
app.config.from_pyfile(configname) #載入設定檔案，須有一個configname.py檔案
db.init(app)  初始化app
```
- configname.py(以下連線至postgresql為例子)  
```
DIALCT = "postgresql"
DRIVER = "psycopg2"
USERNAME = "postgres"
PASSWORD = "test"
HOST = "127.0.0.1"
PORT = "5432"
DATABASE = "test"
DB_URI = f"{DIALCT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
SQLALCHEMY_DATABASE_URI = DB_URI
print(SQLALCHEMY_DATABASE_URI)
JSON_AS_ASCII = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
```
- config.py(以下連線至mysql為例子)  
```
DB_TYPE = "mysql"
DRIVER = "pymysql"
USERNAME = "root"
PASSWORD = "test"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = [DB_TYPE]+[DRIVER]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DATABASE]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```
---- 
### app.config 參數介紹 (3.0後不適用)
- SQLALCHEMY_DATABASE_URL(連線設定)
```
app.config['SQLALCHEMY_DATABASE_URI'] = [DB_TYPE]+[DRIVER]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DATABASE]
```
- SQLALCHEMY_ENGINE_OPTIONS(引擎設置)
```
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
    "pool_recycle": 300, 連接回收時間
    'pool_timeout': 900, 連線等待時間
    'pool_size': 10,   最大連線數
    'max_overflow': 5, 連線滿後加開多少
}
```
- SQLALCHEMY_ECHO(debug設置)
```
app.config['SQLALCHEMY_ECHO'] = True
```
---- 
## sqlalchemy
```
from sqlalchemy import create_engine

DB_TYPE = "postgresql"
DRIVER = "psycopg2"
USERNAME = "postgres"
PASSWORD = "test"
HOST = "127.0.0.1"
PORT = "5432"
DATABASE = "BPS"
engine = create_engine([DB_TYPE]+[DRIVER]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DATABASE],
                        max_overflow=0,  # 超過連線池大小外最多建立的連線
                        pool_size=5,  # 連線池大小
                        pool_timeout=30,  # 池中沒有執行緒最多等待的時間，否則報錯
                        pool_recycle=-1  # 多久之後對執行緒池中的執行緒進行一次連線的回收（重置）
                        )
conn = engine.connect()  #類似SQL連線
```
### 操作Database
----
- 前置條件
```
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:test@127.0.0.1:5432/test'
db = SQLAlchemy()
db.init(app)
```
- 新建資料
```
db.engine.execute(f'INSERT INTO {table} VALUES (test)')
```
- 搜尋資料
```
db.engine.execute(f'SELECT * from {table}')
```

----  
### CORS
- 跨域設置  
```
from flask_cors import *
CORS(app, support_credentials=True)
```
----  
### Sequence
Example:
```
from sqlalchemy import Sequence
id = db.column(format, Sequence(tablename), nullable = False, primary_key=True)  #讓db自動默認排列
datetime = db.column(db.datetime, Sequence(tablename), default=datetime.now(), nullable = False)  
```
- format  
db.Integer    數字  
db.String(50) 文字  
db.Datetime   日期格式  
eq...  

----  
### session_options
```
from flask_sqlalchemy import SQLAlchemy  
db = SQLAlchemy(session_options={'autoflush' : False}) #關閉自動刷新session
```
----  
### SQL連接使用
```
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


db.session.add(self)    #新增
db.session.merge(self)   #修改
db.session.delete(self)  #刪除
db.session.commit()      #確認修改
db.rollback()            #回歸原始點(一般在except後)
```
---- 
### 多個DB連接  
```
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

ENGINE: Engine = create_engine(BP_URI, echo=False, convert_unicode=True, pool_recycle=3600, pool_size=20, pool_timeout=60)
Session = sessionmaker()
Session.configure(bind=ENGINE)
sess = Session()
sess.query.all()
```
---- 
### 新建Table
```
db.create_all()
```
- 若出現no application found  
```
with app.app_context():
    db.create_all()
```
---- 

## Model 
### Create
```
db = SQLAlchemy()

class Objtestuse(db.Model):
    __tablename__ = 'test'
    
    id = db.Column(db.Integer, Sequence('TBL_INCOMING_INFO_id_seq'), primary_key=True, nullable=False)
    text = db.Column(db.String(50), db.ForeignKey('TBL_MATERIAL_BUY_CODE.buy_code'), nullable=True)
    is_bool = db.Column(db.Boolean, nullable=True)
    datetime = db.Column(db.DateTime, nullable=True, default = datetime.now)
```
### Use
#### Serach
1. common
```
ft = [Objtestuse.id == 3]
# method1
result = db.session.query(Objtestuse.id).filter(*ft).all()
# method2
result = Objtestuse.query.filter(*ft).all()
```
2. outerjoin
```
ft = [Objtestuse.id == 1]
result = Objtestuse.query.outerjoin(Objtes1tuse, Objtes2tuse)\
            .filter(*ft).order_by(Objtestuse.id) \
            .paginate(page, per_page=size, error_out=False)
text = ObjtestuseSchema.dump(result.items, many=True)
```
3. Search(不分大小寫)
```
result = Objtestuse.query.filter(Objtestuse.name.ilike('test').all()
data = ObjtestuseSchema.dump(result, many=True)
```
#### Add
```
Objtestuse.name = name
db.session.add(Objtestuse)
db.session.commit()

Obj_id = objtestuse.id   # 若新增後   該值的ID
```
#### Updata
```
db.session.query.filter(Objtestuse.id == 3).update({'name':name})
db.session.commit()
```
#### delete
```
db.session.query.filter(Objtestuse.id == 3).delete()
db.session.commit()
```
### Show出model所有column 
```
model = MYMODEL
columns = [m.key for m in model.__table__.columns]
```
