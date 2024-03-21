from instance import app,mongo
import json
from app.models.Groups import Groups,Group_users
from bson.json_util import dumps
from bson import json_util
from app.utils import current_time,password_hash,current_time
timestamp = current_time.get_current_epoc_time()
import re
def auto_incre_form_id():
    forms_details = mongo.db.forms
    form_id_count = forms_details.find({}).count()
    if form_id_count == 0:
        form_id = 1
        return form_id
    else:
        form_details = forms_details.find({}).sort("form_id",-1).limit(1)
        form_id = [json.loads(json.dumps(item, default=json_util.default)) for item in form_details]
        print(form_id)
        form_id = form_id[0]["form_id"] + 1
        return form_id


def alpha(str):
    only_alpha = ''
    for i in str:
        if i.isalpha():
            only_alpha += i
    return only_alpha

def check_special_char(word):
    special_char = True
    regexp = re.compile('[^0-9a-zA-Z]+')
    if regexp.search(word):
        special_char = False
    return special_char


def create_forms(params):
    try:
        param = json.loads(params)
        forms_details = mongo.db.forms
        form_name = param["form_name"]
        form_type = param["form_type"]
        form_id = auto_incre_form_id()
        header_section = param["header_section"]
        form_section = param["form_section"]
        created_by = param["created_by"]
        created_by_name = param["created_by_name"]
        created_at = timestamp
        check_form = forms_details.find({"form_name": form_name}).count()
        if check_form == 0:
            function = forms_details.insert_one(
                {"form_name": form_name,"form_type":form_type,"form_id":form_id,"header_section":header_section,"form_section":form_section,
                 "created_by":created_by,"created_by_name":created_by_name,"created_at":created_at,"isactive":0})
            form_data = forms_details.find({"form_name": form_name})

            form_data = [json.loads(json.dumps(item, default=json_util.default)) for item in form_data]
            form_data[0]["message"] = "Forms was Successfully Created!!!"
            form_data[0]["save"] = "True"
            res = form_data
            status = 201
        else:
            res = "form already exists!!!"
            status = 409
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res, status

def get_forms(form_name):
    try:
        forms_details = mongo.db.forms
        print(form_name)
        check_form = forms_details.find({"form_name":form_name}).count()
        print(check_form)
        if check_form != 0:
            res = "True"
            status = 200
        else:
            res = "False"
            status = 404
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res, status


def update_form(param):
    try:
        forms_details = mongo.db.forms
        form_name = param["form_name"]
        check_form_name = check_special_char(form_name)
        if check_form_name == True:
            check_form =forms_details.find({"form_id": param["form_id"]}).count()
            print(check_form)
            check_new_form_name = forms_details.find({"form_name": param["new_form_name"]}).count()
            if check_form != 0:
                if check_new_form_name == 0:
                    myquery = {"form_id": param["form_id"]}
                    newvalues = {"$set": {"form_name":param["new_form_name"]}}
                    x = forms_details.update_one(myquery, newvalues)
                    print(x.modified_count)
                    if x.modified_count > 0:
                        form_data = forms_details.find({"form_id": param["form_id"]})
                        form_data = [json.loads(json.dumps(item, default=json_util.default)) for item in form_data]
                        print(form_data)
                        form_data[0]["message"] = "Form Name Details Was Successfully Updated!!!"
                        res = form_data
                        status = 200
                        return res,status
                    else:
                        res = "Form Name Details didn't Updated!!!"
                        status = 407
                        return res, status
                else:
                    res = "Your enter new form name was already exists!!!"
                    status =  409
                    return res,status

            else:
                res = "Form Details Not Found!!!"
                status = 404
                return res, status
        else:
            res = "Please give without special char form name!!!"
            status = 407
            return res, status
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res, status



def delete_forms(form_id):
    try:
        forms_details = mongo.db.forms
        check_form = forms_details.find({"form_id": form_id}).count()
        if check_form != 0:
            forms_details.delete_one({"form_id": form_id})
            res = "Form Was Deleted Successfully!!!"
            status = 200
        else:
            res = "Form Was Not Found!!!"
            status = 404
    except:
        res = "internal server error please try again"
        status = 500
    finally:
        return res, status

def search_form(search_str):
    forms_details = mongo.db.forms
    form_data = forms_details.find({})
    form_data = [json.loads(json.dumps(item, default=json_util.default)) for item in form_data]
    list = []
    for i in form_data:
        for key, value in i.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
            if str(search_str) in str(value):
                if i not in list:
                    print(i)
                    # if age == search_age:
                    list.append(i)
    return list,200














