#!/usr/bin/env python
import sys
import argparse as apa
import os
parser = apa.ArgumentParser()


class Compressor():
    def __init__(self):
        self._parser = apa.ArgumentParser()
        self.config_parser()

    def config_parser(self):
        self._parser.add_argument('src',
                                  default='./',
                                  )

    def parse_args(self):
        self._parser.parse_args()

    @property
    def parser(self):
        return self._parser

    @parser.setter
    def parser(self, value):
        self._parser = value


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append("--help")
    parser.add_argument("echo",
                        help='echo the string you user here'
                        )
    parser.add_argument("--verbosity", metavar='1',
                        help='increase output verbosity'
                        )
    args = parser.parse_args()
    print(args.echo)
    if args.verbosity:
        print('verbosity turn on')
