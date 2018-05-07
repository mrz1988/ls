class GitOutput:
    def __init__(self, output):
        self.branch = None
        self.parse(output)

    def parse_branch(self, lines):
        for line in lines:
            if line.startswith('On branch'):
                self.branch = line.split('On branch ')[1]

    def parse(self, output):
        if 'fatal:' in output:
            self.branch = None
            self.staged_files = []
            self.unstaged_files = []
            self.untracked_files = []

        lines = list(map(lambda l: l.strip(), output.split('\n')))
        self.parse_branch(lines)

        altered_files = {
            'staged': [],
            'unstaged': [],
            'untracked': [],
        }

        file_bucket = None
        for line in lines:
            if line == '':
                continue
            if line.startswith("(use"):
                continue
            if line.startswith("Changes to be committed"):
                file_bucket = 'staged'
                continue
            if line.startswith("Changes not staged"):
                file_bucket = 'unstaged'
                continue
            if line.startswith("Untracked files"):
                file_bucket = 'untracked'
                continue
            if file_bucket is None:
                continue
            
            if ':' in line:
                fpath = line.split(':')[1].strip()
            else:
                fpath = line

            altered_files[file_bucket].append(fpath)

        self.staged_files = altered_files['staged']
        self.unstaged_files = altered_files['unstaged']
        self.untracked_files = altered_files['untracked']
