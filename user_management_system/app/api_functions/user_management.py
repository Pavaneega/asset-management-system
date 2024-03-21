import json
from instance import db
from app.models.Users import User
from app.utils import current_time,password_hash
from app.api_functions import authorize_user

def create_db_tables():
    db.create_all()
    return "successfully created",200

def create_admin_user(params):
    try:
        params = json.loads(params)
        created_by = params["user_id"]
        # password = password_hash.create_hash_password()
        password = password=params["password"]
        confirm_password = password=params["confirm_password"]
        if created_by == 1:
            if password == confirm_password:
                check_login = User.query.filter_by(login_id=params['login_id']).first()
                print(check_login)
                check_personnel_id = User.query.filter_by(personnel_id=params['personnel_id']).first()
                print(check_personnel_id)
                if check_login is None:
                    if check_personnel_id is None:
                        user = User(login_id=params["login_id"],u_name=params["u_name"],password=params["password"],location=params["location"],
                                     department=params["department"],country=params["country"],description=params["description"],image_url=params["image_url"],
                                     personnel_id=params["personnel_id"],role_type=params["role_type"],external_status=params["external_status"],created_on=current_time.get_current_epoc_time(),
                                     created_by=created_by,email=params["email"])

                        db.session.add(user)
                        db.session.commit()
                        check_login = User.query.filter_by(login_id=params['login_id']).first()
                        user_data_serialized = check_login.serialize()
                        user_data_serialized["message"] = "password successfully updated!!!"
                        result = user_data_serialized
                        status = 201
                    else:
                        result = "This Personnel Id Already Exit, please try to another Personal id !!!"
                        status = 409
                else:
                    result = "This Login Id Already Exit, please try to another login id !!!"
                    status = 409
            else:
                result = "passwords didn't matched"
                status = 404
        else:
            result = "Unauthorized admin for creating user"
            status = 404

    except:
        result = "internal server error please try again"
        status = 500
    finally:
        return result, status


def get_admin_user_details(user_id):
    try:
        user_object = User.query.filter_by(user_id=user_id).first()
        if user_object != None:
            user_data_serialized = user_object.serialize()
            result = user_data_serialized
            status = 200
        else:
            result = {}
            status = 200
    except:
        result = "internal server error please try again"
        status = 500
    finally:
        return result,status


def user_authentication(params):
    try:
        # param = dict(params)
        param = json.loads(params)
        print(param["password"])
        print(param['login_id'], param['password'])
        check_login = User.query.filter_by(login_id=param['login_id'], password=param['password']).first()
        res = {}
        if check_login is not None:
            app_previlage = User.query.filter_by(user_id=check_login.user_id).all()
            app_previlage = [row.serialize() for row in app_previlage]
            prev = {}
            for previlage_list in app_previlage:
                #prev[previlage_list["app_name"]] = previlage_list["status"]
                res['application_previlege'] = prev
                res["user_id"] = check_login.user_id
                res["u_name"] = check_login.u_name
                res["login_id"] = check_login.login_id
                res["country"] = check_login.country
                res["department"] = check_login.department
                res["description"] = check_login.description
                res["location"] = check_login.location
                res['token'] = authorize_user.generate_access_token(check_login.user_id)
                res['image_url'] = check_login.image_url
                res['message'] = "login successful"
                res = res
                status = 200

        else:
            res['message'] = "Authentication failure"
            return res, 404
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res, status


def user_password_reset(params):
    try:
        param = json.loads(params)
        if param["user_id"] != 1:
            if param["retype_pass"] == param["confirm_pass"]:
                check_password = User.query.filter_by(user_id=param['user_id'],password=param["cur_pass"]).first()
                check_user = User.query.filter_by(user_id=param['user_id']).first()
                if check_user is not None:
                    if check_password is not None:
                        check_password.password = param["confirm_pass"]
                        db.session.commit()
                        user_data_serialized = check_user.serialize()
                        user_data_serialized["message"] = "password successfully updated!!!"

                        result = user_data_serialized
                        status =200
                    else:
                        result = "Password Was Wrong!!!"
                        status = 404
                else:
                    result = "User Not Found!!!"
                    status = 404
            else:
                result = "New Passwords Didn't Match!!!"
                status = 404
        else:
            result = "Unauthorized admin for reseting user"
            status = 404
    except:
        result = "internal server error please try again"
        status = 500
    finally:
        return result,status


def update_user_email(params,user_id):
    try:
        param = json.loads(params)
        if user_id is not None:
            check_login = User.query.filter_by(user_id=user_id).first()
            if check_login is not None:
                    check_login.email = param["email"]
                    db.session.commit()
                    user_data_serialized = check_login.serialize()
                    user_data_serialized["message"] = "password successfully updated!!!"
                    result = user_data_serialized
                    status =200
                    return result, status
            else:
                result = "User Not Found"
                status = 404
        else:
            result = "user_id not found"
            status = 404
    except:
        result = "internal server error please try again"
        status = 500
    finally:
        return result,status













