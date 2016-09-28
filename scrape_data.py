from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response)

csv_file = open("email_list.csv", "w")

print soup.html.head.title.string

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        name = person_soup.find("div", attrs={"class": "row"}).find("h1").string
        email = person_soup.find("span", attrs={"class": "email"}).string
        city = person_soup.find(text="City: ").findNext("span").string
        csv_file.write(name + "," + email + "," + city + "\n")
        print name + "," + email + "," + city + "\n"

csv_file.close()
# Scrape_data
