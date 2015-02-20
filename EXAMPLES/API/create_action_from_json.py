
"""
Export an action object to a JSON file, then create a new action object from the exported JSON file. Actions can not be deleted, so do not delete it. This will, in effect, 're-deploy' an action.
"""
# Path to lib directory which contains pytan package
PYTAN_LIB_PATH = '../lib'

# connection info for Tanium Server
USERNAME = "Tanium User"
PASSWORD = "T@n!um"
HOST = "172.16.31.128"
PORT = "444"

# Logging conrols
LOGLEVEL = 2
DEBUGFORMAT = False

import sys, tempfile
sys.path.append(PYTAN_LIB_PATH)

import pytan
handler = pytan.Handler(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    loglevel=LOGLEVEL,
    debugformat=DEBUGFORMAT,
)

print handler

# set the attribute name and value we want to add to the original object (if any)
attr_name = ""
attr_add = ""

# delete object before creating it?
delete = False

# setup the arguments for getting an object to export as json file
get_kwargs = {}
get_kwargs["objtype"] = u'action'
get_kwargs["id"] = 1


# get objects to use as an export to JSON file
orig_objs = handler.get(**get_kwargs)

# if attr_name and attr_add exists, modify the orig_objs to add attr_add to the attribute
# attr_name
if attr_name:
    for x in orig_objs:
        new_attr = getattr(x, attr_name)
        new_attr += attr_add
        setattr(x, attr_name, new_attr)
        if delete:
            # delete the object in case it already exists
            del_kwargs = {}
            del_kwargs[attr_name] = new_attr
            del_kwargs['objtype'] = u'action'
            try:
                handler.delete(**del_kwargs)
            except Exception as e:
                print e

# export orig_objs to a json file
json_file, results = handler.export_to_report_file(
    obj=orig_objs,
    export_format='json',
    report_dir=tempfile.gettempdir(),
)

# create the object from the exported JSON file
create_kwargs = {'objtype': u'action', 'json_file': json_file}
response = handler.create_from_json(**create_kwargs)


print ""
print "Type of response: ", type(response)

print ""
print "print of response:"
print response

print ""
print "print the object returned in JSON format:"
print response.to_json(response)


'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258
2015-02-11 12:06:40,662 INFO     handler: Report file '/var/folders/dk/vjr1r_c53yx6k6gzp2bbt_c40000gn/T/ActionList_2015_02_11-12_06_40-EST.json' written with 1221 bytes
2015-02-11 12:06:40,735 INFO     handler: New Action, name: 'Unmanaged Asset Tracking - Run Scan' (ID: 1373) created successfully!

Type of response:  <class 'taniumpy.object_types.action_list.ActionList'>

print of response:
ActionList, len: 1

print the object returned in JSON format:
{
  "_type": "actions", 
  "action": [
    {
      "_type": "action", 
      "action_group": {
        "_type": "group", 
        "id": 0, 
        "name": "Default"
      }, 
      "comment": "Scans for unmanaged assets on the network.", 
      "creation_time": "2015-02-11T17:06:40", 
      "distribute_seconds": 600, 
      "expiration_time": "2015-02-09T05:22:09", 
      "expire_seconds": 3000, 
      "history_saved_question": {
        "_type": "saved_question", 
        "id": 180
      }, 
      "id": 1373, 
      "name": "Unmanaged Asset Tracking - Run Scan", 
      "package_spec": {
        "_type": "package_spec", 
        "command": "cmd /c start /B cscript //T:3600 ..\\..\\Tools\\run-ua-scan.vbs /RANDOM_WAIT_TIME_IN_SECONDS:240", 
        "id": 6, 
        "name": "Run Unmanaged Asset Scanner"
      }, 
      "saved_action": {
        "_type": "saved_action", 
        "id": 47
      }, 
      "skip_lock_flag": 0, 
      "start_time": "2015-02-09T04:32:09", 
      "status": "Active", 
      "stopped_flag": 0, 
      "target_group": {
        "_type": "group", 
        "id": 65, 
        "name": "Default"
      }, 
      "user": {
        "_type": "user", 
        "group_id": 0, 
        "id": 2, 
        "last_login": "2015-02-09T04:32:09", 
        "name": "Tanium User"
      }
    }
  ]
}

'''