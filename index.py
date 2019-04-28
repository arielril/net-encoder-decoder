#!/usr/bin/env python

"""
  ord: string -> int => ord('A') = 65
  format(s, 'b'): (string, int) -> bit (string) => format(65, 'b') = '1000001'
  int(s, 2): (string, 2) -> int => int('1000001', 2) = 65

  Command Examples: 
    - python index.py redudancy -e xxxxx
    - python index.py redudancy -d xxxxx
    - python index.py crc -e xxxxx
    - python index.py crc -d xxxxx
    - python index.py hamming -e xxxxx
    - python index.py hamming -d xxxxx
"""

import argparse as ap

# algorithms files
from algorithms import *

def main():
    parser = ap.ArgumentParser(
        description='Encoder/Decoder for network communication - Block Redundancy/CRC/Hamming Code')

    parser.add_argument('-a', '--algorithm', nargs=1, metavar='algorithm', type=str,
        choices=['redudancy', 'crc', 'hamming'],
        help='Name of the algorithm to be used. Must be "redudancy", "crc" or "hamming"')
    parser.add_argument('-e', '--encode', nargs=1, metavar='ascii_string', type=str, dest='encode',
        help='Encodes an ASCII string and returns the hexadecimal code')
    parser.add_argument('-d', '--decode', nargs=1, metavar='ascii_string', type=str, dest='decode',
        help='Decodes an hexadecimal code and returns the ASCII string')

    args = parser.parse_args()

    # choose algorithm
    if args.algorithm != None and (args.encode != None or args.decode != None):
        algo_name = args.algorithm[0]
        result = 'NO RESULT'
        
        if algo_name == 'redudancy':
            result = redudancy(args)
        elif algo_name == 'crc':
            result = crc(args)
        elif algo_name == 'hamming':
            result = hamming(args)

        print(result)



if __name__ == "__main__":
    main()
