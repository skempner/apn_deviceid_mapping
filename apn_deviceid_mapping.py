import csv, re, sys
#deviceMapping = {3:IDFA, 8:AAID, 4:SHA1UDID, 5:MD5UDID}
EXAMPLE_SEGMENT_ID = 55444

#open csv reader
inputfile  = open('Basket_Raw_UpperandLower.csv', "rb")
reader = csv.reader(inputfile, delimiter='\n')



#for each row in csv
for row in reader:
	#check for empty rows
	if row != []:
		#todo make the row uppercase
		deviceID = row[0].upper()
		#check for a match of each type in order of likeliness

		#do a regex match for IDFA
		idfaMatch = re.search('([0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12})', deviceID)
		if idfaMatch:
			print idfaMatch.group(0) + "," + str(EXAMPLE_SEGMENT_ID) + ";" + "^3"

			#given AAID is the same format - if you require this too uncomment the following line to also insert a line for AAID
			# print idfaMatch.group(0) + "," + str(EXAMPLE_SEGMENT_ID) + ";" + "^8"
			
			continue


		#do a regex match for SHA1UDID
		sha1Match = re.search('([0-9A-F]{40})', deviceID)
		if sha1Match:
			print sha1Match.group(0) + "," + str(EXAMPLE_SEGMENT_ID) + ";" + "^4"
			continue

		#do a regex match for MD5UDID
		md5Match = re.search('([a-fA-F\d]{32})', deviceID)
		if md5Match:
			print md5Match.group(0) + "," + str(EXAMPLE_SEGMENT_ID) + ";" + "^5"
			continue

		#To print out the IDs that do not match uncomment this:
		# else:
		# 	print "no match " + deviceID

inputfile.close()