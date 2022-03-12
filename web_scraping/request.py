import requests_html

#print(f"requests_html:\n{dir(requests_html)}")
##
session = requests_html.HTMLSession()
res = session.get("https://www.yahoo.com/")
items = res.html.absolute_links
print(items)
e = res.html.find('[data-category="trending news"]')[1].find("span")
for i in e:
      print(i.text)

#print(f"requests_html.HTML:\n{dir(requests_html.HTML)}")
#print(f"requests_html.Element:\n{dir(requests_html.Element)}")