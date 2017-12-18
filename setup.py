#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
"""
打包的用的setup必须引入，
"""
VERSION = '0.1.0'

setup(name='uncompresslogs', version=VERSION, description="解析某个目录下所有的zip文件", long_description='用于日志文件的解压', classifires=[], keywords='twocucao', author_email='394570610@qq.com', url='https://github.com/Neojoke/DecompressFile.git', license='MIT', packages=find_packages(), zip_safe=True, install_requires=['argparse'], entry_points={
    'console_scripts': ['uncompresslogs=uncompresslogs.linetool:main']
},)
