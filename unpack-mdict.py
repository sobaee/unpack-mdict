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
import re
import readline

history_file = ".script_history.txt"

# Check if history_file exists
if not os.path.isfile(history_file):
    print(f"{history_file} not found. Ignoring on first run.")

# Load previous command history
try:
    readline.read_history_file(history_file)
except FileNotFoundError:
    pass

def check_command(command):
    try:
        subprocess.check_output([command, '--version'], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        return False
    else:
        return True

if check_command('python3'):
        if check_command('mdict'):
            print("All dependencies are ready!\n")
        else:
            print("ERROR: mdict not found! Run 'pip3 install mdict-utils'!")
            exit(1)
else:
    print("ERROR: python not installed! Download and install from https://www.python.org/downloads")
    exit(1)
    
src = input("Input file (ex. dictionary.mdx): ")

if os.path.isfile(f"{os.path.splitext(src)[0]}.mdd"):
    os.system(f"mdict -x {os.path.splitext(src)[0]}.mdd -d ./{os.path.splitext(src)[0]}.cache_res")

if os.path.isfile(f"{os.path.splitext(src)[0]}.mdx"):
    os.system(f"mdict -x {os.path.splitext(src)[0]}.mdx -d ./")
else:
    print('All done!')
    
os.remove(f"{os.path.splitext(src)[0]}.mdx.title.html")
os.remove(f"{os.path.splitext(src)[0]}.mdx.description.html")

if os.path.exists(f"{os.path.splitext(src)[0]}.mtxt"):
    answer = input(f"{os.path.splitext(src)[0]}.mtxt already exists! OVERWRITE? (y/n) ")
    if answer.lower() == 'y':
        os.remove(f"{os.path.splitext(src)[0]}.mtxt")
    else:
        exit(1)

os.rename(f"{os.path.splitext(src)[0]}.mdx.txt", f"{os.path.splitext(src)[0]}.mtxt")

print('All done!')

# Save command history
readline.write_history_file(history_file)