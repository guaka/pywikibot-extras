# -*- coding: utf-8  -*-
import family, config

# www.hitchwiki.org 

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'hitchwiki'
        self.langs = {
                'en': 'hitchwiki.org',
                'es': 'hitchwiki.org',
                'fr': 'hitchwiki.org',
                'de': 'hitchwiki.org',
                'ru': 'hitchwiki.org',
                'fi': 'hitchwiki.org',
                'pt': 'hitchwiki.org',
                'bg': 'hitchwiki.org',
                'zh': 'hitchwiki.org',
                'pl': 'hitchwiki.org',
                'tr': 'hitchwiki.org',
                'nl': 'hitchwiki.org',
                'ro': 'hitchwiki.org',
                'he': 'hitchwiki.org',
                'hr': 'hitchwiki.org',
        }
        self.namespaces[1] = {
            '_default': u'Talk',
            'ar': u'نقاش',
            'ca': u'Discussió',
            'de': u'Diskussion',
            'eo': u'Diskuto',
            'es': u'Discusión',
            'fi': u'Keskustelu',
            'fr': u'Discuter',
            'he': u'שיחה',
            'hi': u'वार्ता',
            'hu': u'Vita',
            'it': u'Discussione',
            'ja': u'ノート',
            'ko': u'토론',
            'nl': u'Overleg',
            'pl': u'Dyskusja',
            'pt': u'Discussão',
            'ro': u'Discuţie',
            'ru': u'Обсуждение',
            'sv': u'Diskussion',
            'bg': u'Беседа',
            'tr': u'Tartışma',
            }
        self.namespaces[2] = {
            '_default': u'User',
            'de': u'Benutzer',
            'es': u'Usuario',
            'fr': u'Utilisateur',
            'fi': u'Käyttäjä',
            'nl': u'Gebruiker',
            'pl': u'Użytkownik',
            'pt': u'Usuário',
            'ro': u'Utilizator',
            'ru': u'Участник',
            'sv': u'Användare',
            'bg': u'Потребител',
            'tr': u'Kullanıcı',
            }

        self.namespaces[4] = {
            '_default': u'Hitchwiki',
            'de'      : u'Tramperwiki',
            'es' : u'Autostopwiki',
            'tr' : u'Otostopviki',
            'fi' : u'Liftariwikiin',
            'pl' : u'Autostopwiki',
            'pt' : u'CaronaWiki',

            }
        self.namespaces[5] = {
            '_default': u'Hitchwiki talk',
            'de'      : u'Tramperwiki Diskussion',
            'fr'      : u'Discussion Hitchwiki',
            'pl' : u'Dyskusja Autostopwiki',
            'pt' : u'CaronaWiki Discussão',
            'ru' : u'Обсуждение Hitchwiki',
            'tr' : u'Otostopviki tartışma',
            'bg' : u'Hitchwiki беседа',
            'es' : u'Autostopwiki Discusión',
            'fi' : u'Keskustelu Liftariwikiinista',
            'nl' : u'Overleg Hitchwiki',
            }
        self.namespaces[14] = {
            '_default': u'Category',
            'de': u'Kategorie',
            'fr': u'Catégorie',
            'ru': u'Категория',
            'fi': u'Luokka',
            'nl': u'Categorie',
            'pl': u'Kategoria',
            'pt': u'Categoria',
            'ro': u'Categorie',
            'ru': u'Категория',
            'sv': u'Kategori',
            'es': u'Categoría',
            'bg': u'Категория',
            'tr': u'Kategori',
            }

#        self.namespaces[1] = {
#            '_default': [u'Talk', self.namespaces[4]['_default']],
#            'de': [u'Diskussion', self.namespaces[4]['_default']],
#            }
#        self.namespaces[2] = {
#            '_default': [u'User', self.namespaces[4]['_default']],
#            'de': [u'Benutzer', self.namespaces[4]['_default']],
#            'es': [u'Usuario', self.namespaces[4]['_default']],
#            }
#
#        self.namespaces[4] = {
#            '_default': [u'Hitchwiki', self.namespaces[4]['_default']],
#            'de'      : [u'Tramperwiki', self.namespaces[4]['_default']],
#            }
#        self.namespaces[5] = {
#            '_default': [u'Hitchwiki talk', self.namespaces[5]['_default']],
#            'de'      : [u'Tramperwiki Diskussion', self.namespaces[4]['_default']],
#            }
#	
#        self.namespaces[14] = {
#            '_default': [u'Category', self.namespaces[4]['_default']],
#            'de': [u'Kategorie', self.namespaces[4]['_default']],
#            }
    def hostname(self,code):
        return 'hitchwiki.org'

    def scriptpath(self, code):
        return '/%s/index.php' % code

    def apipath(self, code):
        return '/%s/api.php' % code

    def shared_image_repository(self, code):
        return ('en', 'en')

    def version(self, code):
        return "1.19.2"

