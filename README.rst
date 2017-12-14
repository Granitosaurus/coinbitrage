===========
coinbitrage
===========


.. image:: https://img.shields.io/pypi/v/coinbitrage.svg
        :target: https://pypi.python.org/pypi/coinbitrage

.. image:: https://img.shields.io/travis/granitosaurus/coinbitrage.svg
        :target: https://travis-ci.org/granitosaurus/coinbitrage

.. image:: https://readthedocs.org/projects/coinbitrage/badge/?version=latest
        :target: https://coinbitrage.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/granitosaurus/coinbitrage/shield.svg
     :target: https://pyup.io/repos/github/granitosaurus/coinbitrage/
     :alt: Updates


Command line interface application for comparing coin prices for crypto-currency arbitrage

::

    $ coinbitrage diff bitfinex gdax
    ┌──────────┬──────────┬───────┬─────────┬───────────┐
    │ currency │ bitfinex │ gdax  │ diff    │ diff_perc │
    ├──────────┼──────────┼───────┼─────────┼───────────┤
    │ Litecoin │ 283.6    │ 283.8 │ 0.21700 │ -0.07652  │
    │ Ethereum │ 686.4    │ 696.2 │ 9.713   │ -1.41498  │
    │ Bitcoin  │ 16355    │ 16869 │ 514.3   │ -3.14458  │
    └──────────┴──────────┴───────┴─────────┴───────────┘


* Free software: GNU General Public License v3
* Documentation: https://coinbitrage.readthedocs.io.

Features
--------

::

    $coinbitrage diff --help
    Usage: coinbitrage diff [OPTIONS] EXCHANGE1 EXCHANGE2

      show difference between two exchanges

    Options:
      --reverse       reverse ordering
      --sort-by TEXT  which column to sort by [diff, diff_perc]  [default:
                      diff_perc]
      --help          Show this message and exit.

To run continuously use gnu's watch_ tool.
For example, if you wish to continuesly observe difference between bitfinex and binance exchanges
you could run: `watch -n 30 "coinbitrage diff bitfinex binance"` to get data every 30 seconds.

.. _watch: https://en.wikipedia.org/wiki/Watch_(Unix)#External_links

Credits
---------

Pricing data is provided by http://coinmartketcap.com
This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

