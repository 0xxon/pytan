Print Server Info Readme
===========================

---------------------------
<a name='toc'>Table of contents:</a>

  * [Help for Print Server Info](#user-content-help-for-print-server-info)
  * [Print the server info in JSON format](#user-content-print-the-server-info-in-json-format)

---------------------------

# Help for Print Server Info

  * Print the help for print_server_info.py
  * All scripts in bin/ will supply help if -h is on the command line
  * If passing in a parameter with a space or a special character, you need to surround it with quotes properly. On Windows this means double quotes. On Linux/Mac, this means single or double quotes, depending on what kind of character escaping you need.
  * If running this script on Linux or Mac, use the python scripts directly as the bin/print_server_info.py
  * If running this script on Windows, use the batch script in the winbin/print_server_info.bat so that python is called correctly.

```bash
print_server_info.py -h
```

```
usage: print_server_info.py [-h] [-u USERNAME] [-p PASSWORD]
                            [--session_id SESSION_ID] [--host HOST]
                            [--port PORT] [-l LOGLEVEL] [--debugformat]
                            [--debug_method_locals] [--record_all_requests]
                            [--stats_loop_enabled] [--http_auth_retry]
                            [--http_retry_count HTTP_RETRY_COUNT]
                            [--pytan_user_config PYTAN_USER_CONFIG] [--json]

Prints server information to stdout

optional arguments:
  -h, --help            show this help message and exit

Handler Authentication:
  -u USERNAME, --username USERNAME
                        Name of user (default: None)
  -p PASSWORD, --password PASSWORD
                        Password of user (default: None)
  --session_id SESSION_ID
                        Session ID to authenticate with instead of
                        username/password (default: None)
  --host HOST           Hostname/ip of SOAP Server (default: None)
  --port PORT           Port to use when connecting to SOAP Server (default:
                        443)

Handler Options:
  -l LOGLEVEL, --loglevel LOGLEVEL
                        Logging level to use, increase for more verbosity
                        (default: 0)
  --debugformat         Enable debug format for logging (default: False)
  --debug_method_locals
                        Enable debug logging for each methods local variables
                        (default: False)
  --record_all_requests
                        Record all requests in
                        handler.session.ALL_REQUESTS_RESPONSES (default:
                        False)
  --stats_loop_enabled  Enable the statistics loop (default: False)
  --http_auth_retry     Disable retry on HTTP authentication failures
                        (default: True)
  --http_retry_count HTTP_RETRY_COUNT
                        Retry count for HTTP failures/invalid responses
                        (default: 5)
  --pytan_user_config PYTAN_USER_CONFIG
                        PyTan User Config file to use for PyTan arguments
                        (defaults to: ~/.pytan_config.json) (default: )

Output Options:
  --json                Show a json dump of the server information (default:
                        False)
```

  * Validation Test: exitcode
    * Valid: **True**
    * Messages: Exit Code is 0

  * Validation Test: noerror
    * Valid: **True**
    * Messages: No error texts found in stderr/stdout



[TOC](#user-content-toc)


# Print the server info in JSON format

```bash
bin/print_server_info.py -u Administrator -p 'Tanium2015!' --host 10.0.1.240 --port 443 --loglevel 1 --json
```

```
PyTan v2.1.5 Handler for Session to 10.0.1.240:443, Authenticated: True, Platform Version: 6.5.314.4301
{
  "Action History Cache": {
    "Action Stop Count": 1, 
    "Actions": 96
  }, 
  "Active Question Cache": {
    "Active Client Estimate": 3, 
    "Active Question Estimate": 50
  }, 
  "Authenticator": {
    "ActiveSessions": 1, 
    "TotalSessions": 980
  }, 
  "Client Pump": {
    "Connections Active": 2, 
    "Connections Inactive": 2, 
    "Connections Stopped": 96
  }, 
  "Data Interface": {
    "Estimated Node Count": 3, 
    "License Seat Cap": 60, 
    "Reg Connection Count": 0, 
    "Reg Connection Limit": 1000, 
    "Report Cache Count": 60, 
    "Sensor Bytes Per Second Limit": 5242880, 
    "Sensor Bytes Sent Since Last Time": 0, 
    "Sensor Connection Count": 0, 
    "Sensor Connection Limit": 8
  }, 
  "File Request Handler": {
    "Chunk Bytes Sent Since Last Time": 0, 
    "Download Bytes Sent Since Last Time": 0, 
    "Download Connection Count": 0, 
    "Download Connection Limit": 1000
  }, 
  "Group Cache": {
    "ComputerSpecs": 0, 
    "ComputerSpecsGroups": 0, 
    "FilterSpecCount": 210, 
    "GroupCount": 376, 
    "GroupsActionGroupSpecs": 0, 
    "GroupsComputerSpecs": 0, 
    "GroupsTempSensors": 31, 
    "QuestionFilterSpecs": 33, 
    "QuestionSelectSpecs": 2423, 
    "QuestionSubGroups": 508, 
    "QuestionTextCount": 0, 
    "SavedQuestionTextCount": 117, 
    "SelectSpecCount": 2987
  }, 
  "HTTP File Cache": {
    "Cached File Count": 108, 
    "File Cache Size": 7966121
  }, 
  "Memory Info": {
    "DoubleFreeCount": "0", 
    "NonTBBFreeCount": "0", 
    "PageFaultCount": "10919925", 
    "PagefileUsage": "1671671808", 
    "PeakPagefileUsage": "2148749312", 
    "PeakWorkingSetSize": "1.74 GB", 
    "QuotaPagedPoolUsage": "692648", 
    "QuotaPeakNonPagedPoolUsage": "4257020", 
    "QuotaPeakPagedPoolUsage": "698312", 
    "WorkingSetSize": "206.95 MB"
  }, 
  "Module Cache": {
    "127.0.0.1:17477 Module Count": 30, 
    "Module Definition Count": 32
  }, 
  "Network": {
    "Allocated SendOp Count": 201, 
    "Allocated SendOp Limit": 0, 
    "Concurrency": 32, 
    "Concurrency Threads": 33, 
    "Idle Threads": 33, 
    "Max Concurrency Threads": 64, 
    "Min Available Threads": 29, 
    "Pending SendOp Count": 0, 
    "Queue Completion Timeout": 1000, 
    "Running Threads": 33, 
    "SendOpReady FreeCount": 0, 
    "SendOpReady HeadCount": 201, 
    "Threads Reset Interval": 0, 
    "Unpaused Threads": 33
  }, 
  "Package Cache": {
    "Package Count": 103, 
    "Package File Count": 340
  }, 
  "Question History": {
    "History Limit Days": 7, 
    "Last Question ID": 2470, 
    "Last Saved Question ID": 117, 
    "Question Count": 2370
  }, 
  "SOAP Network": {
    "Allocated SendOp Count": 292, 
    "Allocated SendOp Limit": 0, 
    "Concurrency": 32, 
    "Concurrency Threads": 33, 
    "Idle Threads": 32, 
    "Max Concurrency Threads": 64, 
    "Min Available Threads": 26, 
    "Pending SendOp Count": 0, 
    "Queue Completion Timeout": 1000, 
    "Running Threads": 33, 
    "SendOpReady FreeCount": 0, 
    "SendOpReady HeadCount": 292, 
    "Threads Reset Interval": 14400, 
    "Unpaused Threads": 33
  }, 
  "SOAP Pump": {
    "Connections Active": 5, 
    "Connections Inactive": 0, 
    "Connections Stopped": 95
  }, 
  "SOAP Server": {
    "Connections": 5, 
    "Last Reset": "2015-09-15 05:00:00 +0000", 
    "SOAP Busy Handlers": 104, 
    "SOAP Handlers": 0, 
    "Use Compression": "true", 
    "Using IPv6": "true", 
    "Using Keep-Alive": "true", 
    "Using NTLM": "false"
  }, 
  "SOAP Snapshots": {
    "Snapshot Count": 0
  }, 
  "SOAP Timing": {
    "Timing: action": "Average 1ms, Count: 32434, Last: 0ms", 
    "Timing: actions": "Average 0ms, Count: 27, Last: 0ms", 
    "Timing: client_count": "Average 0ms, Count: 5, Last: 0ms", 
    "Timing: client_status": "Average 0ms, Count: 46, Last: 0ms", 
    "Timing: group": "Average 7ms, Count: 88, Last: 0ms", 
    "Timing: groups": "Average 3ms, Count: 96, Last: 0ms", 
    "Timing: package_spec": "Average 1ms, Count: 364, Last: 0ms", 
    "Timing: plugins": "Average 9ms, Count: 5, Last: 16ms", 
    "Timing: question": "Average 9ms, Count: 395, Last: 31ms", 
    "Timing: questions": "Average 15ms, Count: 51, Last: 31ms", 
    "Timing: roles": "Average 0ms, Count: 74, Last: 0ms", 
    "Timing: saved_actions": "Average 3ms, Count: 131, Last: 14ms", 
    "Timing: saved_question": "Average 75ms, Count: 218, Last: 15ms", 
    "Timing: saved_questions": "Average 24ms, Count: 33, Last: 14ms", 
    "Timing: sensor": "Average 9ms, Count: 19, Last: 16ms", 
    "Timing: sensors": "Average 5ms, Count: 654, Last: 31ms", 
    "Timing: system_setting": "Average 4ms, Count: 137, Last: 0ms", 
    "Timing: system_settings": "Average 3ms, Count: 51, Last: 0ms", 
    "Timing: system_status": "Average 0ms, Count: 290, Last: 0ms", 
    "Timing: user": "Average 0ms, Count: 78, Last: 0ms", 
    "Timing: users": "Average 0ms, Count: 99, Last: 0ms", 
    "Timing: white_listed_url": "Average 0ms, Count: 34, Last: 0ms", 
    "Timing: white_listed_urls": "Average 0ms, Count: 100, Last: 0ms"
  }, 
  "Sensor Cache": {
    "Active Preview Sensor Count": 0, 
    "Available Preview Sensor Count": 0, 
    "Preview Sensor Count": 0, 
    "Sensor Count": 505, 
    "Waiting Preview Sensor Count": 0
  }, 
  "Settings": {
    "AllowOldSessionID": "false", 
    "Client Count": "4", 
    "PreFetchRows": "1000", 
    "Server Start Time": "2015-09-14 13:37:35 +0000", 
    "Server Up-Time": "1967 minutes", 
    "ServerName": "0.0.0.0", 
    "ServerPort": "17472", 
    "ServerSOAPPort": "443", 
    "UseSOAPIOCP": "true", 
    "UseTBBAllocator": "true", 
    "UseTBBAllocatorStats": "false", 
    "UseTBBScalingAlignment": "false", 
    "Version": "6.5.314.4301"
  }, 
  "String Cache": {
    "NameData": 653, 
    "Sensor 131549066 Refresh Time/String Count": "1 / 2", 
    "Sensor 1487792243 Refresh Time/String Count": "1 / 19", 
    "Sensor 1487793983 Refresh Time/String Count": "1 / 19", 
    "Sensor 1487795723 Refresh Time/String Count": "1 / 19", 
    "Sensor 1487993648 Refresh Time/String Count": "1 / 19", 
    "Sensor 1487994518 Refresh Time/String Count": "1 / 19", 
    "Sensor 1487995388 Refresh Time/String Count": "1 / 3", 
    "Sensor 1488397328 Refresh Time/String Count": "1 / 19", 
    "Sensor 1488545663 Refresh Time/String Count": "1 / 19", 
    "Sensor 1488547403 Refresh Time/String Count": "1 / 3", 
    "Sensor 1488548273 Refresh Time/String Count": "1 / 19", 
    "Sensor 1488549143 Refresh Time/String Count": "1 / 19", 
    "Sensor 1488747938 Refresh Time/String Count": "1 / 19", 
    "Sensor 1488748808 Refresh Time/String Count": "1 / 3", 
    "Sensor 1488749678 Refresh Time/String Count": "1 / 18", 
    "Sensor 1488750548 Refresh Time/String Count": "1 / 19", 
    "Sensor 1488751418 Refresh Time/String Count": "1 / 19", 
    "Sensor 1488940643 Refresh Time/String Count": "1 / 19", 
    "Sensor 1488941513 Refresh Time/String Count": "1 / 19", 
    "Sensor 1488942383 Refresh Time/String Count": "1 / 3", 
    "Sensor 1488943253 Refresh Time/String Count": "1 / 18", 
    "Sensor 1489142048 Refresh Time/String Count": "1 / 19", 
    "Sensor 1489142918 Refresh Time/String Count": "1 / 19", 
    "Sensor 1489143788 Refresh Time/String Count": "1 / 19", 
    "Sensor 1489144658 Refresh Time/String Count": "1 / 19", 
    "Sensor 1489694498 Refresh Time/String Count": "1 / 19", 
    "Sensor 1489695803 Refresh Time/String Count": "1 / 3", 
    "Sensor 1489696673 Refresh Time/String Count": "1 / 19", 
    "Sensor 1489698413 Refresh Time/String Count": "1 / 19", 
    "Sensor 1489887203 Refresh Time/String Count": "1 / 19", 
    "Sensor 1489888943 Refresh Time/String Count": "1 / 19", 
    "Sensor 1511329504 Refresh Time/String Count": "1 / 1755", 
    "Sensor 1559751995 Refresh Time/String Count": "1 / 25", 
    "Sensor 1688928675 Refresh Time/String Count": "1 / 8", 
    "Sensor 1782389954 Refresh Time/String Count": "1 / 5", 
    "Sensor 1792443391 Refresh Time/String Count": "1 / 139", 
    "Sensor 2581054686 Refresh Time/String Count": "1 / 5", 
    "Sensor 2634431519 Refresh Time/String Count": "1 / 5", 
    "Sensor 3005061811 Refresh Time/String Count": "1 / 2", 
    "Sensor 3209138996 Refresh Time/String Count": "1 / 6", 
    "Sensor 3209246640 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209252730 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209449785 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209452395 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209453265 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209454135 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209653365 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209654235 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209655105 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209655975 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209656845 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209845635 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209846070 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209846505 Refresh Time/String Count": "1 / 3", 
    "Sensor 3209846940 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209847810 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209848680 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209991360 Refresh Time/String Count": "1 / 19", 
    "Sensor 3209993535 Refresh Time/String Count": "1 / 3", 
    "Sensor 3209993970 Refresh Time/String Count": "1 / 19", 
    "Sensor 3210193200 Refresh Time/String Count": "1 / 19", 
    "Sensor 3210194070 Refresh Time/String Count": "1 / 19", 
    "Sensor 3210194940 Refresh Time/String Count": "1 / 19", 
    "Sensor 3210195810 Refresh Time/String Count": "1 / 19", 
    "Sensor 3210199290 Refresh Time/String Count": "1 / 19", 
    "Sensor 3210399390 Refresh Time/String Count": "1 / 19", 
    "Sensor 3210599055 Refresh Time/String Count": "1 / 18", 
    "Sensor 3210601665 Refresh Time/String Count": "1 / 19", 
    "Sensor 3210602535 Refresh Time/String Count": "1 / 19", 
    "Sensor 3210603405 Refresh Time/String Count": "1 / 19", 
    "Sensor 322086833 Refresh Time/String Count": "1 / 47", 
    "Sensor 3409330187 Refresh Time/String Count": "1 / 5", 
    "Sensor 3556221173 Refresh Time/String Count": "1 / 4", 
    "Sensor 435227963 Refresh Time/String Count": "1 / 10", 
    "Sensor 45421433 Refresh Time/String Count": "1 / 4", 
    "Sensor 607666494 Refresh Time/String Count": "1 / 3", 
    "Sensor 7318847 Refresh Time/String Count": "1 / 5", 
    "Sensor 889071797 Refresh Time/String Count": "1 / 8", 
    "Total String Count": 3063
  }, 
  "System Performance Info": {
    "CommitLimit": "4193616", 
    "CommitPeak": "1104707", 
    "CommitTotal": "874946", 
    "HandleCount": "37676", 
    "KernelNonpaged": "15045", 
    "KernelPaged": "50850", 
    "KernelTotal": "65895", 
    "PageSize": "4096", 
    "PhysicalAvailable": "1529776", 
    "PhysicalTotal": "2097038", 
    "ProcessCount": "52", 
    "ProcessThreadCount": "739", 
    "SystemCache": "600098"
  }, 
  "System Status Cache": {
    "System Count": 3, 
    "blocked_count": 0, 
    "leader_count": 3, 
    "normal_count": 0, 
    "receive_backward_count": 1, 
    "receive_forward_count": 0, 
    "receive_none_count": 1, 
    "receive_ok_count": 1, 
    "send_backward_count": 1, 
    "send_forward_count": 2, 
    "send_none_count": 0, 
    "send_ok_count": 0, 
    "slowlink_count": 0, 
    "version_details_5.1.314.7724": "count: 1 filtered: 0", 
    "version_details_6.0.314.1195": "count: 2 filtered: 2", 
    "version_details_6.0.314.1321": "count: 1 filtered: 1"
  }
}
```

  * Validation Test: exitcode
    * Valid: **True**
    * Messages: Exit Code is 0

  * Validation Test: noerror
    * Valid: **True**
    * Messages: No error texts found in stderr/stdout



[TOC](#user-content-toc)


###### generated by: `build_bin_doc v2.1.0`, date: Tue Sep 15 18:25:54 2015 EDT, Contact info: **Jim Olsen <jim.olsen@tanium.com>**