from libqtile import hook, command
from config import wallpaper_cmd, groups
import pprint


@hook.subscribe.client_new
def firefox_flash(window):
    if(window.name == "plugin-container"):
        window.floating = True


@hook.subscribe.client_new
def cairo_dock(window):
    if(window.name == "switcher"):
        window.floating = True


@hook.subscribe.client_new
def transient(window):
    if(window.window.get_wm_transient_for()):
        window.floating = True


from cffi import FFI
ffi = FFI()
ffi.cdef("""
typedef int pid_t;
#define PR_SET_CHILD_SUBREAPER ...
#define WNOHANG ...
int prctl(int option, unsigned long arg2, unsigned long arg3,
                 unsigned long arg4, unsigned long arg5);
pid_t waitpid(pid_t pid, int *status, int options);
""")
C = ffi.verify("""
    #include <sys/types.h>
    #include <sys/wait.h>
    #include<sys/prctl.h>
""", libraries=[])   # or a list of libraries to link with


@hook.subscribe.startup
def prctl_set_child_subreaper():
    C.prctl(C.PR_SET_CHILD_SUBREAPER, 1, 0, 0, 0)
    C.waitpid(-1, ffi.NULL, C.WNOHANG)
    from threading import Thread
    thread = Thread(target=waitpid_thread)
    thread.daemon = True
    thread.start()
    startup()


def waitpid_thread():
    from time import sleep
    while True:
        if C.waitpid(-1, ffi.NULL, 0) < 0:
            sleep(1)

import subprocess
import re


def is_running(process):
    s = subprocess.Popen(["ps", "axuw"], stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x):
            return True
    return False


def execute_once(process):
    if not is_running(process):
        return subprocess.Popen(process.split())


def startup():
    execute_once("compton -b")
    execute_once("fcitx")
    execute_once("xbindkeys")
    execute_once("xfce4-panel")
    execute_once(wallpaper_cmd)
