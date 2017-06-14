# -*- coding :utf-8 -*-

import sys
import socket
import getopt
import threading
import subprocess


# グローバル変数の定義
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


