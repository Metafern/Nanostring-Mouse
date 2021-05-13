import requests
url = 'https://www.nanostring.com/blog/of-mice-and-men-the-importance-of-mouse-models-in-research/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)

webpage = result.content.decode()

print(webpage)

if(webpage.find("<i class=\"mouse-month-mouse\"") != -1):
	print("FOUND!")
