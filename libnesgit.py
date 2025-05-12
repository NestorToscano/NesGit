import argparse # for command line argument parsing
import configparser # for reading configuration files
from datetime import datetime # for date and time manipulation
import grp, pwd # for user and group information
from fnmatch import fnmatch # for filename matching (.gitignore)
import hashlib # Hash functions
from math import ceil # Ceiling function
import os # filesystem routines
import os.path
import re # for regular expressions
import sys # CLI arguments
import zlib # Compressing files

argparse = argparse.ArgumentParser(description="NesGit: My own Git implementation")