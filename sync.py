#!/usr/bin/env python
#
# -*- coding: utf-8  -*-
#
# (C) Kasper Sourenm 2012-2013
#
# Distributed under the terms of the MIT license.
#



import sys
sys.path.append("./pywikipedia")
from wikipedia import *

import re



class SyncSites:
    def __init__(self, dtap, options):
	self.options = options

        print 'Checking dtap:', dtap

        if options.original_wiki:
            original_wiki = options.original_wiki
        else:
            original_wiki = config.sync_default_src

        print "Syncing from " + original_wiki

        family = options.family or config.sync_default_family

        sites = ['for', 'ecm']
        if dtap == 'loc':
            sites.append('light')
            sites.reverse()
        self.dummy = getSite(original_wiki, family)
        self.sites = map(lambda s: getSite(s + dtap, family), sites)
        print sites
        self.differences = {}
        self.user_diff = {}
        for s in self.sites:
            self.differences[s] = []
            self.user_diff[s] = []
            
    def check_sysops(self):
        def get_users(site):
            userlist = site.getUrl(site.get_address('Special:Userlist&group=sysop'))
            # Hackery but working. At least on MW 1.15.0
            # User namespace is number 2
            return set(re.findall(site.namespace(2) + ':(\w+)["\&]',  userlist))
        
        ref_users = get_users(self.dummy)
        for site in self.sites:
            users = get_users(site)
            diff = list(ref_users.difference(users))
            diff.sort()
            self.user_diff[site] = diff

    def check_namespaces(self):
        namespaces = [
            0,   # Main
            8,   # MediaWiki
            152, # DPL
            102, # Eigenschap
            104, # Type
            106, # Formulier
            108, # Concept
            10,  # Sjabloon
            ]
        
        if self.options.namespace:
            print options.namespace
            namespaces = [int(options.namespace)]
        print "Checking these namespaces", namespaces
        # self.check_page('Versienummer')

        for ns in namespaces:
            self.check_namespace(ns)

    def check_namespace(self, namespace):
        print "CHECKING NAMESPACE", namespace
        pages = map(lambda p: p.title(),
                    self.dummy.allpages('!', namespace))
        for p in pages:
            if not p in ['MediaWiki:Sidebar', 'MediaWiki:Mainpage', 
                         'MediaWiki:Sitenotice', 'MediaWiki:MenuSidebar']:
                try:
                    self.check_page(p)
                except pywikibot.exceptions.NoPage:
                    print 'Bizarre NoPage exception that we are just going to ignore'
        print


    def generate_overviews(self):
        for site in self.sites:
            sync_overview_page = Page(site, 'User:' + site.loggedInAs() + '/sync.py overview')
            output = "== Pages that differ from dummy ==\n\n"
            if self.differences[site]:
                output += "".join(map(lambda l: '* [[:' + l + "]]\n", self.differences[site]))
            else:
                output += "All important pages are the same"
            
            output += "\n\n== Admins from dummy that are missing here ==\n\n"
            if self.user_diff[site]:
                output += "".join(map(lambda l: '* ' + l.replace('_', ' ') + "\n", self.user_diff[site]))
            else:
                output += "All users from dummy are also present on this wiki"

            print output
            sync_overview_page.put(output, site.loggedInAs() + ' sync.py')


    def check_page(self, pagename):
        print "\nChecking", pagename,
        sys.stdout.flush()
        page1 = Page(self.dummy, pagename)
        txt1 = page1.get()

        for site in self.sites:
            page2 = Page(site, pagename)
            if page2.exists():
                txt2 = page2.get()
            else:
                txt2 = ''

            if txt1 != txt2:
                print "\n", site, 'DIFFERS'
                self.differences[site].append(pagename)

		if self.options.replace:
		  page2.put(txt1, 'Synchronisatie van dummy')
            else:
                sys.stdout.write('.')
                sys.stdout.flush()

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-p", "--family", dest="family",
                        help="replace pages")
    parser.add_argument("-r", "--replace", action="store_true",
                        help="replace pages")
    parser.add_argument("-o", "--original", dest="original_wiki",
                        help="original wiki")
    parser.add_argument("-ns", "--namespace", dest="namespace",
                        help="specify namespace")
    
    (options, args) = parser.parse_known_args()
    print options

    if len(args) == 0:
        args = ['loc']

    for dtap in args:
        s = SyncSites(dtap, options)
        s.check_sysops()
        s.check_namespaces()
        s.generate_overviews()
