#!/bin/bash
# Takes in a URL, sends a request to that URL
curl -sI "$1" | grep -oiE 'Content-Length: [0-9]+' | cut -d ' ' -f2
