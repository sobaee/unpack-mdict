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
src=""
read -p "Input file (ex. dictionary.mdx): " src

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

echo 'All done!'