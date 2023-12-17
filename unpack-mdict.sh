#!/bin/bash

# Install dependency with:
# pip3 install mdict-utils
if [[ "x" == "x$1" ]]; then
    printf "\n\nUSAGE: `basename $0` dictionary.dsl\n"
    exit 1
fi

src="$1"

if [ -f "${src%.*}.mdd" ]; then
    mdict -x "${src%.*}.mdd" -d "./${src%.*}.cache_res"
fi

if [ -f "${src%.*}.mdx" ]; then
    mdict -x "${src%.*}.mdx" -d "./${src%.*}.mdx_txt"
else
echo 'All done!'

fi