import sys
import os

VARIABLE_FPN = os.path.abspath(__file__)
# PROJECT_BASE, VARIABLE_FN = os.path.split(VARIABLE_FPN)


def get_project_root(fn="root"):
    project_root = None
    path = os.getcwd()
    path, path_sub = os.path.split(path)
    while path_sub:
        folder_list = os.listdir(path)
        if fn in folder_list:
            project_root = path
            break
        path, path_sub = os.path.split(path)
    if not project_root:
        print("Error getting project root path, try to create \"root\" file in project root folder.")
        sys.exit(-1)
    return project_root


PROJECT_BASE = get_project_root(fn='.gitignore')

PATH_PACKAGE = os.path.join(PROJECT_BASE, 'package')
DRIVER_CHROME_FPN = os.path.join(PATH_PACKAGE, "chromedriver.exe")


