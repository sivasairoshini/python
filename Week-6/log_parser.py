#Nmae:T.S.S.Roshini
#Program:To parse log entries using named groups and finditer(), count log levels, redact usernames, and display error entries by user.
import re
log = """2024-06-01 10:30:15 ERROR user=Roshi msg=Login failed
2024-06-01 10:31:20 INFO user=John msg=Login successful
2024-06-01 10:32:10 WARN user=Roshi msg=Password expiring
2024-06-01 10:33:45 ERROR user=John msg=File not found
2024-06-01 10:34:50 ERROR user=Roshi msg=Connection failed
2024-06-01 10:35:30 INFO user=Alice msg=Logged out"""
pattern = r"(?P<timestamp>\S+ \S+) (?P<level>\w+) user=(?P<user>\w+) msg=(?P<msg>.*)"
entries = []
for match in re.finditer(pattern, log):
    entries.append(match.groupdict())
print("Parsed entries:")
print(entries)
error_count = 0
warn_count = 0
info_count = 0
for entry in entries:
    if entry["level"] == "ERROR":
        error_count += 1
    elif entry["level"] == "WARN":
        warn_count += 1
    elif entry["level"] == "INFO":
        info_count += 1
print("\nSummary:")
print("ERROR:", error_count)
print("WARN:", warn_count)
print("INFO:", info_count)
redacted = re.sub(r"user=\w+", "user=<hidden>", log)
print("\nRedacted log:")
print(redacted)
entries.sort(key=lambda x: x["user"])
print("\nERROR entries by user:")
for entry in entries:
    if entry["level"] == "ERROR":
        print(entry)
#output
#Redacted log:
#2024-06-01 10:30:15 ERROR user=<hidden> msg=Login failed
#2024-06-01 10:31:20 INFO user=<hidden> msg=Login successful
#2024-06-01 10:32:10 WARN user=<hidden> msg=Password expiring
#2024-06-01 10:33:45 ERROR user=<hidden> msg=File not found
#2024-06-01 10:34:50 ERROR user=<hidden> msg=Connection failed
#2024-06-01 10:35:30 INFO user=<hidden> msg=Logged out
#
#ERROR entries by user:
#{'timestamp': '2024-06-01 10:33:45', 'level': 'ERROR', 'user': 'John', 'msg': 'File not found'}
#{'timestamp': '2024-06-01 10:30:15', 'level': 'ERROR', 'user': 'Roshi', 'msg': 'Login failed'}
#{'timestamp': '2024-06-01 10:34:50', 'level': 'ERROR', 'user': 'Roshi', 'msg': 'Connection failed'}