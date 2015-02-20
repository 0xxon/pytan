
"""
Export a ResultSet from asking a question as CSV with Computer Name and IP Address for the header_sort
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

# setup the export_obj kwargs for later
export_kwargs = {}
export_kwargs["export_format"] = u'csv'
export_kwargs["header_sort"] = [u'Computer Name', u'IP Address']

# ask the question that will provide the resultset that we want to use
ask_kwargs = {
    'qtype': 'manual_human',
    'sensors': [
        "Computer Name", "IP Route Details", "IP Address",
        'Folder Name Search with RegEx Match{dirname=Program Files,regex=.*Shared.*}',
    ],
}
response = handler.ask(**ask_kwargs)

# export the object to a string
# (we could just as easily export to a file using export_to_report_file)
export_kwargs['obj'] = response['question_results']
export_str = handler.export_obj(**export_kwargs)


print ""
print "print the export_str returned from export_obj():"
if len(out.splitlines()) > 15:
    out = out.splitlines()[0:15]
    out.append('..trimmed for brevity..')
    out = '\n'.join(out)

print out


'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258
2015-02-11 12:15:40,504 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:15:45,534 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:15:50,556 INFO     question_progress: Results 50% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:15:55,584 INFO     question_progress: Results 50% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:16:00,610 INFO     question_progress: Results 50% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:16:05,637 INFO     question_progress: Results 100% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)

print the export_str returned from export_obj():
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258
2015-02-11 12:15:15,219 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:15:20,242 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:15:25,266 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:15:30,293 INFO     question_progress: Results 50% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:15:35,321 INFO     question_progress: Results 50% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:15:40,342 INFO     question_progress: Results 100% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)

print the export_str returned from export_obj():
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258
2015-02-11 12:14:04,691 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:14:09,718 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:14:14,741 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:14:19,766 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
2015-02-11 12:14:24,792 INFO     question_progress: Results 0% (Get Computer Name and IP Route Details and IP Address and Folder Name Search with RegEx Match[No, Program Files, No, ] from all machines)
..trimmed for brevity..

'''