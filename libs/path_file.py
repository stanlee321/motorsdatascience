# GET FILES LOCATION
import os

cwd = os.getcwd()           # Original Path to libs
original_path = cwd


def get_path_to_files():
    return (os.chdir(original_path))

get_path_to_files()