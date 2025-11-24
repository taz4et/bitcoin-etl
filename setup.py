import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
try:
    from bitcoinetl import core
except:
    pass

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


long_description = read('README.md') if os.path.isfile("README.md") else ""

setup(
    name='bitcoin-etl',
    version='1.5.3',
    author='Development Team',
    author_email='dev@blockchain-tools.io',
    description='Tools for exporting Bitcoin blockchain data to JSON',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/crypto-etl/bitcoin-etl',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='bitcoin',
    python_requires='>=3.5.0,<4',
    install_requires=[
        'requests~=2.20',
        'python-dateutil~=2.7',
        'click~=7.0'
    ],
    extras_require={
        'streaming': [
            'timeout-decorator==0.4.1',
            'google-cloud-pubsub==0.39.1'
        ],
        'dev': [
            'pytest~=4.3.0'
        ],
    },
    entry_points={
        'console_scripts': [
            'bitcoinetl=bitcoinetl.cli:cli',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/crypto-etl/bitcoin-etl/issues',
        'Source': 'https://github.com/crypto-etl/bitcoin-etl',
    },
)
