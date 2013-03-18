pywikibot-extras
================

A bunch of [pywikipediabot](http://www.mediawiki.org/wiki/Manual:Pywikipediabot) scripts I built for a client that could be
very useful for others.


sync.py 
-------

`sync.py` can synchronize specific namespaces on several wikis. Great for 
* dealing with MediaWiki in a DTAP setup (this was the use case for which it was built)
* copying over an entire wiki (but not the users and other cruft from the database)
* copying over a MediaWiki site from a wikifarm that doesn't provide a database dump
* synchronizing specific namespaces of different wikis
* skipping a tedious export / import process if you just need to copy all pages from a specific namespace

See `sync.py --help` for some options.



deadlinkreport.py
-----------------

Create a nice overview of dead links.

Currently not very generic.




Feel free to use 
https://github.com/guaka/pywikibot-extras/issues/new



license
-------

MIT, for compatibility with pywikipediabot.
