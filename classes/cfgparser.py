import os
from configparser import SafeConfigParser as CFGParser

ConfigParser = CFGParser(os.environ)
ConfigParser.read(os.environ.get("CONFIG_NAME", "config.ini"))
