
import requests

all ='''/events/COMBINE_2019/abstracts
node/260
/events/COMBINE_2019/agenda'''

all = '''standards
events'''

for l in all.split('\n'):
    print('Getting %s'%l)
    fname = '%s.html'%l
    url = 'http://co.mbine.org/' + l
    r = requests.get(url)
    open(fname , 'wb').write(r.content)
