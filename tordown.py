import urllib2
import os
import feedparser
import re
import sys

UID = 'xxxx'
PASS = 'yyyyyyyyyyyy'

if (len(sys.argv) != 3):
	print "To few arguments, should be tordown.py path/to/save/file 'link_to_rssfeed'"
	sys.exit(1)

rss_feed = sys.argv[2]

save_file = sys.argv[1]

d = feedparser.parse(rss_feed)

regfile = open('regex', 'r').read().splitlines()
	

def downloadshow(wantedShow):

	for torr in d.entries:
		rssTitle = torr.title

		fileSize = torr.description.split(" ")[3]
		MBorGB = torr.description.split(" ")[4]
		getit = True

		if MBorGB == "GB":
			if (float(fileSize) < 1.8):
				getit = True
			else:
				getit = False
		elif MBorGB == "MB":
			getit = True

		matchObj = re.search( wantedShow, rssTitle, re.IGNORECASE) 

		if matchObj:
			#check log file, if not found add to log file and download file
			if (checklog(rssTitle)):
				#dont download

				continue
			elif getit:
				#download

				theLink = torr.link
				fileName = torr.link.replace(' ','%20').split('?')[0]
				fileName = fileName.split('/')

				try:
					opener = urllib2.build_opener()
					opener.addheaders.append(('Cookie', 'uid=' + UID + ';pass=' + PASS + ''))
					f = opener.open(theLink.replace(' ','%20').encode('utf-8'))

					try:
						with open(save_file + '/' + fileName[-1], "wb") as local_file:
							local_file.write(f.read())
					except:
						print "Failed to save file"
				except Exception:
					print "Failed to download"



def checklog(rssTitle):

	if rssTitle.encode('utf-8') in open('torr.log').read():
    		return True
    	else:
    		open('torr.log', 'a').write(rssTitle.encode('utf-8') + '\n')
    		return False
			

for wantedShow in regfile:
	downloadshow(wantedShow)	
	





