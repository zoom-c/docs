Overview
========

What is TREZOR?
---------------

TREZOR is a single purpose device which allows you to make secure Bitcoin transactions. With TREZOR, transactions are completely safe even when initiated on a compromised or vulnerable computer.  Because the use of TREZOR is very easy and intuitive we believe it will help Bitcoin adoption among common people.

.. image:: images/trezor_transparent.png

How does TREZOR work?
---------------------

The Bitcoin protocol works by sending signed notes of payment across the Internet.  These messages(which are referred to as Transactions) are signed using a special algorithm.  In order to sign a Bitcoin transaction you need to have a special key or password.  TREZOR holds that key.  Since TREZOR's job is to help you securely sign Transaction messages, you can think of you TREZOR as a modern day stamp.

.. image:: images/stamp.jpg

(image credit  `Petr Kvashin <http://www.publicdomainpictures.net/view-image.php?image=038943>`_)

TREZOR is better than an ordinary mechanical stamping mechanism, however.  Each TREZOR has a PIN code. If your TREZOR gets stolen, thieves cannot misuse it to steal your money.  Due to TREZOR's clever design, even if the computer with which you use your TREZOR is hacked, the hackers will never know your PIN.

In contrast to the various pieces of software and web services that allow you to store your Bitcoins TREZOR is secure.  Software and web based solutions keep your Bitcoin signing keys either on your computer, or worse, on the Internet!  When you use such a service, hackers can easily steal your Bitcoins by hacking your computers or hacking the servers of the services that you use.

Which operating systems and devices support TREZOR?
---------------------------------------------------

There is full support in Windows, OS X and Linux.  Support for using your TREZOR with Android devices which have USB On-The-Go (aka USB Host) support is planned in a future release.

What kind of hardware specs does the TREZOR have?
-------------------------------------------------

.. image:: images/trezor_pcb.png

**CPU**
  TREZOR is using a 120 MHz embedded ARM processor (Cortex M3 to be precise) with a custom developed system.

**Screen**
  Bright OLED - 128x64 pixels.  Enough to hold six lines of text.  Can display all the details you need to verify a transaction in a single screenfull.

**Case**
  Both TREZOR Classic and TREZOR Metallic will have a similar case with dimensions of approx. 60 x 30 x 6 mm. The Classic edition is made of a reinforced plastic providing great durability. The Metallic TREZOR is made of a polished CNC milled aluminum.

**Safety and certifications**
  The TREZOR is CE and RoHS certified, so it meets all quality, reliability and environmental standards.  Its fine to take your TREZOR with you on the airplane.  Like all modern electronics, the X-Rays won't hurt it.

**Operating temperature**
  -20°C to +60°C (-4°F - +140°F)

What if I lose my TREZOR?
-------------------------

TREZOR comes with excellent support for paper wallets.  When you set up your TREZOR for the first time you will be told a list of secret words to write down.  Once you have written down this list, you can recover your Bitcoins at any time using a replacement TREZOR.

Which wallets are compatible with TREZOR?
-----------------------------------------

- `MyTREZOR <http://www.mytrezor.com>`_ - full support
- `MyTREZOR Lite (Android) <https://play.google.com/store/apps/details?id=com.satoshilabs.btcreceive>`_ - allows to import xpub + watch only mode
- Electrum 2.0 does support TREZOR already (possible to build the client from `github <https://github.com/spesmilo/electrum>`_. If you are not able to compile the client from source, you need to wait for Electrum developers to build the packages for you)
- Multibit HD beta supports it (however it still has not been released yet, please ask Multibit HD developers)
- GreenAddress.it will support TREZOR since firmware 1.3.0 with Multisig support release
- Armory support planned
- BitPay's Copay support planned

Which wallets can be used to recover your seed without TREZOR?
------------------------------------------------------------

These wallets are not compatible, but if you lose your TREZOR, you can use them to recover your seed into:

- `Mycelium Bitcoin Wallet for Android <https://play.google.com/store/apps/details?id=com.mycelium.wallet>`_ - supports full recovery
- `Mycelium Bitcoin Wallet for iOS <https://itunes.apple.com/us/app/mycelium-bitcoin-wallet/id943912290>`_ - supports 12 words recovery only
- `Wallet32 for Android <https://play.google.com/store/apps/details?id=com.bonsai.wallet32>`_ - supports full recovery
