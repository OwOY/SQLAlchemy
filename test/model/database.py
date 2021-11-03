from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True

    def create(self):
        try:
            request_data = {
                "msg": None,
                "error_msg": None,
                "data": None,
            }

            db.session.add(self)
            db.session.commit()
        except Exception as e:
            request_data['msg'] = FAILURE
            request_data['error_msg'] = e
            db.session.rollback()
            return request_data
        else:
            request_data['data'] = self
            request_data['msg'] = SUCCESS
            return request_data

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            # print(e)
            db.session.rollback()
            return FAILURE
        else:
            return SUCCESS

    def update(self):
        try:
            db.session.merge(self)
            db.session.commit()
        except Exception as e:
            # print(e)
            db.session.rollback()
            return FAILURE
        else:
            return SUCCESS

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            # print(e)
            db.session.rollback()
            return FAILURE
        else:
            return SUCCESS

    def deleteById(self, id):
        try:
            od = self.query.get(id)
            if od != None:
                db.session.delete(od)
                db.session.commit()
        except Exception as e:
            # print(e)
            db.session.rollback()
            return FAILURE
        else:
            return SUCCESS

    @staticmethod
    def create_all(model_list):
        try:
            request_data = {
                "msg": None,
                "error_msg": None,
                "data": None,
            }

            db.session.add_all(model_list)
            db.session.commit()
        except Exception as e:
            request_data['msg'] = FAILURE
            request_data['error_msg'] = e
            db.session.rollback()
            return request_data
        else:
            request_data['data'] = model_list
            request_data['msg'] = SUCCESS
            return request_data

    @staticmethod
    def save_all(model_list):
        try:
            db.session.add_all(model_list)
            db.session.commit()
        except Exception as e:
            # print(e)
            db.session.rollback()
            return FAILURE
        else:
            return SUCCESS

    @staticmethod
    def delete_all(model_list):
        try:
            for model in model_list:
                db.session.delete(model)
            db.session.commit()
        except Exception as e:
            # print(e)
            db.session.rollback()
            return FAILURE
        else:
            return SUCCESS
