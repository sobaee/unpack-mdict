# unpack-mdict
This is a bash script to automatically extract or unpack the MDICT MDX (with MDD resources if available) using mdict-utils python tool, which can be installed with: pip3 install mdict-utils.
You may need to install python-lzo either.

N.B: MDX file will be extracted to octopus mdict source format .mtxt file, and MDD will be extracted to a folder with a name of the dictionary and ended with ".cache_res"

USAGE:

Navigate to the directory that contains this bash file and copy the files MDX or MDD to the same directory, and run this command: bash unpack-mdict.sh dictname.mdx (or dictname.mdd)
