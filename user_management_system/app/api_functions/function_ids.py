from instance import app,mongo
import json
from bson.json_util import dumps
from bson import json_util

def create_function(params):
    try:
        param = json.loads(params)
        function_details = mongo.db.functions
        function_name = param["function_name"]
        function_des = param["function_des"]
        function_location = param["function_location"]
        created_by = param["created_by"]
        created_by_name = param["created_by_name"]
        check_function = function_details.find({"function_name":function_name}).count()
        if check_function == 0:
            function = function_details.insert_one({"function_name" : function_name,"function_des" :function_des,"function_location": function_location,"created_by" : created_by,"created_by_name" : created_by_name})
            function_data = function_details.find({"function_name": function_name})
            function_data = [json.loads(json.dumps(item, default=json_util.default)) for item in function_data]
            function_data[0]["message"] = "Function was Successfully Created!!!"
            res = function_data
            status = 201
        else:
            status = 409
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res, status


def create_chanels(params):
    try:
        param = json.loads(params)
        chanel_details = mongo.db.chanels
        chanel_name = param["chanel_name"]
        chanel_code = chanel_name[:4].upper()
        chanel_des = param["chanel_des"]
        authorize_models = param["authorize_models"]
        authorize_groups = [param.get("authorize_groups")]
        chanel_status = param["chanel_status"]
        created_by = param["created_by"]
        created_by_name = param["created_by_name"]
        check_chanel = chanel_details.find({"chanel_name": chanel_name}).count()
        if check_chanel == 0:
            chanel = {"chanel_code":chanel_code,"chanel_name":chanel_name,"chanel_des":chanel_des,"authorize_models":authorize_models,"chanel_status":chanel_status,"created_by":created_by,"created_by_name":created_by_name,"authorize_groups":authorize_groups}
            chanel = chanel_details.insert_one(chanel)
            chanel_data = chanel_details.find({"chanel_name": chanel_name})
            chanel_data = [json.loads(json.dumps(item, default=json_util.default)) for item in chanel_data]
            chanel_data[0]["message"] = "Chanel was Successfully Created!!!"
            res = chanel_data
            status = 201
        else:
            res = "Chanel Was already exists!!!"
            status = 409
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res, status

def update_chanel(params):
    try:
        param = json.loads(params)
        chanel_details = mongo.db.chanels
        chanel_code = param["chanel_code"]
        authorize_groups = [param.get("authorize_groups")]
        check_chanel = chanel_details.find({"chanel_code": chanel_code}).count()
        if check_chanel != 0:
            myquery = {"chanel_code":chanel_code}
            newvalues = { "$set":{"chanel_name":param["chanel_name"],"chanel_code":param["chanel_name"][:4].upper(),"authorize_groups":authorize_groups}}
            x= chanel_details.update_one( myquery, newvalues)
            if x.modified_count > 0:
                chanel_data = chanel_details.find({"chanel_name": param["chanel_name"]})
                chanel_data = [json.loads(json.dumps(item, default=json_util.default)) for item in chanel_data]
                chanel_data[0]["message"] = "Chanel Details Was Successfully Updated!!!"
                res = chanel_data
                status = 200
            else:
                res = "Chanel Details didn't Updated!!!"
                status = 407

        else:
            res = "Chanel Details Not Found!!!"
            status = 404
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res, status


def delete_chanel(params):
    try:
        param = json.loads(params)
        chanel_details = mongo.db.chanels
        print (param)

        chanel_code = param["chanel_code"]
        check_chanel = chanel_details.find({"chanel_code": chanel_code}).count()
        if check_chanel != 0:
            chanel_detail = chanel_details.find_one({"chanel_code":chanel_code})
            if chanel_detail["authorize_groups"] == [None] and chanel_detail["authorize_groups"]==[""]:
                chanel_details.delete_one({"chanel_code": chanel_code})
                res = "successfully deleted"
                status = 200
            else:
                res = "please delete first authorize groups"
                status = 404
        else:
            res = "Chanel Details Not Found!!!"
            status = 404

    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res, status








