
import requests
import os


all ='''/events/COMBINE_2019/abstracts
node/260
/events/COMBINE_2019/agenda'''

all = '''standards
events
/events/COMBINE_2019/agenda'''

for l in all.split('\n'):
    parts = l.strip('/').split('/')
    print('- Handling %s (%s)'%(l,parts))
    if len(parts)==1:
        name = parts[0]
        dir = '.'
    else:
        name = parts[-1]
        if len(parts)>=2:
            dir = parts[0]
            if not os.path.exists(dir):
                print("   Creating: %s"%dir)
                os.makedirs(dir)
        if len(parts)>=3:
            dir = '%s/%s'%(parts[0],parts[1])
            if not os.path.exists(dir):
                os.makedirs(dir)

    fname = '%s.html'%name
    url = 'http://co.mbine.org/' + l
    r = requests.get(url)
    tgt = '%s/%s'%(dir, fname)
    print("     Copying %s to %s" %(url, tgt))
    open(tgt , 'wb').write(r.content)
