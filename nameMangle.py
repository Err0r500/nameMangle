#!/usr/bin/python
# Created by: Nick Sanzotta/@beamer
# Script Version: nameMangle.py v1.0
import os, sys, getopt, time
from sys import argv

timestr = time.strftime("%Y%m%d-%H%M")
curr_time = time.time()

class colors:
   white = "\033[1;37m"
   normal = "\033[0;00m"
   red = "\033[1;31m"
   blue = "\033[1;34m"
   green = "\033[1;32m"

banner = '\n '  + colors.normal + '\n# Created by: Nick Sanzotta/@beamr' \
+ colors.normal + '\n# Description: Mangles usernames into common naming conventions ' + '\n' \
+ colors.green + '\n nameMangle v1.0' + '\n' + colors.normal

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def nameMangle(inputFile, mangle, domain):
    print("\n")

    for x in open(inputFile, 'r'):
        full_name = ''.join([c for c in x if  c == " " or  c.isalpha()])
        full_name = full_name.lower().split()
        first_name = full_name[0]
        last_name = full_name[-1]

        if mangle == 1:
            newname=first_name + last_name
            if domain != '':
                newname = newname+"@"+domain
                write(inputFile, mangle, newname)
                print(newname)
            else:
                write(inputFile, mangle, newname)
                print(newname)
        elif mangle == 2: 
            newname = last_name + first_name
            if domain != '':
                newname = newname+"@"+domain
                write(inputFile, mangle, newname)
                print(newname)
            else:
                write(inputFile, mangle, newname)
                print(newname)
        elif mangle == 3:
            newname = first_name + "." + last_name
            if domain != '':
                newname = newname+"@"+domain
                write(inputFile, mangle, newname)
                print(newname)
            else:
                write(inputFile, mangle, newname)
                print(newname)
        elif mangle == 4:
            newname = last_name + "." + first_name
            if domain != '':
                newname = newname+"@"+domain
                write(inputFile, mangle, newname)
                print(newname)
            else:
                write(inputFile, mangle, newname)
                print(newname)
        elif mangle == 5:
            newname = first_name + "_" + last_name
            if domain != '':
                newname = newname+"@"+domain
                write(inputFile, mangle, newname)
                print(newname)
            else:
                write(inputFile, mangle, newname)
                print(newname)
        elif mangle == 6:
            newname = last_name + "_" + first_name
            if domain != '':
                newname = newname+"@"+domain
                write(inputFile, mangle, newname)
                print(newname)
            else:
                write(inputFile, mangle, newname)
                print(newname)
        elif mangle == 7:
            newname = first_name[0] + last_name
            if domain != '':
                newname = newname+"@"+domain
                write(inputFile, mangle, newname)
                print(newname)
            else:
                write(inputFile, mangle, newname)
                print(newname)
        elif mangle == 8:
            newname = last_name[0] + first_name
            if domain != '':
                newname = newname+"@"+domain
                write(inputFile, mangle, newname)
                print(newname)
            else:
                write(inputFile, mangle, newname)
                print(newname)
        elif mangle == 9:
            newname = first_name + last_name[0]
            if domain != '':
                newname = newname+"@"+domain
                write(inputFile, mangle, newname)
                print(newname)
            else:
                write(inputFile, mangle, newname)
                print(newname)
        elif mangle == 10:
            newname = first_name[0] + "." + last_name
            if domain != '':
              newname = newname+"@"+domain
              write(inputFile, mangle, newname)
              print(newname)
            else:
              write(inputFile, mangle, newname)
              print(newname)
        elif mangle == 11:
            newname = last_name[0] + "." + first_name
            if domain != '':
              newname = newname+"@"+domain
              write(inputFile, mangle, newname)
              print(newname)
            else:
              write(inputFile, mangle, newname)
              print(newname)
        elif mangle == 12:
            newname = last_name[0:3] + first_name[0:2]
            if domain != '':
                newname = newname+"@"+domain
                write(inputFile, mangle, newname)
                print(newname)
            else:
                write(inputFile, mangle, newname)
                print(newname)     
        elif mangle == 13:                               
            newname = last_name[0:4] + first_name[0:3]
            if domain != '':
                newname = newname+"@"+domain
                write(inputFile, mangle, newname)
                print(newname)
            else:
                write(inputFile, mangle, newname)
                print(newname)  
        else:
            sys.exit(2)

def write(inputFile, mangle, newname):
    f1 = "nameMangle-data/"+"format-"+str(mangle)+"_"+timestr+".txt"
    with open(f1, 'a') as f2:
        f2.write(newname+"\n")


def help():
    cls()
    print banner
    print " Usage: ./nameMangle.py <OPTIONS> \n"
    print " Example: ./nameMangle.py -m 7 -d yahoo.com -i /names.txt\n"
    print " Mangled output saved to: nameMangle/nameMangle-data/format[x]_time.txt \n"
    print colors.green + "\n Mangle options:\n" + colors.normal
    print """\t -m <mangle>\t\t  
                                 1)FirstLast        ex:nicksanzotta
                                 2)LastFirst        ex:sanzottanick
                                 3)First.Last       ex:nick.sanzotta
                                 4)Last.First       ex:sanzotta.nick
                                 5)First_Last       ex:nick_sanzotta
                                 6)Last_First       ex:sanzotta_nick
                                 7)FLast            ex:nsanzotta
                                 8)LFirst           ex:snick
                                 9)FirstL           ex:nicks
                                10)F.Last           ex:n.sanzotta
                                11)L.Firstname      ex:s.nick
                                12)FirLa            ex:nicsa
                                13)Lastfir          ex:sanznic  
    """
    print "\t -d <domain>\t\tAppend @domain.com to user list."
    print "\t -i <input>\t\tInput file (Format must be ex: )."
    print colors.green + "\n Misc:\n" + colors.normal
    print "\t -h <help>\t\tPrints this help menu."
    sys.exit(2)

def main(argv):
    if len(argv) < 2:
        help()
    try:
        opts, args = getopt.getopt(argv, 'm:d:i:h',['--mangle=','--domain=','--input=','--help'])
    except getopt.GetoptError:
        help()
        sys.exit(2)
    
    if not os.path.exists("nameMangle-data/"):
        os.mkdir("nameMangle-data/") 
    
    mangle = 7
    domain = ''
    inputFile = ''
    output = 'nameMangle-data/'+timestr+'.txt'

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit(2)
        elif opt in ('-m', '--mangle'):
            mangle = int(arg)
        elif opt in ('-d','--domain'):
            domain = arg
        elif opt in ('-i','--input'):
            inputFile = arg
            nameMangle(inputFile, mangle, domain)
            sys.exit(2)
        else:
            help()
            sys.exit(2)

if __name__ == "__main__":
    main(argv[1:])
