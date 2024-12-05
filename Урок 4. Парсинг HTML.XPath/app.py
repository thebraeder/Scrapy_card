from lxml import etree


tree = etree.parse("Урок 4. Парсинг HTML.XPath/web_page.html")

html = tree.getroot()

title_element = html.cssselect("p")
print(title_element[0].text)













# list_items = tree.xpath("//ul/descendant::li")
# for li in list_items:
#     text = ''.join(map(str.strip, li.xpath(".//text()")))
#     print(text)









# title_element = tree.xpath("//body/p/text()")[0]
# print(title_element)












# --------------------------------
# title_elemetn = tree.find("body/ul")
# list_item = tree.findall("body/ul/li")

# for li in list_item:
#     a = li.find("a")

#     if a is not None:
#         print(f"{li.text.strip()}{a.text}")
#     else:
#         print(li.text)