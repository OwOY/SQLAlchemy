from marshmallow import fields, Schema

# 序列化輸出
class ObjUserSchema(Schema):

    __tablename__ = 'TBL_USER_INFO'

    # id
    id = fields.Int()
    # 人員ID
    user_id = fields.Str()
    # 姓名
    name = fields.Str()
    # 部門
    department = fields.Str()
    # 主管
    manager = fields.Str()
    # 建立使用者ID
    create_user_id = fields.Str()
    # 建立時間
    create_time = fields.DateTime()
    # 更新使用者ID
    update_user_id = fields.Str()
    # 更新時間
    update_time = fields.DateTime()
