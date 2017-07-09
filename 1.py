import sqlite3,os,operator
from collections import OrderedDict
import pylab as plt

def parse(url):
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/', 1)
        domain = sublevel_split[0].replace("www.", "")
        return domain

history_db = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\\User Data\Default\History" #path to user's history database (Chrome)

#db querying
c = sqlite3.connect(history_db)
cursor = c.cursor()
select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
cursor.execute(select_statement)

results = cursor.fetchall() #tuple

sites_count = {} #dict

for url, count in results:
        url = parse(url)
        if url in sites_count:
                sites_count[url] += 1
        else:
                sites_count[url] = 1

sites_count_sorted = OrderedDict(sorted(list(sites_count.items()), key=operator.itemgetter(1), reverse=True))

index = [1,3,5]

count = list(sites_count_sorted.values())[:3]

LABELS = list(sites_count_sorted.items())[:3]


plt.bar(index, count, align='center')
plt.xticks(index, LABELS)
plt.show()
