#!/bin/bash
#
# Stop the Splunk container
#


# Errors are fatal
set -e

echo "# "
echo "# Stopping Splunk"
echo "# "
docker kill splunk-telegram || true


