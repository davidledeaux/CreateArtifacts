import sys
import urllib3
import time
import lorem
import random

from random import randint
from pyral import Rally, rallyWorkset

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
args    = [arg for arg in sys.argv[1:] if arg not in options]
server, user, password, apikey, workspace, project = rallyWorkset(options)

rally = Rally(server, user, password, workspace=workspace, project=project, verify_ssl_cert=False)
rally.enableLogging(dest=b'create_defects.log', attrget=True)

defect_states = ['Submitted','Open','Fixed','Closed']
schedule_states = ['Defined','In-Progress','Completed']
task_states = ['Defined','In-Progress','Completed']

num_tasks = 0

i = 0
while i < 1000:

    # Determine if the upcoming artifact will have any tasks; 1 in 6 chance
    if randint(0,5) == 5:
        num_tasks = randint(0,5)

    if randint(0,1) == 1:
        artifact_type = "Defect"
        artifact_data = { "Name" : lorem.sentence(), "State" : defect_states[randint(0,3)], "ScheduleState" : schedule_states[randint(0,2)], "Description" : lorem.paragraph() }

    else:
        artifact_type = "HierarchicalRequirement"
        artifact_data = { "Name" : lorem.sentence(), "ScheduleState" : schedule_states[randint(0,2)], "Description" : lorem.paragraph() }

    artifact = rally.create(artifact_type, artifact_data)
    print("{artifact_type} created, ObjectID: {object_id}  FormattedID: {formatted_id}".format(artifact_type=artifact_type, object_id=artifact.oid, formatted_id=artifact.FormattedID))

    if num_tasks:
        for x in range(0, num_tasks):
            task_data = { "Name" : lorem.sentence(), "State": task_states[randint(0,2)], "WorkProduct": artifact.ref }                      
            task = rally.create("Task", task_data)
            print("Task created, ObjectID: {object_id}  FormattedID: {formatted_id}".format(object_id=task.oid, formatted_id=task.FormattedID))
            
        num_tasks = 0
        


    i += 1
    
