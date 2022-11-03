
import requests
import os


# Search for: node/[0-9]+	edit	delete

all = '''/events/COMBINE_2019/abstracts
/events/COMBINE_2019/agenda
/standards/sbml/level-3/version-1/core
about
about_old
andre-testing-html
code-of-conduct
colomoto/old
colomoto/old/meetings
colomoto/old/meetings/2010
colomoto/old/meetings/2012
colomoto/old/meetings/2014
colomoto/old/news
colomoto/old/software
combine2011
combine2011
comm
coordinators
documents
documents/archive
documents/archive_0.1
documents/criteria
events
events/calendar
events/COMBINE
events/COMBINE_2010
events/COMBINE_2011
events/COMBINE_2011/Additional_Notes
events/COMBINE_2011/agenda
events/COMBINE_2011/attendees
events/COMBINE_2011/evo
events/COMBINE_2011/exit-survey
events/COMBINE_2011/participants
events/COMBINE_2011/posters
events/COMBINE_2011/Shuttle_Bus
events/COMBINE_2011/Travel_Information
events/COMBINE_2012
events/COMBINE_2012/agenda
events/COMBINE_2012/attendees
events/COMBINE_2012/Tutorial
events/COMBINE_2012/Tutorial2
events/COMBINE_2012/Tutorials
events/COMBINE_2013
events/COMBINE_2013/abstracts
events/COMBINE_2013/agenda
events/COMBINE_2013/attendees
events/COMBINE_2013/exit-survey
events/COMBINE_2013/full-agenda
events/COMBINE_2014
events/COMBINE_2014/abstracts
specifications/combine_archive-Draft1.pdf
'''




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
    url = 'http://131.215.225.44/' + l
    r = requests.get(url)
    if '.pdf' in url:

        fname = name
        tgt = '%s/%s'%(dir, fname)
        print("     Copying %s to %s" %(url, tgt))
        open(tgt , 'wb').write(r.content)
    else:
        tgt = '%s/%s'%(dir, fname)
        print("     Copying %s to %s" %(url, tgt))
        updated = str.encode(r.content.decode().replace('http://co.mbine','http://old_co.mbine'))
        print(type(updated))
        open(tgt , 'w').write(updated.decode())
