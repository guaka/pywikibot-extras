# -*- coding: utf-8  -*-
import family, config

# The wikitravel family

# Translation used on all wikitravels for the 'article' text.
# A language not mentioned here is not known by the robot

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'veganwiki'
        self.langs = {
            'en':'en',
        }

    def hostname(self,code):
        return 'vegan.wiki.yt'
