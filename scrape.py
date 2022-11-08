
import requests
import os


# Search for: node/[0-9]+	edit	delete
# or system.*delete

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
events/COMBINE_2014/agenda
events/COMBINE_2014/attendees
events/COMBINE_2014/exit-survey
events/COMBINE_2015
events/COMBINE_2015/abstracts
events/COMBINE_2015/agenda
events/COMBINE_2015/attendees
events/COMBINE_2016
events/COMBINE_2016/abstracts
events/COMBINE_2016/agenda
events/COMBINE_2016/attendees
events/COMBINE_2017
events/COMBINE_2017/Abstracts
events/COMBINE_2017/Attendees
events/COMBINE_2018
events/COMBINE_2018/abstracts
events/COMBINE_2018/agenda
events/COMBINE_2018/attendees
events/COMBINE_2019
events/COMBINE_2019/abstracts
events/COMBINE_2019/agenda
events/COMBINE_2019/agenda_old
events/COMBINE_2019/attendees
events/COMBINE_2019/CoC
events/COMBINE_2019/COMBINE2019_Travel
events/COMBINE_2019/Posters
events/COMBINE_2019/STANDS4PM
events/COMBINE_2020
events/COMBINE_2021
events/future
events/harmony-2011/attendees
events/harmony-2011/exit-survey
events/harmony-2011/organizers
events/harmony-2011/supplementary-materials
events/harmony-2011/travel-information
events/harmony-2012/organizers
events/HARMONY_2011
events/HARMONY_2012
events/HARMONY_2012/agenda
events/HARMONY_2012/attendees
events/HARMONY_2012/exit-survey
events/HARMONY_2012/poster-list
events/HARMONY_2013
events/HARMONY_2013/attendees
events/HARMONY_2013/organizers
events/HARMONY_2013/travel-options
events/HARMONY_2014
events/HARMONY_2014/presentations
events/HARMONY_2014/travel-options
events/HARMONY_2015
'''

all='''events/HARMONY_2015/Attendees
events/HARMONY_2015/Posters
events/HARMONY_2016
events/HARMONY_2016/Attendees
events/HARMONY_2017
events/HARMONY_2017/agenda
events/HARMONY_2017/Attendees
events/HARMONY_2017/travel
events/HARMONY_2018
events/HARMONY_2018/Attendees
events/HARMONY_2019
events/HARMONY_2019/Activity_suggestions
events/HARMONY_2019/Attendees
events/HARMONY_2019/CoC
events/HARMONY_2019/HARMONY2019_Travel
events/HARMONY_2019/Lightning_talks
events/HARMONY_2019/Location_Information
events/HARMONY_2019/Posters
events/HARMONY_2020
events/HARMONY_2020/Attendees
events/HARMONY_2020/CoC
events/HARMONY_2020/HARMONY2020_Travel
events/HARMONY_2021
events/HARMONY_2021/Attendees
events/ICSB_2013
events/organization
events/tutorial2014
events/tutorial2014/fullagenda
events/tutorial2015
events/tutorial2016
events/tutorial2017
events/tutorial2017/fullagenda
events/tutorial2018
events/tutorial2019
help
help_template1
help_template2
help_template3
home
login
nagios_test_page
specifications.sed-ml.proposal.kisao.RA.version-1
specifications/biopax
specifications/biopax.level-1
specifications/biopax.level-1.pdf
specifications/biopax.level-2
specifications/biopax.level-2.pdf
specifications/biopax.level-3
specifications/biopax.level-3.pdf
specifications/cellml
specifications/cellml.1
specifications/cellml.1.0
specifications/cellml.1.1
specifications/combine_archive-Draft1.pdf
specifications/frog-fva-version-1
specifications/frog-genedeletion-version-1
specifications/frog-json-version-1
specifications/frog-metadata-version-1
specifications/frog-objective-version-1
specifications/frog-reactiondeletion-version-1
specifications/gpml
specifications/neuroml
specifications/omex
specifications/omex-annotation
specifications/omex-annotation/json
specifications/omex-annotation/turtle
specifications/omex-annotation/xml
specifications/omex-archive
specifications/omex-manifest
specifications/omex-metadata
specifications/omex-metadata/1
specifications/omex-metadata/1/0
specifications/omex.RC-1
specifications/omex.RC-2
specifications/omex.version-1
specifications/omex.version-1.pdf
specifications/petab.version-1
specifications/qualifiers
specifications/sbgn
specifications/sbgn.af
specifications/sbgn.af.level-1
specifications/sbgn.af.level-1.version-1
specifications/sbgn.af.level-1.version-1.0
specifications/sbgn.af.level-1.version-1.0.pdf
specifications/sbgn.af.level-1.version-1.2
specifications/sbgn.af.level-1.version-1.2.pdf
specifications/sbgn.er
specifications/sbgn.er.level-1
specifications/sbgn.er.level-1.version-1
specifications/sbgn.er.level-1.version-1.0
specifications/sbgn.er.level-1.version-1.0.pdf
specifications/sbgn.er.level-1.version-1.1
specifications/sbgn.er.level-1.version-1.1.pdf
specifications/sbgn.er.level-1.version-1.2
specifications/sbgn.er.level-1.version-1.2.pdf
specifications/sbgn.er.level-1.version-2
specifications/sbgn.er.level-1.version-2.pdf
specifications/sbgn.pd
specifications/sbgn.pd.level-1
specifications/sbgn.pd.level-1.version-1
specifications/sbgn.pd.level-1.version-1.0
specifications/sbgn.pd.level-1.version-1.0.pdf
specifications/sbgn.pd.level-1.version-1.1
specifications/sbgn.pd.level-1.version-1.1.pdf
specifications/sbgn.pd.level-1.version-1.2
specifications/sbgn.pd.level-1.version-1.2.pdf
specifications/sbgn.pd.level-1.version-1.3
specifications/sbgn.pd.level-1.version-1.3.pdf
specifications/sbgn.pd.level-1.version-2.0
specifications/sbgnml.version-0.3.release-1
specifications/sbgnml.version-0.3.release-1.pdf
specifications/sbml
specifications/sbml-level-3.version-1.core.release-2.pdf
specifications/sbml.level-1
specifications/sbml.level-1.version-1
specifications/sbml.level-1.version-1.pdf
specifications/sbml.level-1.version-2
specifications/sbml.level-1.version-2.pdf
specifications/sbml.level-2
specifications/sbml.level-2.version-1
specifications/sbml.level-2.version-1.pdf
specifications/sbml.level-2.version-2
specifications/sbml.level-2.version-2.pdf
specifications/sbml.level-2.version-3
specifications/sbml.level-2.version-3.release-1.pdf
specifications/sbml.level-2.version-3.release-2
specifications/sbml.level-2.version-3.release-2.pdf
specifications/sbml.level-2.version-4
specifications/sbml.level-2.version-4.release-1
specifications/sbml.level-2.version-4.release-1.pdf
specifications/sbml.level-2.version-5
specifications/sbml.level-2.version-5.RC-1
specifications/sbml.level-2.version-5.RC-1.pdf
specifications/sbml.level-2.version-5.release-1
specifications/sbml.level-2.version-5.release-1.pdf
specifications/sbml.level-3
specifications/sbml.level-3.version-1
specifications/sbml.level-3.version-1.comp
specifications/sbml.level-3.version-1.comp.pdf
specifications/sbml.level-3.version-1.comp.version-1
specifications/sbml.level-3.version-1.comp.version-1.pdf
specifications/sbml.level-3.version-1.comp.version-1.release-1
specifications/sbml.level-3.version-1.comp.version-1.release-1.pdf
specifications/sbml.level-3.version-1.comp.version-1.release-2
specifications/sbml.level-3.version-1.comp.version-1.release-2.pdf
specifications/sbml.level-3.version-1.comp.version-1.release-3
specifications/sbml.level-3.version-1.comp.version-1.release-3.pdf
specifications/sbml.level-3.version-1.core
specifications/sbml.level-3.version-1.core.release-1
specifications/sbml.level-3.version-1.core.release-1.pdf
specifications/sbml.level-3.version-1.core.release-2
specifications/sbml.level-3.version-1.core.release-2.pdf
specifications/sbml.level-3.version-1.core.release-3
specifications/sbml.level-3.version-1.core.release-3.pdf
specifications/sbml.level-3.version-1.distrib
specifications/sbml.level-3.version-1.distrib.version-1
specifications/sbml.level-3.version-1.distrib.version-1.release-1
specifications/sbml.level-3.version-1.distrib.version-1.release-1.pdf
specifications/sbml.level-3.version-1.fbc
specifications/sbml.level-3.version-1.fbc.version-1
specifications/sbml.level-3.version-1.fbc.version-1.release-1
specifications/sbml.level-3.version-1.fbc.version-1.release-1.pdf
specifications/sbml.level-3.version-1.fbc.version-2
specifications/sbml.level-3.version-1.fbc.version-2.release-1
specifications/sbml.level-3.version-1.fbc.version-2.release-1.pdf
specifications/sbml.level-3.version-1.groups
specifications/sbml.level-3.version-1.groups.version-1
specifications/sbml.level-3.version-1.groups.version-1.release-1
specifications/sbml.level-3.version-1.groups.version-1.release-1.pdf
specifications/sbml.level-3.version-1.layout
specifications/sbml.level-3.version-1.layout.version-1
specifications/sbml.level-3.version-1.layout.version-1.release-1
specifications/sbml.level-3.version-1.layout.version-1.release-1.pdf
specifications/sbml.level-3.version-1.multi
specifications/sbml.level-3.version-1.multi.version-1
specifications/sbml.level-3.version-1.multi.version-1.release-1
specifications/sbml.level-3.version-1.multi.version-1.release-1.pdf
specifications/sbml.level-3.version-1.multi.version-1.release-2
specifications/sbml.level-3.version-1.multi.version-1.release-2.pdf
specifications/sbml.level-3.version-1.qual
specifications/sbml.level-3.version-1.qual.version-1
specifications/sbml.level-3.version-1.qual.version-1.release-1
specifications/sbml.level-3.version-1.qual.version-1.release-1.pdf
specifications/sbml.level-3.version-1.render
specifications/sbml.level-3.version-1.render.version-1
specifications/sbml.level-3.version-1.render.version-1.release-1
specifications/sbml.level-3.version-1.render.version-1.release-1.pdf
specifications/sbml.level-3.version-1.spatial
specifications/sbml.level-3.version-1.spatial.version-0.92
specifications/sbml.level-3.version-1.spatial.version-1
specifications/sbml.level-3.version-1.spatial.version-1.release-1
specifications/sbml.level-3.version-2.core
specifications/sbml.level-3.version-2.core.release-1
specifications/sbml.level-3.version-2.core.release-1.pdf
specifications/sbml.level-3.version-2.core.release-2
specifications/sbml.level-3.version-2.core.release-2.pdf
specifications/sbml.level-3.version-2.distrib
specifications/sbml.level-3.version-2.distrib.version-1
specifications/sbml.level-3.version-2.distrib.version-1.release-1	node/279
specifications/sbml.level-3.version-2.distrib.version-1.release-1.pdf
specifications/sbml.level-3.version-2.release-1
specifications/sbml.level-3.version-2.release-2
specifications/sbml.proposal.distrib-annotations.version-1
specifications/sbol
specifications/sbol-visual
specifications/sbol-visual.version-1.0.0
specifications/sbol-visual.version-1.0.0.pdf
specifications/sbol-visual.version-2.0
specifications/sbol-visual.version-2.0.pdf
specifications/sbol.version-1.1.0
specifications/sbol.version-1.1.0.pdf
specifications/sbol.version-2.0.0
specifications/sbol.version-2.0.0.pdf
specifications/sbol.version-2.0.1
specifications/sbol.version-2.0.1.pdf
specifications/sbol.version-2.0.pdf
specifications/sbol.version-2.1.0
specifications/sbol.version-2.1.0.pdf
specifications/sbol.version-2.2.0
specifications/sbol.version-2.2.0.pdf
specifications/sed-ml
specifications/sed-ml.level-1
specifications/sed-ml.level-1.version-1
specifications/sed-ml.level-1.version-1.pdf
specifications/sed-ml.level-1.version-2
specifications/sed-ml.level-1.version-2.pdf
specifications/sed-ml.level-1.version-2.RC
specifications/sed-ml.level-1.version-2.RC.pdf
specifications/sed-ml.level-1.version-2.RC2
specifications/sed-ml.level-1.version-2.RC2.pdf
specifications/sed-ml.level-1.version-3
specifications/sed-ml.level-1.version-3-draft-1
specifications/sed-ml.level-1.version-3-draft-1.pdf
specifications/sed-ml.level-1.version-3.pdf
specifications/sed-ml.level-1.version-4
specifications/sed-ml.proposal.accessing-data.version-1
specifications/sed-ml.proposal.accessing-data.version-1.pdf
specifications/sed-ml.proposal.kisao.RA.version-1
specifications/sed-ml.proposal.kisao.RA.version-1.pdf
specifications/sed-ml.proposal.nested-simulations
specifications/sed-ml.proposal.nested-simulations.FB.version-1
specifications/sed-ml.proposal.nested-simulations.FB.version-1.pdf
specifications/sed-ml.proposal.nested-simulations.FB.version-2
specifications/sed-ml.proposal.nested-simulations.FB.version-2.pdf
specifications/sed-ml.proposal.nested-simulations.FB.version-3
specifications/sed-ml.proposal.nested-simulations.FB.version-3.pdf
specifications/sed-ml/level-1.version-1.pdf
specifications/sed-ml/proposal
specifications/sed-ml/proposal/nested-simulations/FB/version-1
specifications/sed-ml/proposal/nested-simulations/FB/version-2
specifications/shdml
specifications/shdml.level-1
specifications/shdml.level-1.version-1
specifications/shdml.level-1.version-1.pdf
specifications/teddy
specifications/teddy.owl
specifications/teddy.rel-2007-06-04
specifications/teddy.rel-2007-06-04.owl
specifications/teddy.rel-2011-08-30
specifications/teddy.rel-2014-04-24
specifications/teddy.rel-2014-04-24.owl
standards
standards/biopax
standards/biopax/level-1
standards/biopax/level-2
standards/biopax/level-3
standards/cellml
standards/cellml/1/0
standards/cellml/1/1
standards/gpml
standards/kisao
standards/kisao/libkisao
standards/mamo
standards/miase
standards/miase/explanation
standards/miriam
standards/miriam_uris
standards/neuroml
standards/omex
standards/omex-archive
standards/omex-manifest
standards/omex-metadata
standards/omex-metdata/1/0
standards/omex/RC-1
standards/omex/RC-2
standards/omex/version-1
standards/petab/version-1
standards/qualifiers
standards/sbgn
standards/sbgn/af
standards/sbgn/af/level-1/version-1/0
standards/sbgn/af/level-1/version-1/2
standards/sbgn/er
standards/sbgn/er/level-1/version-1/0
standards/sbgn/er/level-1/version-1/1
standards/sbgn/er/level-1/version-1/2
standards/sbgn/er/level-1/version-2
standards/sbgn/pd
standards/sbgn/pd/level-1/version-1/0
standards/sbgn/pd/level-1/version-1/1
standards/sbgn/pd/level-1/version-1/2
standards/sbgn/pd/level-1/version-1/3
standards/sbml
standards/sbml/level-1/version-1
standards/sbml/level-1/version-2
standards/sbml/level-2/version-1
standards/sbml/level-2/version-2
standards/sbml/level-2/version-3/release-1
standards/sbml/level-2/version-3/release-2
standards/sbml/level-2/version-4/release-1
standards/sbml/level-2/version-5/RC-1
standards/sbml/level-2/version-5/release-1
standards/sbml/level-3
standards/sbml/level-3/version-1
standards/sbml/level-3/version-1/comp
standards/sbml/level-3/version-1/comp/version-1/
standards/sbml/level-3/version-1/comp/version-1/release-1
standards/sbml/level-3/version-1/comp/version-1/release-2
standards/sbml/level-3/version-1/comp/version-1/release-3
standards/sbml/level-3/version-1/core
standards/sbml/level-3/version-1/core/release-1
standards/sbml/level-3/version-1/core/release-2
standards/sbml/level-3/version-1/core/release-3
standards/sbml/level-3/version-1/distrib
standards/sbml/level-3/version-1/distrib/version-1/
standards/sbml/level-3/version-1/distrib/version-1/release-1
standards/sbml/level-3/version-1/fbc
standards/sbml/level-3/version-1/fbc/version-1/
standards/sbml/level-3/version-1/fbc/version-1/release-1
standards/sbml/level-3/version-1/fbc/version-1/release-1
standards/sbml/level-3/version-1/fbc/version-2/
standards/sbml/level-3/version-1/fbc/version-2/release-1
standards/sbml/level-3/version-1/groups
standards/sbml/level-3/version-1/groups/version-1
standards/sbml/level-3/version-1/groups/version-1/release-1
standards/sbml/level-3/version-1/layout
standards/sbml/level-3/version-1/layout/version-1/
standards/sbml/level-3/version-1/layout/version-1/release-1
standards/sbml/level-3/version-1/multi
standards/sbml/level-3/version-1/multi/version-1
standards/sbml/level-3/version-1/multi/version-1/release-1
standards/sbml/level-3/version-1/multi/version-1/release-2
standards/sbml/level-3/version-1/qual
standards/sbml/level-3/version-1/qual/version-1
standards/sbml/level-3/version-1/qual/version-1/release-1
standards/sbml/level-3/version-1/render
standards/sbml/level-3/version-1/render/version-1
standards/sbml/level-3/version-1/render/version-1/release-1
standards/sbml/level-3/version-1/spatial
standards/sbml/level-3/version-1/spatial/version-1
standards/sbml/level-3/version-1/spatial/version-1/release-1
standards/sbml/level-3/version-2
standards/sbml/level-3/version-2/core
standards/sbml/level-3/version-2/core/release-1
standards/sbml/level-3/version-2/core/release-2
standards/sbml/level-3/version-2/distrib
standards/sbml/level-3/version-2/distrib/version-1
standards/sbml/level-3/version-2/distrib/version-1/release-1
standards/sbo
standards/sbol
standards/sbol-visual
standards/sbol-visual/version-1.0.0
standards/sbol-visual/version-2.0
standards/sbol/version-1.1.0
standards/sbol/version-2.0.0
standards/sbol/version-2.0.1
standards/sbol/version-2.1.0
standards/sbol/version-2.2.0
standards/sbolVisual
standards/sed-ml
standards/sed-ml/level-1
standards/sed-ml/level-1/version-1
standards/sed-ml/level-1/version-2
standards/sed-ml/level-1/version-2/RC
standards/sed-ml/level-1/version-2/RC2
standards/sed-ml/level-1/version-3
standards/sed-ml/level-1/version-3/draft-1
standards/sed-ml/proposal
standards/sed-ml/proposal/
standards/sed-ml/proposal/kisao/RA/version-1
standards/sed-ml/proposal/nested-simulations
standards/sed-ml/proposal/nested-simulations/
standards/sed-ml/proposal/nested-simulations/FB/version-1
standards/sed-ml/proposal/nested-simulations/FB/version-2
standards/sed-ml/proposal/nested-simulations/FB/version-3
standards/shdml
standards/shdml/level-1/version-1
standards/specification-infrastructure
standards/specifications
standards/teddy
standards/teddy/ontology
standards/teddy/rel-2014-04-24
Supplementary_materials
test/caltech
test/lenovsandbox
tools
user_help
'''

all_ = '''/events/COMBINE_2019/abstracts
/events/COMBINE_2019/agenda
/standards/sbml/level-3/version-1/core
about
events
standards/sbml/level-3/version-1/core
standards/sbml/level-3/version-1/core/release-1
standards/sbml/level-3/version-1/core/release-2
standards/sbml/level-3/version-1/core/release-3
standards/sbml/level-3/version-1/distrib
events/COMBINE_2018'''


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
        if len(parts)>=4:
            dir = '%s/%s/%s'%(parts[0],parts[1],parts[2])
            if not os.path.exists(dir):
                os.makedirs(dir)
        if len(parts)>=5:
            dir = '%s/%s/%s/%s'%(parts[0],parts[1],parts[2],parts[3])
            if not os.path.exists(dir):
                os.makedirs(dir)
        if len(parts)>=6:
            dir = '%s/%s/%s/%s/%s'%(parts[0],parts[1],parts[2],parts[3],parts[4])
            if not os.path.exists(dir):
                os.makedirs(dir)

    fname = '%s.html'%name
    url = 'http://co.mbine.org/' + l
    url = 'http://131.215.225.44/' + l
    r = requests.get(url)
    if '.pdf' in url or '.owl' in url:
        fname = name
        tgt = '%s/%s'%(dir, fname)
        print("     Copying %s to %s" %(url, tgt))
        open(tgt , 'wb').write(r.content)
    else:
        tgt = '%s/%s'%(dir, fname)
        print("     Copying %s to %s" %(url, tgt))
        cc = r.content.decode()
        cc = cc.replace('http://co.mbine','http://old_co.mbine')
        cc = cc.replace('?q=system/files/','/system/files/')
        cc = cc.replace('href="/freelinking/', 'href="/')
        cc = cc.replace('%20" cla', '" cla')
        updated = str.encode(cc)
        print(type(updated))
        open(tgt , 'w').write(updated.decode())
