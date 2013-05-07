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

    def __init__(self, mapping):
	self.families = mapping

        self.wikis = {}
        self.pages = {}
        for family in self.families:
            print "Loading page list from", family
            wiki = self.wikis[family] = getSite('en', family)
            
            self.pages[family] = map(lambda p: p.title(),
                                     wiki.allpages('!', 0))
            self.pages[family].reverse()

        for f1 in self.families:
            if self.families[f1]:
                for title in self.pages[f1]:
                    page = Page(self.wikis[f1], title)

                    try:
                        text = page.get()
                        self.check_text(f1, page, text)
                    except pywikibot.exceptions.IsRedirectPage:
                        print 'Error: Redirectpage ' + f1 + ' - ' + title 
                        
    def check_text(self, f1, page, text):
        title = page.title()
        new_links = []
        for f2 in self.families[f1]:
            if title in self.pages[f2]:
                f = f2.replace('wiki', '')
                link = '[[' + f + ':' + title + ']]'
                if text.find(link) < 0:
                    new_links.append(link)
                else:
                    print f1, title, 'already has link', link

        for new_link in new_links:
            text += "\n" + new_link
            print text
        if new_links:
            page.put(text, 'adding interfamily links')
            


if __name__ == '__main__':
    mapping = { 
            'sharewiki': ['veganwiki', 'hitchwiki', 'velo', 'trashwiki'],
            'velo': [], #['hitchwiki', 'sharewiki'],
            'couchwiki': ['trashwiki', 'sharewiki', 'hitchwiki', 'velo'],
            'trashwiki': [], #['veganwiki', 'hitchwiki', 'sharewiki'],
            'veganwiki': [], #['trashwiki'],
            'hitchwiki': ['trashwiki'],
            }

    inter = InterwikiFamily(mapping)
    
