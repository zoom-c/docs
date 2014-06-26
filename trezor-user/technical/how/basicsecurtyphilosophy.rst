The zero trust principle
-----------------

TREZOR's security model is based on the principle of zero trust.  The zero trust principle says that any part of a secure system could at some point be compromised.

TODO-insert-diagram-with:

 myTREZOR.com<->Internet<->computer<->TREZOR

Your TREZOR device will continue to protect your bitcoins even in the case that the myTREZOR web wallet and your computer 

A single purpose computer
----------------------

Limmiting the attack surface: no battery, wifi, bluetooth, fingerprint reader, NFC
----------------------

Any time a computer has to deal with untrusted information there is a risk that the computer will be infected with malware.  The TREZOR is no exception.  In order to limit the attack surface against the TREZOR, TREZOR communicates soley though a simple serial USB protocol.  There is no WIFI or bluetooth, no cammera for scanning QR-codes.  There's not even a fingerprint reader.  This is all because we want the TREZOR to be as secure as possible.  The less the TREZOR talks to, the less likely it is to get infected.

The TREZOR also has no battery.  When its unplugged its off, and your bitcoins are safe from cyber attack.

Why TREZOR has a screen and buttons
------------------------

For those of use used to swiping our credit cards and entering a PIN to make our payment's the TREZOR's screen and button's may seem a bit bulky.  You may find yourself wondering: why does my payment device need a screen anyways?

TREZOR's security is much greater than that of a common credit card.  You could reasonablly have millions of dollars worth of bitcoins loaded onto your TREZOR device.  You could also use TREZOR safely in a foreing country where you don't trust the bank machines.
