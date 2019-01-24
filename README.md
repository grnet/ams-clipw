# Cloud info provider wrapper

Python script to publish cloud info to AMS.

`ams-clipw -c <ConfigPath>`

`-c : Path to appropriate config file.`

## Installation 
```buildoutcfg
# git clone https://github.com/grnet/ams-clipw.git
# cd ams-clipw/
# edit the config file with the appropriate settings 
# python setup.py  install
```

## Configuration

Use the `settings.example` to produce your conf file. The project should exist in AMS in advance.
```buildoutcfg
[AMS]
# ams url
ams_host:
# under which ams project the message will be published
ams_project:
# under which ams topic the message will be published  (SITE_<name of site in GOCDB>_ENDPOINT_<identifier of the endpoint in GOCDB>  e.g. SITE_IN2P3-IRES_ENDPOINT_7535G0
ams_topic:
# message body (path to the ldif that cloud info provider produces)
msg_file_path:
# executable to run to obtain ldif output
exec_to_run

[AUTH]
# Use either token or cert_path and key_path
# token to access ams
token:
# certificate path
cert_path:
# key path
key_path:
```
