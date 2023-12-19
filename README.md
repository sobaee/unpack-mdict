# unpack-mdict


This is a python script to automatically extract or unpack the MDICT MDX (with MDD resources if available) using mdict-utils python tool.

<br />
## DEPENDENCIES:  

python3, mdict-utils, python-lzo

<br />
<br />
## USAGE:

Navigate to the directory that contains this script and copy the files MDX or MDD to the same directory, and run this command:  `python unpack-mdict.py`

N.B: MDX file will be extracted to octopus mdict source format .mtxt file, while MDD will be extracted to a folder with a name of the dictionary and ended with ".cache_res"
