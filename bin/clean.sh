#!/bin/bash
#
# Stop the Splunk container and clean up after it
#


# Errors are fatal
set -e

pushd $(dirname $0)/..

./bin/stop.sh 

echo "# "
echo "# Removing Splunk data..."
echo "# "
rm -rfv splunk-data/
mkdir logs/
touch logs/empty

