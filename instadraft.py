#!/usr/bin/env python
import requests
from lxml import html
from time import strftime

nd = html.fromstring(requests.get('http://nextdraft.com/current').content)
urls = nd.xpath('//div[@class="blurb-content"]/p/a/@href')

l = "foo@bar.baz" # required -- usually your email address
p = "" # optional (most people don't have passwords)

print strftime("%Y-%m-%d %H:%M:%S")+" | Ok "+ l + ", let's do this!"
for u in urls:
    print "Adding "+u+" to Instapaper"
    r = requests.get('https://www.instapaper.com/api/add?username='+l+'&password='+p+'&url='+u)
    print r.content
print strftime("%Y-%m-%d %H:%M:%S")+" | Dunzo."
