# Cloud info provider wrapper

Python script to publish cloud info to AMS.

`publish.py -c <ConfigPath>`

`-c : Path to appropriate config file.`

## Configuration

Use the `settings.example` to produce your conf file. The project should exist in AMS in advance.
```buildoutcfg
[AMS]
# ams url
ams_host:
# under which ams project the message will be published
ams_project:
# under which ams topic the message will be published
ams_topic:
# message body
msg_file_path:

[AUTH]
# Use either token or cert_path and key_path
# token to access ams
token:
# certificate path
cert_path:
# key path
key_path:
```
