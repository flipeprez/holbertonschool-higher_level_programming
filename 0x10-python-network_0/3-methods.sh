#!/bin/bash
# script that takes in a URL, sends a request to that URL.
curl -sI "$1" | greep allow | cut -c 8-
