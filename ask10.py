import urllib
import urllib.request
import re
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup # pip install beautifulsoup4

img_pat = re.compile('<img.*?>',re.I)

def get_info(url):
  tag_counter=0
  try:
      w =  urllib.request.urlopen(url)
  except IOError:
      sys.stderr.write("Couldn't connect to %s " % url)
      sys.exit(1)
  contents =  str(w.read())
  img_num = len(img_pat.findall(contents))
  soup = BeautifulSoup(urllib.request.urlopen(url),features="html.parser")
  for tag in soup.findAll():
      tag_counter+=1
  print("Page Title :" ,soup.title.string)
  print("Number of Page Images :",img_num)
  print("Number of html tags :",tag_counter)
#get_info("https://www.facebook.com/")
