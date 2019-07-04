#!/usr/bin/env python

import os
import logging
import argparse
import ConfigParser
import subprocess
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
    info_provider_path = config.get("AMS", "info_provider_path")

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
    if info_provider_path:
        try:
            data = subprocess.check_output(
                [info_provider_path],
                shell=True)
        except subprocess.CalledProcessError as cpe:
            logger.error(cpe)
            return
    else:
        try:
            with open(msg_file_path, 'r') as ldif:
                data = ldif.read()
        except IOError as ioe:
            logger.error(ioe)
            return

    msg = AmsMessage(data=data).dict()
    try:
        ret = ams.publish(topic, msg)
        logger.info(
            "Successfully published message at: %s, ret: %s"
            % (topic, ret))
    except AmsException as e:
        logger.error("Failed to publish message: %s" % e)


def main():

    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CONF_FILE = os.path.join(ROOT_DIR, 'conf', 'settings.conf')

    LOG_FILE = os.path.join(ROOT_DIR, 'ams.log')
    f_handler = logging.FileHandler(LOG_FILE)
    f_handler.setFormatter(
        logging.Formatter('%(asctime)s %(name)s [%(levelname)s]: %(message)s'))
    logger.addHandler(f_handler)
    c_handler = logging.StreamHandler()
    logger.addHandler(c_handler)
    logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description="Publish ams message")
    parser.add_argument("-c", "--ConfigPath", type=str, help="Config file path")
    args = parser.parse_args()

    config = ConfigParser.ConfigParser()
    if args and args.ConfigPath:
        config.read(args.ConfigPath)
    else:
        config.read(CONF_FILE)

    publish(config)
