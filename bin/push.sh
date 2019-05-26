#!/bin/bash

# Errors are fatal
set -e

#
# Change to the parent of this script
#
pushd $(dirname $0) > /dev/null
cd ..

echo "# "
echo "# Building our images..."
echo "# "
./bin/build.sh

echo "# "
echo "# Pushing containers to Docker Hub..."
echo "# "
docker push dmuth1/splunk-telegram-python
docker push dmuth1/splunk-telegram

echo "# Done!"

