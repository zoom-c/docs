Using passphrase encrypted seeds
--------------------------------

In addition to a PIN is possible to add a passphrase to your TREZOR.  This has the advantage of making your TREZOR impervious to phisical attack.  Even if your TREZOR were to be stolen and the chip examined under an electron microscope to discover your recovery seed your bitcoins would still be safe!  A passphrase can be a word or any set of letters that you might use as a password.  Your passphrase should be memorable though.  You typically would not write it down anywhere to eliminate any possibility of it being discovered.

One limitation of the passphrase approach is that you have to enter your passphrase into the computer that you use with your TREZOR.  For this reason, you should not be tempted to dissable your PIN if you use a passphrase as well!

The flip side to this extreme level of security is that if you forget your passphrase your bitcoins are lost.  Really lost! 

Multi-passphrase encryption (hidden volumes)
--------------------------------------------

Security researchers have a habit of comming up with spicy names for simple attacks.  One such attack is refered to as the $5 wrench attack.

.. image:: ../images/5-dollar-wrench.png

(Image credit Randall Munroe xkcd.com and used under the terms of the Ceative Commons Attribution license)

If you have your passphrase memorized and you haven't written it down anywhere, attackers with physical access to your TREZOR may still be able to extract the passphrase with a $5 wrench.   In order to mitigate this risk it is possible to set up your TREZOR multiple times with mutliple passphrases.  The goal is to have one "spoof" setup that only holds a few bitcoins or cents, then a "real" setup that holds your fortune.

In order to do this all you need to do is setup your TREZOR with a passphrase, then unplug and replug your TREZOR and enter a different passphrase.  Here's an example:

I setup my TREZOR with the passphrase "lonelypumpkins" and load a large number of bitcoins onto my device.  I unplug/replug my TREZOR and enter the passphrase "fooybarness".  I then send a few bitcents to the "fooybarness" TREZOR.  When the thugs come and steal my TREZOR, I can now safely tell them that my passphrase is "fooybarness" and they will not be able to tell that I actually have a large number of bitcoins hidden away.

.. note:: Do not use either the passphrase "lonelypumpkins" nor the passphrase "fooybarness" to secure your TREZOR device! 