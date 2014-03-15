
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


def prctl_set_child_subreaper():
    C.prctl(C.PR_SET_CHILD_SUBREAPER, 1, 0, 0, 0)
    C.waitpid(-1, ffi.NULL, C.WNOHANG)
    from threading import Thread
    thread = Thread(target=waitpid_thread)
    thread.daemon = True
    thread.start()


def waitpid_thread():
    from time import sleep
    while True:
        if C.waitpid(-1, ffi.NULL, 0) < 0:
            sleep(1)

import os
prctl_set_child_subreaper()
os.system("date")
