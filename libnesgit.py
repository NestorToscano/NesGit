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

# https://docs.python.org/3/library/argparse.html

# CL argument parsing
argparser = argparse.ArgumentParser(description="NesGit: My own Git implementation")

argsubparsers = argparser.add_subparsers(dest="Commands", help="subcommand")
argsubparsers.required = True

def main(argv=sys.argv[1:]): # argv is a list of command line arguments
    args = argparser.parse_args(argv) 
    match args.subcommand:
        case "add"          : cmd_add(args)
        case "cat-file"     : cmd_cat_file(args)
        case "check-ignore" : cmd_check_ignore(args)
        case "checkout"     : cmd_checkout(args)
        case "commit"       : cmd_commit(args)
        case "hash-object"  : cmd_hash_object(args)
        case "init"         : cmd_init(args)
        case "log"          : cmd_log(args)
        case "ls-files"     : cmd_ls_files(args)
        case "ls-tree"      : cmd_ls_tree(args)
        case "rev-parse"    : cmd_rev_parse(args)
        case "rm"           : cmd_rm(args)
        case "show-ref"     : cmd_show_ref(args)
        case "status"       : cmd_status(args)
        case "tag"          : cmd_tag(args)
        case _              : print("Unknown command")

# Initializing Repositories
class GitRepository : 
    """A Git repository."""

    working_dir = None
    git_dir = None
    config = None

    def __init__(self, path, force=False) : # Extra argument to force the creation of a new repository
        self.working_dir = path
        self.git_dir = os.path.join(path, ".git") # git directory

        if not (force or os.path.isdir(self.git_dir)) :
            raise Exception(f"Invalid repository path: {path}")
        
        self.config = configparser.ConfigParser()
        config_file = repo_file(self, "config") # TBD / create config file function
