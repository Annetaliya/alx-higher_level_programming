#!/bin/bash
#A script that shows the size in bites of a url body
curl -s "$1" | wc -c
