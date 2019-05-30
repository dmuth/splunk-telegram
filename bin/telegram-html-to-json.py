#!/usr/bin/env python3
# Vim: :set softtabstop=0 noexpandtab tabstop=4
#
# This script reads one or more HTML files that Telegram Desktop creates
# when exporting a chat.  It then outputs JSON which Splunk can read.
#


import argparse
import datetime
import json
import logging 


from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
logger = logging.getLogger()

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
		for div2 in soup.findAll("div", {"class": ["message", "default"] }):

			#
			# We're not doing anything with forwarded messages for now,
			# so remove them so they don't get counted.
			#
			for div in div2.findAll("div", {"class": ["forwarded"]}):
				div.decompose()

			# 
			# At this point, we should have one message, so go through it
			# and extract key values.
			#
			for div in div2.findAll("div", {"class": "body"}):

				row = {}

				html = div.findAll("div", {"class": "date"})
				if (len(html)):
					row["date"] = html[0]["title"]

				html = div.findAll("div", {"class": "from_name"})
				if (len(html)):
					row["name"] = html[0].get_text().strip()
					#
					# Wow, really beautifulsoup?  Removing the semi-colon
					# and not touching the rest of the entity?  Ugh.
					# Looks like I'll have to do this by hand.
					#
					row["name"] = row["name"].replace("&apos", "'")
					last_name = row["name"]

				else:
					row["name"] = last_name

				html = div.findAll("div", {"class": "text"})
				if (len(html)):
					row["text"] = html[0].get_text().strip()
					#
					# Bugs in beautifulsoup, take 2.
					#
					row["text"] = row["text"].replace("&apos", "'")

				html = div.findAll("div", {"class": "media_photo"})
				if (len(html)):
					if not "text" in row:
						row["text"] = ""
					photo = html[0].get_text().strip()
					row["text"] = "(Telegram Photo: {}) {}".format(photo, row["text"])

				if "text" not in row:
					#logger.info("No text found in row: {}".format(row))
					continue

				if "date" not in row:
					#logger.info("No date found in row: {}".format(row))
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


