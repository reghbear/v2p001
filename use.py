import os,sys,glob
from git import *

py_path=os.getcwd()
print(py_path)

repo=Repo(py_path)

repo.git.status()
repo.git.add('.')
repo.git.commit()
repo.git.status()
repo.git.push()


