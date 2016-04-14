#!/usr/bin/env python

from setuptools import setup

setup(
    name='some_cool_facts',
    version='0.0.1',
    description='some cool facts',
    url='https://github.com/tpinecone/some_cool_facts',
    author='pinecone',
    author_email='teriankoscik@gmail.com',
    license='GPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'Topic :: Artistic Software',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    ],
    keywords='bots',
    packages=['somecoolfacts'],
    install_requires = ['tweepy==3.4.0', 'nltk==3.0.0', 'requests==2.9.1'],
    entry_points = {
          'console_scripts': [
              'somecoolfacts  = somecoolfacts.__init__:main'
          ]
    },
)
