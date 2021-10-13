import os
import configparser
from pathlib import Path
import logging
from logging.config import fileConfig


def parser():
    config_path = Path(os.getenv("{{cookiecutter.project_name}}_config"), "appconfig.cfg")
    conf_parser = configparser.ConfigParser()
    conf_parser.read(config_path)
    return conf_parser


def log_parser():
    log_config = Path(os.getenv("{{cookiecutter.project_name}}_config"), "logging.cfg")
    fileConfig(log_config)
    logger = logging.getLogger('{{cookiecutter.project_name}}')
    return logger


if __name__ == '__main__':
    print(parser().getboolean('stream_config', 'batch_status'))
