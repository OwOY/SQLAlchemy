from model.database import db
from model.UserInfo import ObjUserInfo
from model.UserGroupInfo import ObjUserGroupInfo


class SrvUserInfo:
    def create(self):
        obj = ObjUserInfo()
        obj.name = 'david'
        obj.create()
    
    def serach(self):
        # data_list = ObjUserInfo.query.filter(ObjUserInfo.name=='david').all()
        data_list = ObjUserInfo.query.filter_by(name='david').all()
        # data_list = ObjUserInfo.query.filter_by(name='david').order_by(ObjUserInfo.id.desc()).all()
        # data_list = ObjUserInfo.query.filter(ObjUserGroupInfo.id==3)\
                                        # .join(ObjUserGroupInfo, ObjUserInfo.name==ObjUserGroupInfo.name)\
                                        # .all()
        for data in data_list:
            name = data.name
        
    def update(self):
        obj = ObjUserInfo.query.filter_by(name='david')
        obj.name = 'David'
        obj.update()
        
    def update1(self):
        ObjUserInfo.query.filter_by(name='david').update({'name':'David'})
        db.session.commit()
        
    def delete(self):
        # ObjUserInfo.query.delete() # truncate
        ObjUserInfo.query.filter_by(name='david').delete()
        db.session.commit()
    
