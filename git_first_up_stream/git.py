#!/usr/bin/env python3

# alias init

# cp ./git.py /usr/local/bin/init

import subprocess
import sys

if __name__ == '__main__':
    remote_repo = 'origin'
    if len(sys.argv) >= 2:
        remote_repo = sys.argv[1]
    output = subprocess.getoutput("git status | grep branch | head -n 1 | awk '{print $3}'")
    shell = 'git push --set-upstream ' + remote_repo + ' ' + output
    print("generate shell script: ", shell)
    subprocess.call(shell, shell=True)
