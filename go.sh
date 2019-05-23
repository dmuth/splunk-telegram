#!/bin/bash
#
# Start up Splunk to ingest data
#

# Errors are fatal
set -e

pushd $(dirname $0) > /dev/null

DOCKER_NAME=splunk-telegram bash <(curl -s https://raw.githubusercontent.com/dmuth/splunk-lab/master/go.sh)



