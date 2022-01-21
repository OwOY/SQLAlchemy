from marshmallow import fields, Schema

# 序列化輸出
class ObjUserSchema(Schema):

    __tablename__ = 'TBL_USER_INFO'

    # id
    id = fields.Integer()
    # 人員ID
    user_id = fields.String()
    # 姓名
    name = fields.String()
    # 部門
    department = fields.String()
    # 主管
    manager = fields.String()
    # 建立使用者ID
    create_user_id = fields.String()
    # 建立時間
    create_time = fields.DateTime()
    # 更新使用者ID
    update_user_id = fields.String()
    # 更新時間
    update_time = fields.DateTime()
