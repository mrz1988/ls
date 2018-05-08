# Available colors:
# 'white'
# 'red'
# 'yellow'
# 'blue'
# 'cyan'
# 'magenta'
# 'green'
#
# All colors can also be prefixed with 'bright' or 'dark' if your console supports it.
# Ex: 'bright green'
#
# If your console supports background colors as well, you can add a background color like:
# 'blue on white'
#
# To experiment:
# >>> from lilies import grow
# >>> grow('Hello!', 'blue on white')
# >>> c'Hello!'
# (The above text should appear the color you selected.)

force_tty_width = None # a char width or None for auto-sensing

default_color = 'white'
staged_color = 'green'
unstaged_color = 'red'
untracked_color = 'blue on white'
dir_color = 'yellow'
link_color = 'magenta'
show_branch = True
