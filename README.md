# unpack-mdict
This is a bash script to automatically extract or unpack the MDICT MDX (with MDD resources if available) using mdict-utils python tool, which can be installed with: pip3 install mdict-utils

N.B: MDX file will be extracted to octopus source format .mtxt file, and MDD will be extracted to a folder with a name of the dictionary and ended with ".cache_res"

USAGE:

Navigate to the directory that contains this bash file and the files MDX or MDD or both, and run this command: bash unpack-mdict.sh dictname.mdx (or dictname.mdd)
