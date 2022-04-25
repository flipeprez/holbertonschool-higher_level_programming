#!/bin/bash
# script that takes in a URL, sends a request to that URL.
curl -is $1 | grep allow: | cut -d -f2-
