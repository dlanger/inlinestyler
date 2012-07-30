============================================
inlinestyler - Making Styled HTML Email Easy
============================================

:Version: 0.1.7
:Download: http://pypi.python.org/pypi/inlinestyler/
:Source: http://github.com/dlanger/inlinestyler/
:Keywords: inline, HTML, CSS, email, preflight

`inlinestyler` is an easy way to locally inline CSS into an HTML email message.

Styling HTML email is a `black art`_. CSS works, but only when it's been placed
inline on the individual elements (and event then, not always) - which makes
development frustrating, and iteration slow. 

The general solution is to use an inlining service, which takes a message with 
the CSS placed externally, and rewrites it so that all CSS is applied to the
individual elements. The most widely used of these services - and as far as I 
can tell, the one that powers CampaignMonitor - is `Premailer`_. It's a great 
service, and the guys behind it put a lot of work into keeping it up to date
with the most recent discoveries in what works and what doesn't.

`inlinestyler` takes (most) of the functionality of Premailer, and makes it 
available locally, accessible without having call a remote service. 

To see what `inline-styler` can do, check out this `demo`_.

.. _`black art`: http://www.campaignmonitor.com/css/
.. _`Premailer`: http://premailer.dialect.ca/
.. _`demo`: http://inlinestyler.torchboxapps.com/

History
=======

`Dave Cranwell`_ wrote the original `inline-styler`_ single-app Django project, 
and (graciously) released it. `inlinestyler` is a refactor of that project into 
a free-standing package usable outside of Django.

.. _`inline-styler`: https://github.com/davecranwell/inline-styler
.. _`Dave Cranwell`: http://www.twitter.com/davecranwell

Requirements
============

`inlinestyler` requires the following packages in order to run:

* ``cssutils`` (which will be installed by ``pip``)
* ``lxml`` (which we assume you already have installed through your OS)

It also requires a ``css_complaiance.csv`` file, which indicates the 
compatibility of various email clients with certain CSS features. This
is included with the package, but can be updated manually from 
`Campaign Monitor`_'s spreadsheet.

.. _`Campaign Monitor`: http://www.campaignmonitor.com/css/

Usage
=====

::

     from inlinestyler.utils import inline_css
     message_inline_css = inline_css(message_external_css)


``message_external_css`` must be a string containing the message to be inlined, 
with the CSS presented in the HTML as one of:

* an absolute link ``<link rel="stylesheet" href="http://mysite.com/styles.css" />`` 
* a ``<style>`` block in the ``<head>``, without the use of ``@import``.

The code will also calculate an estimate for how compatible your message is with 
various clients (using the ``css_compliance.csv`` file), but this number isn't 
yet exposed. 

Contributions
=============

All development happens at github: http://github.com/dlanger/inlinestyler.

Contributions are always more than welcome. If you see something missing, add it
in and send me a pull request.

License
=======

This distribution is licensed under the ``New BSD License``. Please see the 
``LICENSE`` file for a full copy of the license text.

As far as I can tell, Dave Cranwell `released`_ the underlying `inline-styler`
project into the public domain:

   I'm [...] releasing it to the public after many requests for the source.

.. _`released`: https://github.com/davecranwell/inline-styler/blob/c22a5fb67771d082ce0e999ea814dbdf2f05cdfe/README
