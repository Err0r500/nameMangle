#!/usr/bin/python
# Description: Mangles usernames into common naming conventions
# Created by: Nick Sanzotta/@beamer
# Script Version: nameMangle.py v1.0
import os, sys, getopt, time
from sys import argv


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

def mangler(inputFile):
    commonSeparators = ['', '.', '-', '_']

    for x in open(inputFile, 'r'):
        combinationsArray = []
        full_name = ''.join([c for c in x if  c == " " or  c.isalpha()])
        full_name = full_name.lower().split()
        modifiedArray = modifier(full_name)

        for modFullName in modifiedArray:
            for separator in commonSeparators:
                combinationsArray.append(modFullName[0] + separator + modFullName[1])
                combinationsArray.append(modFullName[1] + separator + modFullName[0])

        appendToFile(combinationsArray, full_name[0] + full_name[1])

def modifier(n):
    modifiedArray = []

    modifiedArray.append([n[0][0], n[1][0]])
    modifiedArray.append([n[0][0], n[1][0].upper()])
    modifiedArray.append([n[0][0].upper(), n[1][0]])
    modifiedArray.append([n[0][0].upper(), n[1][0].upper()])



    modifiedArray.append([n[0][0], n[1]])
    modifiedArray.append([n[0][0], n[1].upper()])
    modifiedArray.append([n[0][0], n[1][0].upper() + n[1][1:]])

    modifiedArray.append([n[0][0].upper(), n[1]])
    modifiedArray.append([n[0][0].upper(), n[1].upper()])
    modifiedArray.append([n[0][0].upper(), n[1][0].upper() + n[1][1:]])

    modifiedArray.append([n[0], n[1][0]])
    modifiedArray.append([n[0].upper(), n[1][0]])
    modifiedArray.append([n[0][0].upper() + n[0][1:], n[1][0]])

    modifiedArray.append([n[0], n[1][0].upper()])
    modifiedArray.append([n[0].upper(), n[1][0].upper()])
    modifiedArray.append([n[0][0].upper() + n[0][1:], n[1][0].upper()])



    modifiedArray.append([n[0], n[1]])
    modifiedArray.append([n[0], n[1].upper()])
    modifiedArray.append([n[0], n[1][0].upper() + n[1][1:]])

    modifiedArray.append([n[0].upper(), n[1]])
    modifiedArray.append([n[0][0].upper() + n[0][1:], n[1]])

    modifiedArray.append([n[0][0].upper() + n[0][1:], n[1][0].upper() + n[1][1:]])
    modifiedArray.append([n[0].upper(), n[1].upper()])

    return modifiedArray


def appendToFile(combinationArray, fileName):
    f1 = "nameMangle-data/"+"format-"+fileName + '-' + time.strftime("%Y%m%d-%H%M")+".txt"
    with open(f1, 'a') as f2:
        f2.write("\n".join(combinationArray))

def help():
    cls()
    print banner
    print " Usage: ./nameMangle.py <OPTIONS> \n"
    print " Example: ./nameMangle.py -m 7 -d yahoo.com -i /names.txt\n"
    print " Mangled output saved to: nameMangle/nameMangle-data/format[x]_time.txt \n"
    print colors.green + "\n Mangle options:\n" + colors.normal
    print "\t -i <input>\t\tInput file (Format must be ex: )."
    print colors.green + "\n Misc:\n" + colors.normal
    print "\t -h <help>\t\tPrints this help menu."
    sys.exit(2)

def main(argv):
    if len(argv) < 1:
        help()
    try:
        opts, args = getopt.getopt(argv, 'i:h',['--input=','--help'])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    if not os.path.exists("nameMangle-data/"):
        os.mkdir("nameMangle-data/")

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit(2)
        elif opt in ('-i','--input'):
            inputFile = arg
            mangler(inputFile)
            sys.exit(2)
        else:
            help()
            sys.exit(2)

if __name__ == "__main__":
    main(argv[1:])

