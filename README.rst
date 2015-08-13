Goal
====

-  Create a simple importable Python module which will produce parsed
   WHOIS data for a given domain.
-  Able to extract data for all the popular TLDs (com, org, net, ...)
-  Query a WHOIS server directly instead of going through an
   intermediate web service like many others do.
-  Works with Python 2.4+ and no external dependencies

Example
=======

.. sourcecode:: python

    >>> import whois
    >>> w = whois.whois('webscraping.com')
    >>> w.expiration_date  # dates converted to datetime object
    datetime.datetime(2013, 6, 26, 0, 0)
    >>> w.text  # the content downloaded from whois server
    u'\nWhois Server Version 2.0\n\nDomain names in the .com and .net 
    ...'

    >>> print w  # print values of all found attributes
    creation_date: 2004-06-26 00:00:00
    domain_name: [u'WEBSCRAPING.COM', u'WEBSCRAPING.COM']
    emails: [u'WEBSCRAPING.COM@domainsbyproxy.com', u'WEBSCRAPING.COM@domainsbyproxy.com']
    expiration_date: 2013-06-26 00:00:00
    ...

Install
=======

Install from pypi:

.. sourcecode:: python

    pip install python-whois

Or checkout latest version from repository:

.. sourcecode:: python

    hg clone https://bitbucket.org/richardpenman/pywhois

Contact
=======

You can post ideas or patches here:
https://bitbucket.org/richardpenman/pywhois/issues

Thanks to the many who have sent patches for additional domains!
