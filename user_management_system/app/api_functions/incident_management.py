import json
from instance import db
from app.utils.current_time import get_current_epoc_time
from app.models.incidents import incidents
from sqlalchemy import desc
from instance import app,mongo
from instance.dbconfig import base_url
from app.utils import current_time,password_hash,current_time
timestamp = current_time.get_current_epoc_time()
import re
import request
import requests

from sqlalchemy.exc import IntegrityError

#simple function to create a uniqye ID in Postgres for new incidents
def api_create_incident(user_id):
    try:
        timestamp = get_current_epoc_time()
        incident=incidents(
            created_on=timestamp,
            created_by=user_id
            )
        db.session.add(incident)
        db.session.commit()
        incident_id = incidents.query.order_by(desc(incidents.created_on)).first().incident_id
        status=201
        data={"incident_id":incident_id}
        #return data,status
    except Exception as ex:
        print ex
        status = 500
        data = "An Unexpected error occured in our Servers. Please try again"
    finally:
        return data, status

#todo incident creation
#note : 1 for created ,2 for accepted ,4 for submitted ,5 for draft ,7 for
def ticket_creation(data):
    try:
        service_incidents = mongo.db.service_incidents
        time_stamp = current_time.get_current_epoc_time()
        data = json.loads(data)
        user_id = data["created_by_user_id"]
        incident_id=requests.get(base_url+'/platform/api/v1.0/web/user/'+str(user_id)+'/create_channel_incident/').json()['incident_id']
        print("incident_id:",incident_id)
        new_incident_id = data["channel_code"][0:4] + "000000INC" + str(incident_id)
        following_users = [str(i["u_name"]) for i in data["assigned_users"]]
        following_users_str = ','.join(following_users)
        ticket_data = {}
        ticket_data["created_by"] = user_id
        ticket_data["assigned_users"]  = data["assigned_users"]
        ticket_data["form_id"]  = data["form_id"]
        ticket_data["priority"]  = data["priority"]
        ticket_data["sprint"]  = data["sprint"]
        ticket_data["start_time"]  = timestamp
        ticket_data["end_time"]  = data["end_time"]
        ticket_data["incident_id"] = new_incident_id
        ticket_data["status"] = 1
        ticket_data = service_incidents.insert_one(ticket_data)
        data = "An incident with Incident id " + new_incident_id + " is  created and assigned to the following users " + following_users_str + " "
        status = 201
    except Exception as ex:
        print ex
        data = "An unexpected error occured in our servers. Please try again."
        status = 500
    finally:
        return data, status

def incident_accept(data):
    pass