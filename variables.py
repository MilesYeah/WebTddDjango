import os

VARIABLE_FPN = os.path.abspath(__file__)
PROJECT_BASE, VARIABLE_FN = os.path.split(VARIABLE_FPN)

PATH_PACKAGE = os.path.join(PROJECT_BASE, 'package')
DRIVER_CHROME_FPN = os.path.join(PATH_PACKAGE, "chromedriver.exe")


