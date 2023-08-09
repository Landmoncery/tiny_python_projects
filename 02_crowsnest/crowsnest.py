#!/usr/bin/env python3
"""
Author : sansan <sansan@localhost>
Date   : 2023-06-14
Purpose: Shiver your timbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    if word[0] in ['a', 'e', 'i', 'o', 'u']:
        article = 'an'
    else:
        article = 'a'
    print('Ahoy, Captain, {article} ' + word + ' off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
