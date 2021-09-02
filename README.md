# flask_sqlalchemy  
### 創建以及初始化  

----  
```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(configname) #載入設定檔案，須有一個configname.py檔案
app.config.from_pyfile(configname) #載入設定檔案，須有一個configname.py檔案
db.init(app)  初始化app
```
- config.py(以下連線至postgresql為例子)  
```
DB_TYPE = "postgresql"
DRIVER = "psycopg2"
USERNAME = "postgres"
PASSWORD = "test"
HOST = "127.0.0.1"
PORT = "5432"
DATABASE = "BPS"
app.config['SQLALCHEMY_DATABASE_URI'] = [DB_TYPE]+[DRIVER]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DATABASE]

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
```
----  
### CORS
- 跨域設置  
```
from flask_cors import *
CORS(app, support_credentials=True)
```
----  
### Sequenct
```
from sqlalchemy import Sequence
ex. 
id = db.column(format, Sequenct(tablename), nullable = False, primary_key=True)  #讓db自動默認排列
datetime = db.column(db.datetime, Sequenct(tablename), default=datetime.now(), nullable = False)  
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
# sqlalchemy
### 創建及初始化

----  
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
