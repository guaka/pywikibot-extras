# -*- coding: utf-8  -*-
#
# (C) Kasper Sourenm 2012-2013
#
# Distributed under the terms of the MIT license.
#


import wikipedia
import codecs, pickle
import datetime

def create_report(family, wiki, extra_fields = False):
    datfilename = wikipedia.config.datafilepath('deadlinks',
						'deadlinks-%s-%s.dat'
						% (family, wiki))
    datfile = open(datfilename, 'r')
    historyDict = pickle.load(datfile)

    d = historyDict

    def nicetime(t):
        return datetime.datetime.fromtimestamp(float(t)).strftime('%Y-%m-%d')

    def link_report(info):
	dates = map(lambda x: x[1], info)
	last = nicetime(max(dates))
	first = nicetime(min(dates))
	error = info[0][2].replace('404 Not Found', '404')
	page = info[0][0]

        if not extra_fields:
            return '||'.join([page, error, first, last])

        else:
            editors = get_editors(wiki, page)
            if wiki == 'forprod':
                page = '[[blauw:' + page + '|]]'
                
            return '||'.join([page, error, first, last,
                              editors['auteur'],
                              editors['bureauredacteur']
                              ])

    def get_editors(site, pagename):
        '''Find extra fields'''

        page = wikipedia.Page(site, pagename)
        editors = { 'auteur': '',
                    'bureauredacteur': '' }
        try:
            text = page.get()
            for l in text.split("\n"):
                if l.startswith("|Bureauredacteur"):
                    editors['bureauredacteur'] = l.replace('|Bureauredacteur=', '')
                if l.startswith("|Auteur"):
                    editors['auteur'] = l.replace('|Auteur=', '')
        except wikipedia.pywikibot.exceptions.NoPage:
            editors['auteur'] = 'NoPage exception'
        return editors

    def save_report(site, pagename, report):
        page = wikipedia.Page(site, pagename)
        page.put(report)

    output = """{| class='sortable max-width'
|-
| link || pagina || fout || eerst || laatst || redacteur || bureauredacteur
|-""" + "\n|-\n".join(map(lambda k: ("|"+ k + '||' + link_report(d[k])), d)) + "\n|}"


    pagename = "User:" + site.loggedInAs() + "/linkrapport " + wiki
    site = wikipedia.getSite("ecmprod", family)
    save_report(site, pagename, output)

    pagename = "User:" + site.loggedInAs() + "/linkrapport"
    site = wikipedia.getSite(wiki, family)
    save_report(site, pagename, output)
    

for dtap in ['test', 'prod', 'acc']:
    for wiki in ['for', 'eka', 'ecm']:
        print wiki + dtap
        try:
            create_report(config.deadlinkreport_default_family, wiki + dtap, True)
        except EOFError:
            print EOFError, ' with ', wiki + dtap
