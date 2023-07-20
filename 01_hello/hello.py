#!/usr/bin/env python3
'''
Author: Luyao M
Purpose: Say hello
'''

import argparse
# ----------------------------------------------
def get_args():
    '''Get the command-line arguments'''
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()
# note: be careful about the [space].
# I was failed to pass the test just because the output is 'Hello,World!', missed the space

# ----------------------------------------------
def main():
    '''make a k-pop noise there'''
    args = get_args()
    print('Hello, ' + args.name + '!')

# ----------------------------------------------     
if __name__ == '__main__':
    main()
