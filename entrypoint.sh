#!/bin/bash
#
# Entrypoint script--either spawn a shell or run the script.
#


if test "$1"
then

	if test "$1" == "--devel"
	then
		echo "# "
		echo "# Starting container in devel mode and spawning a bash shell..."
		echo "# "
		echo "# (Scripts are in /mnt/bin/)"
		echo "# "
		exec "/bin/bash"

	else 
		#
		# Assume we're downloading a file full of URLs...
		#
		cd /mnt
		exec /app/telegram-html-to-json.py $@

	fi

else
	echo "! "
	echo "! Syntax: $0 ( --devel | file [ file [ file [ ... ] ] ] )"
	echo "! "
	echo "! file - One or more Telegram HTML files to turn into JSON"
	echo "! "
	exit 1

fi


