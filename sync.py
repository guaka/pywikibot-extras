#!/usr/bin/env python
#
# -*- coding: utf-8  -*-
#
# (C) Kasper Sourenm 2012-2013
#
# Distributed under the terms of the MIT license.
#


import sys
import re
from wikipedia import *


def multiple_replace(text, word_dict):
    for key in word_dict:
        text = text.replace(key, word_dict[key])
    return text


class SyncSites:
    def __init__(self, options):
	self.options = options

        if options.original_wiki:
            original_wiki = options.original_wiki
        else:
            original_wiki = config.sync_default_src

        print "Syncing from " + original_wiki

        family = options.family or config.sync_default_family


        sites = options.destination_wiki
        print sites

        self.original = getSite(original_wiki, family)
        
        if 'help' in options.namespace:
            nsd = dict(map(lambda n: (self.original.getNamespaceIndex(n), n), 
                           self.original.namespaces()))
            for k in nsd:
                print k, nsd[k]
            sys.exit()

        self.sites = map(lambda s: getSite(s, family), sites)
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
        
        ref_users = get_users(self.original)
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
                    self.original.allpages('!', namespace))
        for p in pages:
            if not p in ['MediaWiki:Sidebar', 'MediaWiki:Mainpage', 
                         'MediaWiki:Sitenotice', 'MediaWiki:MenuSidebar']:
                try:
                    self.check_page(p)
                except pywikibot.exceptions.NoPage:
                    print 'Bizarre NoPage exception that we are just going to ignore'
                except pywikibot.exceptions.IsRedirectPage:
                    print 'error: Redirectpage - todo: handle gracefully'
        print


    def generate_overviews(self):
        for site in self.sites:
            sync_overview_page = Page(site, 'User:' + site.loggedInAs() + '/sync.py overview')
            output = "== Pages that differ from original ==\n\n"
            if self.differences[site]:
                output += "".join(map(lambda l: '* [[:' + l + "]]\n", self.differences[site]))
            else:
                output += "All important pages are the same"
            
            output += "\n\n== Admins from original that are missing here ==\n\n"
            if self.user_diff[site]:
                output += "".join(map(lambda l: '* ' + l.replace('_', ' ') + "\n", self.user_diff[site]))
            else:
                output += "All users from original are also present on this wiki"

            print output
            sync_overview_page.put(output, site.loggedInAs() + ' sync.py')


    def check_page(self, pagename):
        print "\nChecking", pagename,
        sys.stdout.flush()
        page1 = Page(self.original, pagename)
        txt1 = page1.get()

        for site in self.sites:
            page2 = Page(site, pagename)
            if page2.exists():
                txt2 = page2.get()
                
            else:
                txt2 = ''
                
            if config.sync_replace:
                txt_new = multiple_replace(txt1, config.sync_replace)
                if txt1 != txt_new:
                    print 'NOTE: text replaced using config.sync_replace'
                    txt1 = txt_new

            if txt1 != txt2:
                print "\n", site, 'DIFFERS'
                self.differences[site].append(pagename)

		if self.options.replace:
		  page2.put(txt1, 'sync.py')
            else:
                sys.stdout.write('.')
                sys.stdout.flush()

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-f", "--family", dest="family",
                        help="wiki family")
    # TODO:  
    #parser.add_argument("-df", "--origin-family", dest="family",
    #                    help="if origin family differs from destination family")
    parser.add_argument("-r", "--replace", action="store_true",
                        help="actually replace pages (without this option you will only get an overview page)")
    parser.add_argument("-o", "--original", dest="original_wiki",
                        help="original wiki")
    parser.add_argument('destination_wiki', metavar='N', type=str, nargs='+',
                        help='destination wiki(s)')
    parser.add_argument("-ns", "--namespace", dest="namespace",
                        help="specify namespace")
    
    (options, args) = parser.parse_known_args()
    print options

    s = SyncSites(options)
    s.check_sysops()
    s.check_namespaces()
    s.generate_overviews()
    
