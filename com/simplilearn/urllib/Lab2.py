googleSearch = [
	"python image processing",
	"python web scraping",
	"python data analysis",
	"python graphical user interface",
	"python web applications",
	"python ploting",
	"python numerical analysis",
	"python generators",
	"python tutorial"
]
baseurl1="https://www.google.com/search?q="
urls = [ baseurl1 + t.replace(" ", "+") for t in googleSearch ]

for url in urls:
	print(url)