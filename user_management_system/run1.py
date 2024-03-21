from flask import Flask,request, make_response, jsonify
from flask_pymongo import PyMongo
import json
from bson import json_util

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Mongo_Queries'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Mongo_Queries'
app.config['SECRET_KEY'] = 'some-secret-string'

mongo = PyMongo(app)

#TODO INSERTED ONE DATA TO MONGODB :

'''insert_one({detail})'''
@app.route("/insert_one",methods=["GET"])
def insert_one():
        student_details = mongo.db.students_data #student data is the collection name
        one_student_data = {"name":"ramu reddy","job":"web developer","roll":33,"batch":2013}
        query = student_details.insert_one(one_student_data)
        return "successfully insert one student data"

#TODO INSERTED ONE DATA TO MONGODB :

'''insert_many({details})'''
@app.route("/insert_many",methods=["GET"])
def insert_many():
        student_details = mongo.db.students_data #student data is the collections
        many_student_data = [{"name":"sreenu","job":"civil engineer","roll":22,"batch":2017},{"name":"pavan","job":"pyhton developer","roll":33,"batch":2013}]
        query = student_details.insert_many(many_student_data)
        return "successfully insert many student data"

#TODO INSERTED ONE/MANY DATA TO MONGODB :

'''insert({detail/details})''' #insert one or many data insert with this function
@app.route("/insert",methods=["GET"])
def insert():
        student_details = mongo.db.students_data #student data is the collections
        student_data =[{"name":"praveen","job":"app developer","roll":33,"batch":2020,"name":"pradeep","job":"testing developer","roll":34,"batch":2020}]
        data = student_details.insert_many(student_data)
        return "successfully insert student data"

#TODO SEARCHING ONE DATA FROM MONGODB :

'''find_one()'''
@app.route("/find_one",methods=["GET"])
def find_one():
        student_details = mongo.db.students_data
        query = student_details.find_one() # Getting first one of the data from the collection
        query1 = student_details.find_one({"name":"rajesh reddy"}) # Search_one_data_with_specific_field(first filter all data and finally, getting first match data from all matches)
        query2 = student_details.find_one({"name":"praveen","job":"app developer"}) # Search_one_data_with_specific_fields
        search_one_student_data = json.loads(json.dumps(query, default=json_util.default))
        search_one_student_data_with_specific_query = json.loads(json.dumps(query1, default=json_util.default))
        search_one_student_data_with_specific_queries= json.loads(json.dumps(query2, default=json_util.default))
        return {"data":[search_one_student_data,search_one_student_data_with_specific_query,search_one_student_data_with_specific_queries]}

#TODO SEARCHING OR FILTERING MANY DATA FROM MONGODB : 

'''find({})'''
@app.route("/find",methods=["GET"])
def find():
        student_details = mongo.db.students_data
        query = student_details.find({}) # Getting all the data from the collection
        get_all_data = [json.loads(json.dumps(data, default=json_util.default)) for data in query]
        query1 = student_details.find({"roll":33}) # filter all the data with specific field or fields
        filter_data = [json.loads(json.dumps(data, default=json_util.default)) for data in query1]
        query2 = student_details.find({"name":{"$regex":"^r"}}) # Search all documents with regex object
        regex_filter_data = [json.loads(json.dumps(data, default=json_util.default)) for data in query2]
        return {"get_all_data":get_all_data,"filter_all_data":filter_data,"regex_filter_data":regex_filter_data}


#TODO Assending :
'''find({}).sort("field",1)'''
@app.route("/ ",methods=["GET"])
def assending():
        student_details = mongo.db.students_data
        query = student_details.find({}).sort("batch",1)
        assending_data = [json.loads(json.dumps(data, default=json_util.default)) for data in query]
        return {"assending_data":assending_data}

#TODO deassending
'''find({}).sort("field",-1)'''
@app.route("/deassending",methods=["GET"])
def deassending():
        student_details = mongo.db.students_data
        query = student_details.find({}).sort("batch",-1)
        deassending_data = [json.loads(json.dumps(data, default=json_util.default)) for data in query]
        return {"assending_data":deassending_data}

#TODO limit
@app.route("/limit",methods=["GET"])
def limit():
        student_details = mongo.db.students_data
        query = student_details.find({}).sort("batch",-1).limit(1)
        limit_data = [json.loads(json.dumps(data, default=json_util.default)) for data in query]
        return {"assending_with_limit_data:":limit_data}

#TODO skip
@app.route("/skip",methods=["GET"])
def skip():
        student_details = mongo.db.students_data
        query = student_details.find({}).sort("batch",-1).skip(5).limit(1)
        skip_data = [json.loads(json.dumps(data, default=json_util.default)) for data in query]
        return {"after_skip_data:":skip_data}


#Todo Operators
#Todo 1. Comparison :
#Todo $eq  syntax: { <field>: { $eq: <value> } }
#The $eq operator matches documents where the value of a field equals the specified value.
@app.route("/$eq",methods=["GET"])
def eq():
        inventory_details = mongo.db.inventory
        inventory_data = [
                {'item': { 'name': "ab", 'code': "123" }, 'qty': 15, 'tags': [ "A", "B", "C" ] }
                ,{'item': { 'name': "cd", 'code': "123" }, 'qty': 20, 'tags': [ "B" ] }
                ,{'item': { 'name': "ij", 'code': "456" }, 'qty': 25, 'tags': [ "A", "B" ] }
                ,{'item': { 'name': "xy", 'code': "456" }, 'qty': 30, 'tags': [ "B", "A" ] }
                ,{'item': { 'name': "mn", 'code': "000" }, 'qty': 20, 'tags': [ [ "A", "B" ], "C" ] }
        ]
        #inventory_details.insert(inventory_data)
        fetch_dict_documents = inventory_details.find( { 'qty': { '$in': [20] } } )
        eq_data = [json.loads(json.dumps(data, default=json_util.default)) for data in fetch_dict_documents]
        return {"after_skip_data:":eq_data}







if __name__ == '__main__':
    app.run(debug=True,port=5001)