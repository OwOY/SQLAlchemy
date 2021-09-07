from model.database import db
from datetime import datetime
from DBSchema.UserSchema import ObjUserSchema


UserSchema = ObjUserSchema()
class md(db.Model):

    __tablename__ = 'TBL_USER_INFO'

    # id
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # 人員ID
    user_id = db.Column(db.String(50), nullable=False)
    # 姓名
    name = db.Column(db.String(50), nullable=False)
    # 部門
    department = db.Column(db.String(20), nullable=False)
    # 主管
    manager = db.Column(db.String(50), nullable=True)
    # 建立使用者ID
    create_user_id = db.Column(db.String(50), nullable=False)
    # 建立時間
    create_time = db.Column(db.DateTime, default=datetime.now())
    # 更新使用者ID
    update_user_id = db.Column(db.String(50), nullable=False)
    # 更新時間
    update_time = db.Column(db.DateTime, default=datetime.now())

    # groups = db.relationship('ObjUserGroupMapping', backref='TBL_USER_INFO')

    def __repr__(self):
        return '<TBL_USER_INFO %r>' % self.id

    def create(self, data):
        db.session.add(data)
        return db.session.commit()
    
    def search(self, data):
        # input_id = data.get('id', None)
        data = db.engine.execute('SELECT * from "TBL_USER_INFO";')
        for d in data:
            json_data = UserSchema.dump(d)

        # output = md.query.filter(md.id == input_id).all()
        # out = ObjUserInfoSchema().dump(output)
        return {'data':json_data}