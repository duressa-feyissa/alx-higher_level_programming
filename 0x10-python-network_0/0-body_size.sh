#!/bin/bash
# Takes in a URL, sends a request to that URL
curl -sI "$1" | grep -h 'Content-Length:' | cut -d ' ' -f2
