import requests
from bs4 import BeautifulSoup
import os

m=input('enter movie : ')

os.mkdir(m)
os.chdir(m)

url='https://masstamilan.in/{}/'.format(m)

r=requests.get(url).content
soup= BeautifulSoup(r,'lxml')

songs_name = []
for i in soup.find_all('h2',{'class':'nostyle'}):
	print(i.find('span').text)
	songs_name.append(str(i.find('span').text).strip())
	
song_link = []
for s in soup.find_all('a',{'title':'Download Idhu Varai Naan 320kbps'}):
	song_link.append(s.get('href'))

songs = dict(zip(songs_name,song_link))

q = int(input('1 : One Song, 2: All Songs : '))

def single_song(k):	
	
	name = songs[k].split('/')[-1]

	r = requests.get(songs[k]).content

	file=open(name, 'wb')
	file.write(r)
	print('Downloded :',name)
		 
def all_song():
	for f in song_link:
		name1 = f.split('/')[-1]
		e = requests.get(f).content

		file1=open(name1,'wb')
		file1.write(e)
		print('Downloded :',name1)

if q == 1:
	single_song(input('enter song name: '))
else:
	all_song()