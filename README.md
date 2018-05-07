ls is a python-based command line utility. Add an alias into your .bash_profile to run the script with a more basic command. Feature set isn't very customizable right now since this was a quick bake job, but basic features are:

- Files sorted in alphabetical order
- Folders listed in a separate group
- Folders colored yellow in the terminal
- Untracked git files appear magenta
- Edited git files appear red
- Edited and staged git files appear green
- Committing reverts all colors back to basic white/yellow
- Folders that are not git repositories are labeled as such
- All data is fit to your terminal in neat columns for easy reading

To install:
- Clone lilies (https://github.com/mrz1988/lilies)
- cd into lilies directory
- `python setup.py install`
- Clone ls into a separate folder
- Bind an alias to `python /your_ls_dir/ls.py`
- Reboot your terminal and try it out!
