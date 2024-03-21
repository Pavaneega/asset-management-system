import json
from instance import db,mongo
from app.models.Groups import Groups,Group_users
from app.models.Users import User
from app.utils import current_time,password_hash,current_time
from app.api_functions import authorize_user
from bson import ObjectId
timestamp = current_time.get_current_epoc_time()


def create_group(data):
    try:
        data = json.loads(data)
        check_group = Groups.query.filter_by(group_name=data["group_name"]).first()
        if check_group is None:
            function_details = mongo.db.functions
            function_details = function_details.find_one({"function_location":data["function_location"]})
            function_id = str(function_details.get('_id'))
            create_group = Groups(group_name = data['group_name'],created_by=data['created_by'],function_id = function_id,
                                      created_at=timestamp,last_updated_at=timestamp,group_type=data['group_type']
                                      )
            db.session.add(create_group)
            db.session.commit()
            group_data = Groups.query.filter_by(group_name=data["group_name"]).first()
            group_data_serialized = group_data.serialize()
            print(group_data_serialized)
            group_data_serialized["message"] = "Create group successfully!!"
            res = group_data_serialized
            status = 201
        else:
            res = "Group already exists!!"
            status = 409
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res,status


#add user to group
def create_group_user(data):
    try:
        data = json.loads(data)
        check_group = Groups.query.filter_by(group_name=data["group_name"]).first()
        if check_group is not None:
            check_user = User.query.filter_by(user_id=data["user_id"]).first()
            if check_user is not None:
                check_group_user = Group_users.query.filter_by(group_name=data["group_name"],user_id = str(data["user_id"])).first()
                if check_group_user is None:
                    create_group_user = Group_users(group_name = data["group_name"] , user_id = data["user_id"],add_by = data["add_by"],add_at = timestamp)
                    db.session.add(create_group_user)
                    db.session.commit()
                    check_group_user = Group_users.query.filter_by(group_name=data["group_name"],
                                                                   user_id=str(data["user_id"])).first()
                    group_user_data = check_group_user.serialize()
                    group_user_data["message"] = "Added user to group sucessfully!!!"
                    res = group_user_data
                    status = 201
                else:
                    res = "Group User already Exists!!"
                    status = 409
            else:
                res = "User Not Found!!!"
                status = 404
        else:
            res = "Group already Exists!!"
            status = 409
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res,status


def get_all_groups():
    try:
        all_group_data = Groups.query.filter_by().all()
        group_list = [group.serialize() for group in all_group_data]
        res = group_list
        status = 200
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res,status

def update_group_name(data):
    try:
        data = json.loads(data)
        check_group = Groups.query.filter_by(group_name=data["old_group_name"]).first()
        if check_group is not None:
            check_group.group_name = data["group_name"]
            db.session.commit()
            group_data = Groups.query.filter_by(group_name=data["old_group_name"]).first()
            group_data = group_data.serialize()
            group_data["message"] = "Group Name Successfully Updated"
            res = group_data
            status = 200
        else:
            res = "Group not found"
            status = 404
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res,status



def delete_group(data):
    try:
        data = json.loads(data)
        check_group = Groups.query.filter_by(group_name=data["group_name"]).first()
        print(check_group)
        if check_group is not None:
            delete_group = Groups.query.filter_by(group_name=data["group_name"]).delete()
            db.session.commit()
            print("delete_group",delete_group)
            res = "Delete Group Successfully!!!"
            status = 200
            return res, status
        else:
            res = "Group not found"
            status = 404
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res,status

def delete_user_from_group(data):
    try:
        data = json.loads(data)
        check_group = Group_users.query.filter_by(group_name=data["group_name"],user_id=data["user_id"]).first()
        print(check_group)
        if check_group is not None:
            delete_group = Group_users.query.filter_by(group_name=data["group_name"],user_id=data["user_id"]).delete()
            db.session.commit()
            check_group = Group_users.query.filter_by(group_name=data["group_name"],user_id=data["user_id"]).first()
            if check_group == None:
                res = "Delete Group User Successfully!!!"
                status = 200
        else:
            res = "Group User Not Found!!!"
            status = 404
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res,status



def get_users_from__specific_group(data):
    try:
        data = json.loads(data)
        check_group = Group_users.query.filter_by(group_name=data["group_name"]).first()
        if check_group is not None:
            a = Group_users.query.filter_by(group_name=data["group_name"]).all()
            group_list = [group.serialize() for group in a]
            res = group_list
            status = 200
        else:
            res = "Group Not Found!!"
            status = 404
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res,status











