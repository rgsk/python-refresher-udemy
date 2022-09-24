from .operations import operator

'''
path for .operations is resolved by following below process -
libs.mylib
the current file name is dropped
so it becomes 'libs'
then .operations is appended to libs
so import statement becomes ->
from libs.operations import operator
'''

print('mylib.py:', __name__)


def magical_fun():
    print('its magic')
