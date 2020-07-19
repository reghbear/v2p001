import os,sys,glob
from git import *

py_path=os.getcwd()
print(py_path)

local_path = os.path.join('code', 'codetest')
print(local_path)

repo=Repo(py_path)

