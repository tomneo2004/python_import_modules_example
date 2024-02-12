import os
import sys
# insert root directory into python module search path
sys.path.insert(1, os.getcwd())

# import module from outside of app folder
import common_modules.utils as common_utils

# import module from inside app folder
import app_modules.utils as app_utils

if __name__ == "__main__":
    common_utils.say_hello()
    app_utils.say_hello()