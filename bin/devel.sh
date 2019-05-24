#!/bin/bash

# Errors are fatal
set -e

if test "$1" == "python"
then
	DEVEL="python"

elif test "$1" == "splunk"
then
	DEVEL="splunk"

else
	echo "! "
	echo "! Syntax: $0 ( python | splunk )"
	echo "! "
	echo "! python - Spin up Python container in devel mode"
	echo "! splunk - Spin up Splunk container in devel mode"
	echo "! "
	exit 1

fi


#
# Change to the parent of this script
#
pushd $(dirname $0) > /dev/null
cd ..

./bin/build.sh

if test "$DEVEL" == "python"
then
	./1-telegram-html-to-json.sh --devel

elif test "$DEVEL" == "splunk"
then
	./2-start-splunk.sh --devel

fi

