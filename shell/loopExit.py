#! /user/bin/env python3
import os, sys, time, re


commands = ()
userInput = ''
line = '$'
# line will be the PS1

# from p3-exec.py
pid = os.getpid()


while userInput != 'exit':
    userInput = raw_input(line)
    # raw_input() is used because it is in python 2.7
    if userInput == 'exit':
        line = ''
        continue
        # exit program

    elif userInput == './shell':
    # shell start
        while userInput != 'exit':
            userInput = raw_input(os.environ['PS1'])
            if userInput == 'exit':
                continue
            elif userInput != '':
                
                rc = os.fork()

                if rc < 0:
                    os.write(2, ("fork failed, returning %d\n" % rc).encode())
                    sys.exit(1)

                elif rc == 0:                   # child
                    args = userInput.split()
                    for dir in re.split(":", os.environ['PATH']): # try each directory in the path
                        program = "%s/%s" % (dir, args[0])
                        try:
                            os.execve(program, args, os.environ) # try to exec program
                        except EnvironmentError as e:             # ...expected
                            pass                              # ...fail quietly

                    os.write(2, ("Child:    Could not exec %s\n" % args[0]).encode())
                    sys.exit(1)                 # terminate with error

                else:                           # parent (forked ok)
                                 (pid, rc)).encode())
                    childPidCode = os.wait()
                    os.write(1, ("Parent: Child %d terminated with exit code %d\n" % 
                                 childPidCode).encode())
            else:
                continue

    else:
        continue
        # end of the WHOLE SHELL


