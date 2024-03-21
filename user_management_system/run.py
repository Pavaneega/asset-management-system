from flask import Flask, request, make_response, jsonify
from app.api_functions import user_management,function_ids,groups_management,forms,form_approvals,incident_management
from instance import app,mongo
import json


@app.route("/db/tables/creation",methods=["GET"])
def creating_db_tables():
    if request.method == 'GET':
        res, status = user_management.create_db_tables()
        return make_response(jsonify(data=res), status)

@app.route('/platform/create/user/', methods=['POST'])
#@token_required
def create_user():
    if request.method == 'POST':
        params = request.data
        res, status = user_management.create_admin_user(params)
        return make_response(jsonify(data=res),status)

@app.route('/platform/get/user/details/<int:user_id>/',methods=["GET"])
def get_user_details(user_id):
    if request.method == "GET":
        res,status = user_management.get_admin_user_details(user_id)
        return make_response(jsonify(data=res),status)


@app.route('/platform/login/', methods=['POST'])
#@token_required
def login():
    if request.method == "POST":
        params = request.data
        res, status = user_management.user_authentication(params)
        return make_response(jsonify(data=res), status)

@app.route('/platform/user/password/reset/', methods=['PUT'])
def user_reset_password():
    if request.method == "PUT":
        params = request.data
        res, status = user_management.user_password_reset(params)
        return make_response(jsonify(data=res), status)

@app.route('/update/user/email/<int:user_id>/', methods = ["PUT"])
def update_email(user_id):
    if request.method == "PUT":
        params = request.data
        res,status = user_management.update_user_email(params,user_id)
        return make_response(jsonify(data=res), status)

@app.route('/platform/functions', methods = ["POST"])
def create_functions():
    if request.method == "POST":
        params = request.data
        res,status = function_ids.create_function(params)
        return make_response(jsonify(data=res), status)

@app.route("/platform/group/create", methods=["POST"])
def creategroup():
    data = request.data
    data,status= groups_management.create_group(data)
    return make_response(jsonify(data=data), status)

@app.route("/platform/group/users", methods=["POST"])
def create_group_users():
    data = request.data
    data,status= groups_management.create_group_user(data)
    return make_response(jsonify(data=data), status)

@app.route("/platform/get/groups/", methods=["GET"])
def get_groups():
    data,status= groups_management.get_all_groups()
    return make_response(jsonify(data=data), status)

@app.route("/platform/update/group/name/", methods=["PUT"])
def change_group_name():
    data = request.data
    data,status= groups_management.update_group_name(data)
    return make_response(jsonify(data=data), status)

@app.route("/platform/delete/group/", methods=["DELETE"])
def remove_group():
    data = request.data
    data,status = groups_management.delete_group(data)
    return make_response(jsonify(data=data), status)


@app.route("/platform/delete/group/users", methods=["DELETE"])
def remove_group_user():
    data = request.data
    data,status = groups_management.delete_user_from_group(data)
    return make_response(jsonify(data=data), status)

@app.route("/platform/get/specific/group/users", methods=["GET"])
def get_group_users():
    data = request.data
    data,status = groups_management.get_users_from__specific_group(data)
    return make_response(jsonify(data=data), status)


@app.route("/platform/create/chanel", methods=["POST"])
def chanels_creation():
    params = request.data
    data,status = function_ids.create_chanels(params)
    return make_response(jsonify(data=data), status)

@app.route("/platform/update/chanel", methods=["PUT"])
def chanels_update():
    params = request.data
    data,status = function_ids.update_chanel(params)
    return make_response(jsonify(data=data), status)

@app.route("/platform/delete/chanel", methods=["DELETE"])
def remove_chanel():
    params = request.data
    data,status = function_ids.delete_chanel(params)
    return make_response(jsonify(data=data), status)

@app.route("/platform/forms/creation/", methods=["POST"])
def forms_creation():
    if request.method == "POST":
        params = request.data
        data,status = forms.create_forms(params)
        return make_response(jsonify(data=data), status)

@app.route("/platform/forms/hub/<int:form_id>/", methods=["DELETE", "GET", "POST", "PUT"])
def forms_oparations(form_id):
    if request.method == "PUT":
        params = request.data
        params = json.loads(params)
        params["form_id"] = form_id
        data,status = forms.update_form(params)
        return make_response(jsonify(data=data), status)
    elif request.method == "DELETE":
        data,status = forms.delete_forms(form_id)
        return make_response(jsonify(data=data), status)

@app.route("/platform/forms/hub/<string:form_name>/", methods=["GET"])
def check_form_name(form_name):
    if request.method == "GET":
        data,status = forms.get_forms(form_name)
        return make_response(jsonify(data=data), status)

@app.route("/platform/forms/search/<string:search_str>/", methods=["GET"])
def forms_search(search_str):
    if request.method == "GET":
        data,status = forms.search_form(search_str)
        return make_response(jsonify(data=data), status)

@app.route("/platform/forms/active/inactive/form_id/<int:form_id>/permission_id/<int:permission_id>/", methods=["PUT"])
def forms_permissions(form_id,permission_id):
    if request.method == "PUT":
        data,status = form_approvals.form_permission(form_id,permission_id)
        return make_response(jsonify(data=data), status)



'''add,delete and get group to form'''
@app.route('/platform/manageforms/with/groups/formid/<int:form_id>',methods=['GET','POST','DELETE'])
#@token_required
def manage_forms_with_groups(form_id):
    if request.method=='POST':
        data=request.data
        data,status=form_approvals.add_group_to_form(form_id,data)
        return make_response(jsonify(data=data), status)
    if request.method=='DELETE':
        data=request.data
        data,status=form_approvals.delete_group_to_form(form_id,data)
        return make_response(jsonify(data = data),status)
    elif request.method=='GET':
        data,status=form_approvals.get_groups_forms(form_id)
        return make_response(jsonify(data = data),status)

'''add,delete and get chanel to form'''
@app.route('/platform/manageforms/with/chanels/formid/<int:form_id>',methods=['GET','POST','DELETE'])
#@token_required
def manage_forms_with_chanels(form_id):
    if request.method=='POST':
        data=request.data
        data,status=form_approvals.add_chanel_to_form(form_id,data)
        return make_response(jsonify(data=data), status)
    if request.method=='DELETE':
        data=request.data
        data,status=form_approvals.delete_chanel_from_form(form_id,data)
        return make_response(jsonify(data = data),status)
    elif request.method=='GET':
        data,status=form_approvals.get_chanel_forms(form_id)
        return make_response(jsonify(data = data),status)

# This private API is used to create a unique Order ID for new incident in postgres
@app.route('/platform/api/v1.0/web/user/<int:user_id>/create_channel_incident/', methods=['GET'])
def create_channel_incident_id(user_id):
    data,status=incident_management.api_create_incident(user_id)
    return make_response(jsonify(data),status)

#/sg2/api/v1.0/incidents/web/create_order/
@app.route("/service/ticket/creation/", methods=["POST"])
def create_ticket():
    if request.method == "POST":
        data = request.data
        data,status = incident_management.ticket_creation(data)
        return make_response(jsonify(data=data), status)
@app.route("/service/ticket/accept/user/<int:user_id>/incident/status/<int:incident_status>", methods=["GET"])
def ticket_accept():
    if request.method == "GET":
        data = request.data
        data,status = incident_management.incident_accept(data)
        return make_response(jsonify(data=data), status)


# @app.route("/detail/", methods = ['GET'])
# def detail(user_id=2):
# 	detail = mongo.db.users
# 	user = detail.insert_one({"user_id":user_id})
# 	return "success"





if __name__ == '__main__':
    app.run(debug=True,port=5004)


'''
server starting error : socket.error: [Errno 98] Address already in use
'''
#app.run(debug=True)
#error:socket.error: [Errno 98] Address already in use

#resolve : app.run(debug=True, port=0)
#change port number
