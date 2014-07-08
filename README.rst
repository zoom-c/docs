SatoshiLabs Documentation Tree
==============================

Deployed on http://doc.satoshilabs.com/

Contents
--------

==================== ===========================================================
**slips**            SatoshiLabs Improvement Proposals
**tools**            Various Tools Used in the Documentation Process
**trezor-devel**     TREZOR Developer Documentation
**trezor-faq**       TREZOR Frequently Asked Questions
**trezor-tech**      TREZOR Technical Documentation
**trezor-user**      TREZOR User Documentation
==================== ===========================================================

References
----------

Built using Sphinx_ with sphinx_rtd_theme_

.. _Sphinx: https://sphinx-doc.org/
.. _sphinx_rtd_theme: https://github.com/snide/sphinx_rtd_theme/

Building the documentation
------------------------

If you have Docker installed you can run:

    make shell

    make html

Then open up _build/index.html in your favorite web browser.
