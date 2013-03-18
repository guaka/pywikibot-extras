pywikibot-extras
================

A bunch of [pywikipediabot](http://www.mediawiki.org/wiki/Manual:Pywikipediabot) scripts I built for a client that could be
very useful for others.


sync.py 
-------

`sync.py` can synchronize specific namespaces on several wikis. Great for 
* dealing with MediaWiki in a DTAP setup (this was the use case for which it was built)
* copying over an entire wiki (but not the users and other cruft from the database)
* synchronizing specific namespaces of different wikis
* copying over a MediaWiki site from a wikifarm that doesn't provide a database dump

See `sync.py --help` for some options.



deadlinkreport.py
-----------------

Create a nice overview of dead links.

Currently not very generic.


license
-------

MIT, for compatibility with pywikipediabot.
