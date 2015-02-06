Overview
========

What is TREZOR?
---------------

TREZOR is a single purpose device which allows you to make secure Bitcoin transactions. With TREZOR, transactions are completely safe even when initiated on a compromised or vulnerable computer.  Because the use of TREZOR is very easy and intuitive we believe it will help Bitcoin adoption among people not familiar with the security issues.

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

There is full support in Windows, OS X (version 10.8 and higher) and Linux.  Support for using your TREZOR with Android devices which have USB On-The-Go (aka USB Host) support is planned in a future release.

Can I plug TREZOR into USB 3.0 (blue) port?
-------------------------------------------

No TREZOR is USB 2.0 (black port) compatible device. It might not work properly when plugged into USB 3.0 (blue port).

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

Which wallets are compatible with TREZOR hardware?
--------------------------------------------------

These wallets can communicate with TREZOR hardware and use its full potential.

- `myTREZOR <http://www.mytrezor.com>`_
- Electrum 2.0 (binaries not released yet, sources available from `github <https://github.com/spesmilo/electrum>`_)
- Multibit HD (not released yet, in closed beta, ask Multibit HD developers for access)
- `GreenAddress.it <http://www.greenaddress.it>`_ (once 1.3.0 firmware with Multisig support is released)
- Armory support planned
- BitPay's Copay support planned

Which wallets are compatible with TREZOR recovery seed?
-------------------------------------------------------

These wallets cannot communicate with TREZOR hardware yet, but you can use them to access your funds using TREZOR recovery seed.

- `Mycelium Bitcoin Wallet for Android <https://play.google.com/store/apps/details?id=com.mycelium.wallet>`_ - supports full recovery
- `Mycelium Bitcoin Wallet for iOS <https://itunes.apple.com/us/app/mycelium-bitcoin-wallet/id943912290>`_ - supports 12 words recovery only (18 and 24 words soon)
- `Wallet32 for Android <https://play.google.com/store/apps/details?id=com.bonsai.wallet32>`_ - supports full recovery

Which watch-only wallets can import TREZOR account public keys (xpub)?
----------------------------------------------------------------------

These wallets cannot operate with your funds, but you can use them to watch transactions and generate receive addresses for your TREZOR accounts.

- `myTREZOR Lite (Android) <https://play.google.com/store/apps/details?id=com.satoshilabs.btcreceive>`_
