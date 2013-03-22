pywikibot-extras
================

A bunch of [pywikipediabot](http://www.mediawiki.org/wiki/Manual:Pywikipediabot) scripts built for a client
that could be very useful for others.


sync.py 
-------

`sync.py` can synchronize specific namespaces on several wikis. Great for 
 1. dealing with MediaWiki in a DTAP setup 
 2. dealing with several wikis were one wiki is the "master" wiki that is kept mostly empty but 
  contains the Semantic MediaWiki functionality that needs to be synced to other wikis
 3. copying over an entire wiki (but not the users and other cruft from the database)
 4. copying over a MediaWiki site from a wikifarm that doesn't provide a database dump
 5. synchronizing specific namespaces of different wikis
 6. skipping a tedious export / import process if you just need to copy all pages from a specific namespace

`sync.py` was started with 1. and 2. in mind.

See `sync.py --help` for some options.



deadlinkreport.py
-----------------

Creates a nice overview of dead links.

Currently not very generic.




Feel free to use 
https://github.com/guaka/pywikibot-extras/issues/new



license
-------

MIT, for compatibility with pywikipediabot.
