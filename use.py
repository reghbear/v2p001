import os,sys,glob
from git import *

repo=Repo('.')

git=repo.git
git.add ('.')
git.status()
