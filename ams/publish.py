#!/usr/bin/env python

import sys
import logging
import argparse
import ConfigParser
from argo_ams_library import ArgoMessagingService, AmsMessage, AmsException

logger = logging.getLogger("ams.publish")


def publish(config):

    token = config.get("AUTH", "token")
    host = config.get("AMS", "ams_host")
    project = config.get("AMS", "ams_project")
    topic = config.get("AMS", "ams_topic")
    cert_path = config.get("AUTH", "cert_path")
    key_path = config.get("AUTH", "key_path")
    msg_file_path = config.get("AMS", "msg_file_path")

    # initialize service
    if token:
        ams = ArgoMessagingService(endpoint=host, project=project, token=token)
    else:
        ams = ArgoMessagingService(
            endpoint=host,
            project=project,
            cert=cert_path,
            key=key_path)

    data = ''
    with open(msg_file_path, 'r') as ldif:
        data = ldif.read()

    msg = AmsMessage(data=data).dict()
    try:
        ret = ams.publish(topic, msg)
        logger.info(
            "Successfully published message at: %s, ret: %s"
            % (topic, ret))
    except AmsException as e:
        logger.error("Failed to publish message: %s" % e)


def main(args=None):

    f_handler = logging.FileHandler('ams.log')
    f_handler.setFormatter(
        logging.Formatter('%(asctime)s %(name)s [%(levelname)s]: %(message)s'))
    logger.addHandler(f_handler)
    c_handler = logging.StreamHandler()
    logger.addHandler(c_handler)
    logger.setLevel(logging.INFO)

    config = ConfigParser.ConfigParser()
    if args.ConfigPath is None:
        config.read('../conf/settings.conf')
    else:
        config.read(args.ConfigPath)

    publish(config)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Publish ams message")
    parser.add_argument("-c", "--ConfigPath", type=str, help="Cpnfig file path")

    sys.exit(main(parser.parse_args()))
