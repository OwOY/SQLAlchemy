# Marshmallow(序列化輸出)

### Example:
```
from marshmallow import fields, Schema

# 序列化輸出，根據database的格式做輸出
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


UserSchema = ObjUserSchema()
dic_data = UserSchema.dump(data)  #dict
json_data = UserSchema.dumps(data)  #dict
```

### 輸出格式

|較常用fields值|解釋|  
|----|-----|  
|Bool | alias of marshmallow.fields.Boolean|
|Date(format, **kwargs) | ISO8601-formatted date string.|
|DateTime(format, **kwargs) | A formatted datetime string.|
|Dict(keys, type]] = None, values, …) | A dict field.|
|Email(*args, **kwargs) | An email field.|
|Field(*, load_default, missing, …) | Basic field from which other fields should extend.|
|Int | alias of marshmallow.fields.Integer|
|List(cls_or_instance, type], **kwargs) | A list field, composed with another Field class or instance.|
|Str | alias of marshmallow.fields.String|
|Time(format, **kwargs) | A formatted time string.|
|TimeDelta(precision, **kwargs) | A field that (de)serializes a datetime.timedelta object to an integer and vice versa.|
|Tuple(tuple_fields, *args, **kwargs) | A tuple field, composed of a fixed number of other Field classes or instances|
|URL | alias of marshmallow.fields.Url|
|Url(*, relative, schemes, Set[str]]] = None, …) | An URL field.|
- 更多格式  
https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html
