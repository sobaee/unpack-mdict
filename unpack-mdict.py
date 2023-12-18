#!/usr/bin/env python3
# 
# Dependencies:
# python3, mdict-utils, which
# 
# Install all dependencies with:
# pip3 install mdict-utils python-lzo
#
# pyglossary better to be installed from a local folder with: python setup.py install (better to use my ready pyglossary zip file)
#
# Import the modules
import os
import sys
import subprocess

def command_exists(command):
    # Check if a command exists in the system
    return subprocess.call(['which', command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

if command_exists('python3'):
    print('Python3 is ready!')
else:
    print("ERROR: python not installed! Download and install from https://www.python.org/downloads")
    sys.exit(1)

if command_exists('mdict'):
    print('Mdict-utils is ready!')
else:
    print("ERROR: mdict not found! Run 'pip3 install mdict-utils'!")
    sys.exit(1)
    
src = input("Input file (ex. dictionary.mdx): ")

if os.path.isfile(f"{os.path.splitext(src)[0]}.mdd"):
    os.system(f"mdict -x {os.path.splitext(src)[0]}.mdd -d ./{os.path.splitext(src)[0]}.cache_res")

if os.path.isfile(f"{os.path.splitext(src)[0]}.mdx"):
    os.system(f"mdict -x {os.path.splitext(src)[0]}.mdx -d ./")
else:
    print('All done!')

if os.path.exists(f"{os.path.splitext(src)[0]}.mtxt"):
    answer = input(f"{os.path.splitext(src)[0]}.mtxt already exists! OVERWRITE? (y/n) ")
    if answer.lower() == 'y':
        os.remove(f"{os.path.splitext(src)[0]}.mtxt")
    else:
        exit(1)

os.rename(f"{os.path.splitext(src)[0]}.mdx.txt", f"{os.path.splitext(src)[0]}.mtxt")

os.remove(f"{os.path.splitext(src)[0]}.mdx.title.html")
os.remove(f"{os.path.splitext(src)[0]}.mdx.description.html")

print('All done!')