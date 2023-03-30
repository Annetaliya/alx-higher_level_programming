#!/usr/bin/bash
#A script that shows the size in bites of a url body
curl -so /dev/null -w '%{size_download}\n' "$1"
