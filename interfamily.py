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



class InterwikiFamily:
    '''Work is done in here.'''

    def __init__(self):
	self.families = { 
            'velo': ['hitchwiki', 'sharewiki'],
            'veganwiki': ['trashwiki'],
            'couchwiki': ['trashwiki', 'sharewiki', 'hitchwiki', 'velo'],
            'trashwiki': ['veganwiki', 'hitchwiki', 'sharewiki'],
            'sharewiki': ['veganwiki', 'hitchwiki', 'velo', 'trashwiki'],
            'hitchwiki': ['trashwiki'],
            }


        self.wikis = {}
        self.pages = {}
        for family in self.families:
            print "Loading", family
            wiki = self.wikis[family] = getSite('en', family)
            
            self.pages[family] = map(lambda p: p.title(),
                                     wiki.allpages('!', 0))

        for f1 in self.families:
            for title in self.pages[f1]:
                page = Page(self.wikis[f1], title)

                for f2 in self.families[f1]:
                    if title in self.pages[f2]:
                        self.check_link(page, title, f2)

    
    def check_link(self, page, title, family):
        f = family.replace('wiki', '')
        try:
            text = page.get()
            link = '[[' + f + ':' + title + ']]'
            if text.find(link) < 0:
                text += "\n" + link
                print text
                page.put(text, 'adding interfamily link to ' + family)

        except pywikibot.exceptions.NoPage:
            print 'Bizar NoPage exception that we are just going to ignore'
        except pywikibot.exceptions.IsRedirectPage:
            print 'error: Redirectpage - todo: handle gracefully'


if __name__ == '__main__':
    inter = InterwikiFamily()
    
