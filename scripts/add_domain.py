#!/usr/bin/env python2
#
# Copyright 2018 The Recruiter Block List Project
#

import sys
import argparse


blockListFileName = '../recruiter_block_list.txt'

class AddDomain:

    def __init__(self, newDomain):
        
        # Clean.
        newDomainClean = newDomain[0].strip()
        if (newDomainClean == ''):
            print("New domain cannot be empty! Exiting!")
            sys.exit(0)
        
        # Read list of domains.
        listOfDomains = []
        print "Opening file ", blockListFileName, " ..."
        fObj = open(blockListFileName, "r")
        line = fObj.readline().strip()
        while line != "":
            # Check if the new domain matches and existing domain.
            if line == newDomainClean:
                print("New domain is already in the list! Exiting!")
                fObj.close()
                sys.exit(0)
            else:
                # Check if this is a unique domain.
                uniqueDomain = True
                for i in range(0, len(listOfDomains)):
                    if (line == listOfDomains[i]):
                        uniqueDomain = False
                if (uniqueDomain == True):
                    listOfDomains.append(line)
                    #print line
            # Get the next line.
            line = fObj.readline().strip()
        
        fObj.close()
        
        # Append the new domain.
        print "Appending new domain ", newDomainClean, " to list of recruiter block list..."
        listOfDomains.append(newDomainClean)
        
        # Sort and make unique
        print "Sorting list of recruiter domains..."
        listOfDomains.sort()
        
        fObj = open(blockListFileName, "w")
        print "Writing recruiter domains..."
        for i in range(0, len(listOfDomains)):
            fObj.write(listOfDomains[i] + '\n')
        fObj.close()
        print "Done! New domain successfully added!"
        print "You may now commit and push your changes!"

def main(args):

    if args.version:
        print_debug("Add Domain v0.1\n"
                "Add a recruiter domain to the recruiter block list, make sure it is unique and sort it\n"
                "https://github.com/\n")
        sys.exit(0)
        
    try:
        AddDomain(args.newDomain)
        
    except (KeyboardInterrupt, SystemExit):
        print("\nScript stopped.\n")
        #raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add Domain to Recruiter Block List')

    parser.add_argument('-v', '--version', dest='version', nargs='?', const=True, help='Show Add Domain script version.')

    parser.add_argument('newDomain', type=str, nargs=1, help='The new recruiter domain to add to the Recruiter Block List.')


    args = parser.parse_args()
    main(args)
