#!/bin/bash
# Sends a request to a URL, displays the size of the body of the response
curl -sI "$1" | grep "Content-length:" | cut -d " " -f 2
