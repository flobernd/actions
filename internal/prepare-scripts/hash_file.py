#!/usr/bin/env python3
# coding: utf8

import argparse
import hashlib
import sys

parser = argparse.ArgumentParser(description='Generates a SHA256 hash over the given file.')

parser.add_argument('filename', type=str, 
                    help='The filename of the file to hash.',)

args = parser.parse_args()

hasher = hashlib.sha256()
with open(args.filename, 'rb') as file:
    for block in iter(lambda: file.read(1024 * 1024), b''):
        hasher.update(block)
result = hasher.digest()

# GitHub `hashFiles()` returns the hash over the hash of all file contents..
print(hashlib.sha256(result).hexdigest())
