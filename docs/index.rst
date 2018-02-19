.. layabout documentation master file

Layabout
========

Release v\ |release|.

.. image:: https://img.shields.io/travis/reillysiemens/layabout/master.svg?style=flat-square&label=build
    :target: https://travis-ci.org/reillysiemens/layabout
    :alt: Unix build status on Travis CI

.. image:: https://img.shields.io/coveralls/reillysiemens/layabout/master.svg?style=flat-square&label=coverage
    :target: https://coveralls.io/github/reillysiemens/layabout?branch=master
    :alt: Code coverage on Coveralls

.. image:: https://img.shields.io/badge/license-ISC-blue.svg?style=flat-square
    :target: https://github.com/reillysiemens/layabout/blob/master/LICENSE
    :alt: ISC Licensed

**Layabout** is a small event handling library on top of the Slack RTM API.

.. code-block:: python

   from pprint import pprint
   from layabout import Layabout

   layabout = Layabout('app')


   @layabout.handle('*')
   def debug(slack, event):
       """ Pretty print every event seen by the app. """
       pprint(event)


   @layabout.handle('message')
   def echo(slack, event):
       """ Echo all messages seen by the app except our own. """
       if event.get('subtype') != 'bot_message':
           slack.rtm_send_message(event['channel'], event['text'])


   def someone_leaves(events):
       """ Return False if a member leaves, otherwise True. """
       return not any(e.get('type') == 'member_left_channel'
                      for e in events)

   if __name__ == '__main__':
       layabout.run(until=someone_leaves)
       print("Don't talk to me or my handlers ever again!")

Installation
------------

To install **Layabout** run this command in your terminal:

.. code-block:: bash

   pip install git+https://github.com/reillysiemens/layabout.git@master

Features
--------

Not sold yet? Here's a list of features to sweeten the deal.

- Automatically load Slack API tokens from environment variables or provide
  them directly.
- Register multiple event handlers for one event.
- Register a single handler for multiple events by stacking decorators.
- Configurable application shutdown.
- Configurable retry logic in the event of lost connections.
- Lightweight. Depends only on the official Python `slackclient`_ library.

.. note::

   Layabout **only** supports Python 3.6+ and will never be backported to
   Python 2. If you haven't moved over to Python 3 yet please consider the
   `many reasons to do so <http://www.asmeurer.com/python3-presentation/slides.html>`_.

Project Info
------------

.. toctree::
   :maxdepth: 1

   why
   changelog
   license
   authors
   contributing
   code_of_conduct

.. TODO remove this

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _slackclient: https://github.com/slackapi/python-slackclient
