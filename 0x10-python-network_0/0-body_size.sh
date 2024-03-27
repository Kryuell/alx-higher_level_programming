#!/bin/bash

url=$1

# Send a GET request to the URL and extract the body size from the response headers
body_size=$(curl -s -I $url | grep -i "content-length" | awk '{print $2}')

echo $body_size
