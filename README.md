# unpack-mdict
This is a bash script (and a similar python script) to automatically extract or unpack the MDICT MDX (with MDD resources if available) using mdict-utils python tool, which can be installed with python-lzo by: `pip3 install mdict-utils python-lzo`.  
You will need to install "which" package either. 

N.B: MDX file will be extracted to octopus mdict source format .mtxt file, while MDD will be extracted to a folder with a name of the dictionary and ended with ".cache_res"

## USAGE:

Navigate to the directory that contains this bash file and copy the files MDX or MDD to the same directory, and run this command: `bash unpack-mdict.sh`
