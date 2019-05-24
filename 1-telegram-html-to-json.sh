#!/bin/bash
#
# This script downloads reviews from a specified file and then
# starts up Splunk to ingest them.
#

# Errors are fatal
set -e

DOCKER_IT=""
DOCKER_V=""

DEVEL_PYTHON=""

if test "$1" == "--devel"
then
	DOCKER_IT="-it"
	DOCKER_V="-v $(pwd)/:/app"
	DEVEL_PYTHON="--devel"
fi


DOCKER_V_MNT="-v $(pwd):/mnt"
DOCKER_V_LOGS="-v $(pwd)/logs:/logs"
docker run ${DOCKER_IT} ${DOCKER_V} ${DOCKER_V_LOGS} \
	-v $(pwd):/mnt  dmuth1/splunk-telegram-python ${DEVEL_PYTHON} $@

