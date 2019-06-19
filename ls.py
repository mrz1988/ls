from __future__ import print_function
import os
from subprocess import Popen, PIPE, STDOUT
from lilies import grow, columnify
from git import GitOutput
import config

def tty_width():
    if not config.force_tty_width is None:
        return config.force_tty_width
    else:
        cwd = os.getcwd()
        _, width = os.popen('stty size', 'r').read().split()
        return int(width)

def dir_color():
    if config.dir_color is None:
        return 'yellow'
    return config.dir_color

def untracked_color():
    if config.untracked_color is None:
        return 'magenta'
    return config.untracked_color

def staged_color():
    if config.staged_color is None:
        return 'green'
    return config.staged_color

def unstaged_color():
    if config.unstaged_color is None:
        return 'red'
    return config.unstaged_color

def file_color():
    if config.default_color is None:
        return 'white'
    return config.default_color

def format_git_output(s):
    print(str(s))
    if ('fatal:' in s):
        print('fatal')
        return
    else:
        print('stuff')

def format_dir(s):
    return grow(s + '/', dir_color())

def format_link(s):
    return grow(s, 'magenta')

def format_file(s, git_output):
    color = file_color()
    if s in git_output.staged_files:
        color = staged_color()
    elif s in git_output.unstaged_files:
        color = unstaged_color()
    elif s in git_output.untracked_files:
        color = untracked_color()
    return grow(s, color)

def printls(git_output):
    entries = os.listdir(os.getcwd())
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
    print(columnify(colored, width=tty_width()))
    return True


if __name__ == '__main__':
    git_output = Popen('git status', shell=True, stdout=PIPE, stderr=STDOUT).stdout
    git_output = str(git_output.read())
    git_output = GitOutput(git_output)
    if config.show_branch:
        print("")
        if git_output.branch is not None:
            print("Currently on branch: '" + grow(git_output.branch, 'green') + "'")
        else:
            print(grow("(Not a git repository)", "blue"))
        print("")
    printls(git_output)
    print("")
