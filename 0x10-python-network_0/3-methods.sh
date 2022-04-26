#!/bin/bash
# script that takes in a URL, sends a request to that URL.
curl -is $1 | grep Allow: | cut -d' ' -f2-
