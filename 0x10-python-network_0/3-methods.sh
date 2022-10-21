#!/bin/bash
# Displays all HTTP methods accepted by the server
curl -siLk -X OPTIONS "$1" | grep -oiE 'Allow: .+' | cut -d ' ' -f2-
