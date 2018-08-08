from bs4 import BeautifulSoup
import urllib.request 
import re
import nltk

#def get_key_words_from (STR)
response = urllib.request.urlopen('https://factba.se/transcript/donald-trump-speech-maga-lewis-center-oh-august-4-2018') 
html = response.read() 
soup = BeautifulSoup(html,"html.parser") 
text = soup.get_text(strip=True) 
tokens = [t for t in re.split(r"[\s\d]",text)]
freq = nltk.FreqDist(tokens)
for key,val in freq.items():
    print (str(key) + ' - ' + str(val) )