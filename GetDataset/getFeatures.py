import csv
import urllib.request
import imgkit
import wikipedia
import pickle
import os.path
import signal
from Utils.Constants import Constants

const=Constants()
OUT_DIR_IMG  = const.rootDir+const.imagesDir
OUT_DIR_WIKI = const.rootDir+const.wikiDir
OUT_DIR_HTML = const.rootDir+const.htmlDir
wikipedia.set_lang("en")

file = open('top-1m.csv', 'r')
reader = csv.reader(file)

def handler(signum, frame):
	print("timeout!")
	raise Exception("end of time")

signal.signal(signal.SIGALRM, handler)
skip = int(input('how many to skip? '))
index=0
for row in reader:
	index+=1
	if index<=skip:
		continue
	print("processing website #"+str(index))
	rank=row[0]
	url=row[1]

	# set timeout for fetching html
	signal.alarm(20)

	# get the html
	fname = OUT_DIR_HTML+str(index)+'.html'
	if not os.path.isfile(fname):
		try:
			with open(fname, "w") as text_file:
				text_file.write(urllib.request.urlopen('http://python.org/').read().decode("utf-8"))
		except Exception as e:
			print("Haha .. error with html of "+str(index)+": "+str(e) )


	# set timeout for fetching image
	signal.alarm(20)

	# get screenshot from the website
	fname = OUT_DIR_IMG+str(index)+'.jpg'
	if not os.path.isfile(fname):
		try:
			imgkit.from_url(url, fname)
		except Exception as e:
			print("Haha .. error with image of "+str(index)+": "+str(e)	)


	# set timeout for fetching the wiki
	signal.alarm(20)

	# get the wiki page about the website
	fname = OUT_DIR_WIKI+str(index)+'.pkl'
	if not os.path.isfile(fname):
		try:
			wiki_page=wikipedia.page(url)
			pickle.dump(wikipedia.page(url), open(fname, 'wb'))
		except Exception as e:
			print("Haha .. error with wiki of "+str(index)+": "+str(e) )

	signal.alarm(0)



file.close()