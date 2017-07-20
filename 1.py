import sqlite3,os
from collections import OrderedDict
import pylab as plt

history_db = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\\User Data\Default\History" #path to user's history database (Chrome)

#db querying
c = sqlite3.connect(history_db)
cursor = c.cursor()
select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
cursor.execute(select_statement)

results = cursor.fetchall()[::-1] #reverse
sites_count = {} #dict

for url, count in results:
        a=url.split('//')
        b=a[1].split('/', 1)
        url = b[0].replace("www.", "")
        if url in sites_count:
                sites_count[url] += 1
        else:
                sites_count[url] = 1

sites = OrderedDict(sites_count)
index = [1,3,5]
count = list(sites.values())[:3]
LABELS = list(sites.items())[:3]

plt.bar(index, count, align='center')
plt.xticks(index, LABELS)
plt.show()
