#!/bin/bash

# Errors are fatal
set -e 

echo "# "
echo "# Stopping Docker container..."
echo "# "

docker kill splunk-telegram

echo "# "
echo "# Done!"
echo "# "

