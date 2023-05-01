#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 30 Apr 2023
@author: ok
'''

from processes.play import Play


def main():
    """ The main runner function for the app"""
    Play(use_default_input=False, output_allowed=True)


if __name__ == "__main__":
    main()
