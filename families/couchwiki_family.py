# -*- coding: utf-8  -*-
import family, config

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'couchwiki'
        self.langs = {
            'en': 'en',
            'fr': 'fr',
            'it': 'it',
        }

    def hostname(self, code):
        return 'couchwiki.org'

#    def scriptpath(self, code):
#        # return '/w/%s' % code
#        return '/w'

    def apipath(self, code):
        return '/w/api.php'
