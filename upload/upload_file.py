#!/usr/bin/env python3

import subprocess, sys

token = ""


if __name__ == '__main__':
    token = subprocess.getoutput("cat /Users/winters/config/pic_token")
    if len(sys.argv) != 2:
        exit(1)
    file = sys.argv[1]
    if file.startswith("/"):
         out = subprocess.getoutput("""/usr/bin/base64 {} > /tmp/temp.base64 && /usr/bin/curl -s -X POST -d "@/tmp/temp.base64" -H "Content-Type: application/text" https://api.jonwinters.pw/pic/upload/{}""".format(
            file, token))
         print(out)
         shell ="echo " + out + " | /usr/bin/pbcopy"
         print(shell)
         subprocess.getoutput(shell)

