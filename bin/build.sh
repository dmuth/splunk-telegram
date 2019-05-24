#!/bin/bash
#
# Build our containers
#

# Errors are fatal
set -e

#
# Change to the parent of this script
#
pushd $(dirname $0) > /dev/null
cd ..

echo "# "
echo "# Building Docker containers..."
echo "# "
docker build . -f Dockerfile-python -t splunk-telegram-python
docker build . -f Dockerfile-splunk -t splunk-telegram

echo "# "
echo "# Tagging container..."
echo "# "
docker tag splunk-telegram-python dmuth1/splunk-telegram-python
docker tag splunk-telegram dmuth1/splunk-telegram

echo "# Done!"

