# pylint: disable=missing-module-docstring

import os
import re
from distutils.command.install import INSTALL_SCHEMES
from setuptools import setup, find_packages
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

version_re = re.compile("""__version__[\\s]+=[\\s]*['|"](.*)['|"]""")

with open('calc.py', 'r', encoding="utf-8") as f:
    content = f.read()
    match = version_re.search(content)
    version = match.group(1)


def read(filename):
    """ Read readme contents """
    return open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8").read()


long_description = read('README.md')

setup(
    name='calc',
    incude_package_data=True,
    version=version,
    description=('calc: a simple py3 script to perform arithmetic operations'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/psadi/calc/',
    author='P S, Adithya',
    author_email='adithya3494@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Terminals',
    ],
    py_modules=['calc', ],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['calc=calc:main']
    }
)
