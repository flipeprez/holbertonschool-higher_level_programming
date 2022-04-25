#!/bin/bash
# script that takes in a URL, sends a request to that URL.
curl -H "X-School-User-Id: 98" -s "$1"
