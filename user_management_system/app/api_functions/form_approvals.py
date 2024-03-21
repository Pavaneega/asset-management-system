from instance import app,mongo
from instance.dbconfig import base_url
import json
from app.models.Groups import Groups,Group_users
from bson.json_util import dumps
from bson import json_util
from app.utils import current_time,password_hash,current_time
timestamp = current_time.get_current_epoc_time()
import re
import request
import requests

def check_form_active_or_inactive(fn):
    def _wrap(form_id,data):
        form_details = mongo.db.forms
        form_detail = form_details.find({"form_id": form_id})
        form_detail = json.loads(json_util.dumps(form_detail, default=json_util.default))
        if form_detail !=[]:
            form_isactive = form_detail[0]["isactive"]
            if form_isactive == 1:
                return fn(form_id,data)
            else:
                return "Please,Make inactive before adding Group or Chanel to the form and then modify!!!",401
        else:
            return "please provide correct form_id",404
    _wrap.func_name = fn.func_name
    return _wrap

def form_permission(form_id,permission_id):
    try:
        forms_details = mongo.db.forms
        check_form = forms_details.find({"form_id": form_id}).count()
        if check_form != 0:
            myquery = {"form_id": form_id}
            newvalues = {"$set": {"isactive": permission_id}}
            x = forms_details.update_one(myquery, newvalues)
            print (x.modified_count)
            if x.modified_count > 0:
                if permission_id == 1:
                    res = "Form Permission Was ON!!!"
                    status = 200
                else:
                    res = "Form Permission was OFF!!!"
                    status = 200

            else:
                res = "Authorize permission didn't updated!!!"
                status = 200
        else:
            res = "Form Was Not Found!!!"
            status = 404
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res, status

@check_form_active_or_inactive
def add_group_to_form(form_id,data):
    try:
        formapp_table=mongo.db.forms
        data = json.loads(data)
        group_id = data["group_id"]
        check=formapp_table.find({'$and':[{'form_id':form_id},{'authorized_groups':{'$elemMatch':{'$eq':data}}}]})
        for i in check:
            print(i)
        check=formapp_table.find({'$and':[{'form_id':form_id},{'authorized_groups':{'$elemMatch':{'$eq':{"group_id":group_id}}}}]}).count()
        if check ==0:
            formapp_table.update({'form_id':form_id},{'$addToSet':{'authorized_groups':data}} ) #another field add and save
            data="Successfully Assigned the Group"
            status=200
            return data, status
        else:
            status=409
            data="The Group you are trying to add already exists! Please add another Group!"
            return data, status
    except Exception as ex:
        status=500
        data="An unexpected error occurred in our Servers. Please try again"
    finally:
        return data,status
@check_form_active_or_inactive
def delete_group_to_form(form_id,data):
    try:
        formapp_table=mongo.db.forms
        data=json.loads(data)
        groupid = data['group_id']
        update = formapp_table.update({'form_id':form_id},{'$pull':{'authorized_groups': data}})
        data="operation Successful- Successfully deleted the Group!"
        #return data, 200
        status=200
    except Exception as ex:
        print ex
        status=500
        data="An unexpected error occurred in our Servers. Please try again"
    finally:
        return data,status


def get_groups_forms(form_id):
    try:
        formapp_table=mongo.db.forms
        print form_id
        mapped_groups=formapp_table.find({'form_id':form_id},{'authorized_groups':1})
        print mapped_groups
        data=[json.loads(json.dumps(item,default=json_util.default)) for item in mapped_groups]
        status=200
        #return data,200
    except Exception as ex:
        print ex
        status=500
        data="An unexpected error occurred in our Servers. Please try again"
    finally:
        return data,status

@check_form_active_or_inactive
def add_chanel_to_form(form_id,data):
    try:
        print(form_id)
        formapp_table=mongo.db.forms
        data = json.loads(data)
        chanel_code = data["chanel_code"]
        #check=formapp_table.find({'$and':[{'form_id':form_id},{'authorized_chanels':{'$elemMatch':{'$eq':data}}}]})
        check=formapp_table.find({'$and':[{'form_id':form_id},{'authorized_chanels':{'$elemMatch':{'$eq':{"chanel_code":chanel_code}}}}]}).count()
        if check ==0:
            formapp_table.update({'form_id':form_id},{'$addToSet':{'authorized_chanels':data}} ) #another field add and save
            data="Successfully Assigned the Chanel"
            status=200
            return data, status
        else:
            status=409
            data="The Chanel you are trying to add already exists! Please add another Chanel!"
            return data, status
    except Exception as ex:
        status=500
        data="An unexpected error occurred in our Servers. Please try again"
    finally:
        return data,status

@check_form_active_or_inactive
def delete_chanel_from_form(form_id,data):
    try:
        formapp_table=mongo.db.forms
        data=json.loads(data)
        chanel_code = data['chanel_code']
        formapp_table.update({'form_id':form_id},{'$pull':{'authorized_chanels': data}})
        data="operation Successful- Successfully deleted the Chanel!"
        #return data, 200
        status=200
    except Exception as ex:
        print ex
        status=500
        data="An unexpected error occurred in our Servers. Please try again"
    finally:
        return data,status


def get_chanel_forms(form_id):
    try:
        formapp_table=mongo.db.forms
        print form_id
        mapped_chanels=formapp_table.find({'form_id':form_id},{'authorized_chanels':1})
        print mapped_chanels
        data=[json.loads(json.dumps(item,default=json_util.default)) for item in mapped_chanels]
        status=200
        #return data,200
    except Exception as ex:
        print ex
        status=500
        data="An unexpected error occurred in our Servers. Please try again"
    finally:
        return data,status







