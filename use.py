import os
from git import Repo
import git

path = 'project_code_path'
repo = Repo(path)

git=repo.git
git.add ('.')
git.status()
