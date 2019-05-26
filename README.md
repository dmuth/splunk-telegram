
# Splunk Telegram

This app lets you run Splunk against messages from Telegram groups and generate
graphs absedon the activity in them.

This app is based on my other app, <a href="https://github.com/dmuth/splunk-lab/">Splunk Lab</a>,
which is a generate Splunk platform build for ingesting data on an ad-hoc basis.
You should check it out!


## Exporting Data From Telegram

Telegram has a blog post which explains how to export data <a href="https://telegram.org/blog/export-and-more">over here</a>.


## Usage




## Licensing

Splunk has its own license.  Please abide by it.

The Docker image ships with the <a href="https://splunkbase.splunk.com/app/4066/">NLP Text Analytics app</a>, which is licensed under <a href="https://github.com/geekusa/nlp-text-analytics/blob/master/LICENSE/LICENSE.txt">the MIT License</a>.


## TODO/Bugs

Only regular messages are supported at this time.  If a photo is found, a note will
be made that it was a photo of a specified size.  No other media types (including stickers)
are supported at this time.


## Contact

My email is doug.muth@gmail.com.  I am also <a href="http://twitter.com/dmuth">@dmuth on Twitter</a> 
and <a href="http://facebook.com/dmuth">Facebook</a>!


