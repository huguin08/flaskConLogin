from .entities.User import User
from werkzeug.security import check_password_hash

class ModelUser():

    @classmethod
    def login(self,db,user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM user
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row is not None:
                user_id, username, hashed_password, fullname = row
                if check_password_hash(hashed_password, user.password):
                    return User(user_id, username, hashed_password, fullname)
            return None
        except Exception as ex:
            raise Exception(ex)