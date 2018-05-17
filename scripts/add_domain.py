#!/usr/bin/env python
"""Copyright 2018 The Recruiter Block List Project"""
from __future__ import print_function
import argparse
import sys


block_list_file_name = '../recruiter_block_list.txt'


def add_domain(new_domain):
    with open(block_list_file_name, 'r+') as f:
        all_domains = f.read().splitlines()

        # check for matches
        for domain in all_domains:
            if new_domain == domain:
                sys.exit('New domain is already in the list! Exiting!')

        # add new domain and sort list
        print('Appending new domain {} to list of recruiter block '
              'list...'.format(new_domain))
        print('Sorting list of recruiter domains...')
        all_domains.append(new_domain)
        all_domains.sort()

        # write updated domain list
        f.seek(0)
        f.write('\n'.join(all_domains))
        f.truncate()
        print('Done! New domain successfully added! '
              'You may now commit and push your changes!')
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Add Domain to Recruiter Block List')

    parser.add_argument('--version', '-v',
                        action='store_true',
                        help='Show Add Domain script version.')

    parser.add_argument('newDomain',
                        help='The new recruiter domain to add to the '
                             'Recruiter Block List.')

    args = parser.parse_args()

    if args.version:
        sys.exit("""\
Add Domain v0.1
Add a recruiter domain to the recruiter block list,
make sure it is unique and sort it
https://github.com/""")

    # add the new domain
    add_domain(args.newDomain)
