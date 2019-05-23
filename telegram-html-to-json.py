#!/usr/bin/env python3
# Vim: :set softtabstop=0 noexpandtab tabstop=4
#
# This script reads one or more HTML files that Telegram Desktop creates
# when exporting a chat.  It then outputs JSON which Splunk can read.
#


import argparse
import datetime
import json

from bs4 import BeautifulSoup


#
# Parse our args
#
parser = argparse.ArgumentParser(description = "Convert Telegram HTML to JSON")
parser.add_argument("Files", metavar = "file", type = str, nargs='+',
                    help='an integer for the accumulator')
args = parser.parse_args()


#
# Open a file, read it, and parse its contents.
#
def processFile(file):

	with open(file) as fp:
		soup = BeautifulSoup(fp, "html.parser")

		last_name = "<UNKNOWN>"

		#
		# Note that this does NOT catch forwarded messages.
		# As of this writing, they are a minority.
		#
		for div in soup.findAll("div", {"class": "body"}):

			row = {}

			html = div.findAll("div", {"class": "date"})
			if (len(html)):
				row["date"] = html[0]["title"]

			html = div.findAll("div", {"class": "from_name"})
			if (len(html)):
				row["name"] = html[0].get_text().strip()
				last_name = row["name"]

			else:
				row["name"] = last_name

			html = div.findAll("div", {"class": "text"})
			if (len(html)):
				row["text"] = html[0].get_text().strip()

			html = div.findAll("div", {"class": "media_photo"})
			if (len(html)):
				if not "text" in row:
					row["text"] = ""
				photo = html[0].get_text().strip()
				row["text"] = "(Telegram Photo: {}) {}".format(photo, row["text"])

			if "text" not in row:
				continue

			if "date" not in row:
				continue

			row["date"] = datetime.datetime.strptime(row["date"], 
				"%d.%m.%Y %H:%M:%S").strftime("%Y-%m-%dT%T.000")

			print(json.dumps(row))



#
# Our main entry point
#
def main(args):

	for file in args.Files:
		data = processFile(file)


main(args)


