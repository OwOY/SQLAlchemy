from model.database import db
from datetime import datetime


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

    def __repr__(self):
        return '<TBL_USER_INFO %r>' % self.id

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            
    def update(self):
        try:
            db.session.merge(self)
            db.session.commit()
        except:
            db.session.rollback()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
