#!/usr/bin/env python
import sys
import argparse as apa
import os


class Compressor():
    def __init__(self):
        self._parser = apa.ArgumentParser()
        self.config_parser()

    def config_parser(self):
        self._parser.add_argument('src',
                                  default='./',
                                  help='要解压缩的文件所在目录的路径'
                                  )
        self._parser.add_argument('--expression', '-e',
                                  help='压缩文件文件匹配的表达式', nargs='*'
                                  )

    def parse_args(self):
        if len(sys.argv) == 1:
            sys.argv.append("--help")
        self._args = self._parser.parse_args()
        return self._args

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, value):
        self._args = value

    @property
    def parser(self):
        return self._parser

    @parser.setter
    def parser(self, value):
        self._parser = value


compressor = Compressor()
args = compressor.parse_args()
print("expression : %s , \n src : %s" % (args.expression, args.src))
