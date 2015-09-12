import urllib

def read_text():
	# print "thyis"
	quotes = open("movies_quotes.txt")
	# print "that"
	contents_of_file = quotes.read()
	print contents_of_file
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=shot" + text_to_check)
	output = connection.read()
	print output
	connection.close()

read_text()

