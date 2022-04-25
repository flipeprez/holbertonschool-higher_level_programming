#!/bin/bash
# script that takes in a URL, sends a request to that URL.
curl -s -H -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
