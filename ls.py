from __future__ import print_function
import os
from subprocess import Popen, PIPE, STDOUT
from lilies import grow, columnify
from git import GitOutput
cwd = os.getcwd()
_, width = os.popen('stty size', 'r').read().split()
width = int(width)

def format_git_output(s):
    print(str(s))
    if ('fatal:' in s):
        print('fatal')
        return
    else:
        print('stuff')

def format_dir(s):
    return grow(s + '/', 'yellow')

def format_link(s):
    return grow(s, 'magenta')

def format_file(s, git_output):
    color = 'white'
    if s in git_output.staged_files:
        color = 'green'
    elif s in git_output.unstaged_files:
        color = 'red'
    elif s in git_output.untracked_files:
        color = 'magenta'
    return grow(s, color)

def printls(git_output):
    entries = os.listdir(cwd)
    if len(entries) == 0:
        print(grow("(This directory is empty)", "magenta"))
        return False
    dirs = filter(os.path.isdir, entries)
    links = filter(os.path.islink, entries)
    files = filter(os.path.isfile, entries)

    dirs = map(format_dir, dirs)
    links = map(format_link, links)
    files = map(lambda f: format_file(f, git_output), files)

    colored = list(dirs) + list(links) + list(files)
    columnify(colored, width=width)
    return True


if __name__ == '__main__':
    git_output = Popen('git status', shell=True, stdout=PIPE, stderr=STDOUT).stdout
    git_output = str(git_output.read())
    git_output = GitOutput(git_output)
    print("")
    if git_output.branch is not None:
        print("Currently on branch: '" + grow(git_output.branch, 'green') + "'")
    else:
        print(grow("(Not a git repository)", "blue"))
    print("")
    printls(git_output)
    print("")
