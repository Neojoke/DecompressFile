#!/usr/bin/env python
import sys
import argparse as apa
import os
import re
import subprocess


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
                                  help='压缩文件文件匹配的表达式', nargs='*',
                                  required=True
                                  )

    def uncompress(self):
        if os.path.isdir(self._args.src):
            pattern = self._args.expression[0]
            try:
                pattern = re.compile(pattern)
            except Exception as exception:
                print('EXPRESSION error: %s' % (exception,))
                return
            if pattern:
                target_filenames = os.listdir(self._args.src)
                for file_name in target_filenames:
                    match_result = pattern.match(file_name)
                    if match_result:
                        file_path = os.path.join(self._args.src, file_name)
                        file_path_changed = file_path + '.zip'
                        subprocess.call(['mv', file_path, file_path_changed])
                        subprocess.call(['unzip', file_path_changed])
                        os.remove(file_path_changed)
                        print('target file path is : %s' % (file_path,))

            else:
                print('expression is not a valid pattern.')
        else:
            print('src is not a valid path.')

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


def main():
    compressor = Compressor()
    args = compressor.parse_args()
    print("expression is : %s , \n src is : %s" % (args.expression, args.src))
    compressor.uncompress()


if __name__ == '__main__':
    print('entry')
    main()
