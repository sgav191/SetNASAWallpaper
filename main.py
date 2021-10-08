import datetime
import time
import random
import os
import pwd
import requests
print ("Welcome to SetNASAWallpaper, where you can set your wallpaper as a NASA image.")
def GenerateDate():
	start_date = datetime.date(1996, 1, 1)
	end_date = datetime.date.today()
	time_between_dates = end_date - start_date
	days_between_dates = time_between_dates.days
	random_number_of_days = random.randrange(days_between_dates)
	random_date = start_date + datetime.timedelta(days=random_number_of_days)
	return random_date
userimage = input ("""What image would you like to set as your wallpaper?
---------------------------------------------
a) Today's Image
b) A Random Image
c) An image from a specific date

Type your answer here: """)
if userimage == "b":
	date = GenerateDate()
elif userimage == "c":
	date = input ("What is your specific date (YYYY-MM-DD): ")
else:
	date = datetime.date.today()
	
"""Please enter your NASA API Key here,
if you don't have one, you can get one at https://api.nasa.gov
"""
apikey = <API-KEY>
url = f"https://api.nasa.gov/planetary/apod?api_key={apikey}&date={date}"
filename = "YourNASAWallpaper.png"
def GetFileName():
	username = pwd.getpwuid(os.getuid()).pw_name
	directory = "/Users/" + username + "/Downloads/"
	return os.path.join(directory, filename)
def GetImage():
	res = requests.get(url)
	if res.status_code != 200:
		print ("There was an error with the API. Try re-entering your API Key.")
		return
	imageurl = res.json()["url"]
	
	if "jpg" not in imageurl:
		print ("Sorry! There isn't a picture available from NASA at this time. Try again!")
	else:
		image = requests.get(imageurl, allow_redirects=True)
		filename = GetFileName()
		open(filename, 'wb').write(image.content)

GetImage()
filename = GetFileName()
cmd = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" + filename + "\"'"
os.system(cmd)

print ("Your wallpaper is now a NASA Image! To find your Image, go to your Downloads folder and find 'YourNASAWallpaper.png'")