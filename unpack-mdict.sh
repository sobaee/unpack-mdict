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
    mdict -x "${src%.*}.mdx" -d ./
else
echo 'All done!'

fi

if [ -e "${src%.*}.mtxt" ]; then
    read -p "${src%.*}.mtxt already exists! OVERWRITE? (y/n) " answer
    if [[ $answer =~ ^[Yy]$ ]]; then
        rm -v "${src%.*}.mtxt"
    else
        exit 1
    fi
fi

mv "${src%.*}.mdx.txt" "${src%.*}.mtxt"
rm -v "${src%.*}.mdx.title.html"
rm -v "${src%.*}.mdx.description.html"
