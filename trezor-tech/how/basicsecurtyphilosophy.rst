Security philosophy
===================

The zero trust principle
------------------------

TREZOR's security model is based on the principle of zero trust.  The zero trust principle says that any part of a secure system could at some point be compromised.

TODO-insert-diagram-with:

 myTREZOR.com<->Internet<->computer<->TREZOR

Your TREZOR device will continue to protect your bitcoins even in the case that the myTREZOR web wallet and your computer are both infected by viruses.  This is important.  The whole point of TREZOR is being more secure than a traditional web wallet or desktop bitcoin application.

Why does the TREZOR have a screen and buttons?
----------------------------------------------

If you are using your TREZOR device with an untrusted computer and you want to make a payment, how do you know that the payment is going to the right person?  If the TREZOR did not have a screen it would be impossible to know that the payment was being made to the correct address.  Afterall, an infected computer could easilly lie about where the money was going to go.

By making the TREZOR with a screen and physical buttons, you know that no payments will ever be made without you being able to read their amount and being able to physically accept or cancle the payment.

The need for a PIN
------------------

Zero trust doesn't end with not trusting the computer to which you have connected your TREZOR.  We also do not wish to trust the person who is currently holding the TREZOR in their hands.  What if your TREZOR was stolen?  In order to prevent trivial physical theft of the TREZOR device the TREZOR requires you to enter you PIN number each time it is plugged into a computer.  This ensures that not only is each transaction confirmed by a person who is physically present, but that the person confirming the transactions is you.

A single purpose computer
-------------------------

The TREZOR is a single purpose computer.  TREZOR doesn't have a weather app.  There are no free downloads for TREZOR that could compromise the device.

Limmiting the attack surface: no battery, wifi, bluetooth, fingerprint reader, NFC
----------------------------------------------------------------------------------

Any time a computer has to deal with untrusted information there is a risk that the computer will be infected with malware.  The TREZOR is no exception.  In order to limit the attack surface against the TREZOR, TREZOR communicates soley though a simple serial USB protocol.  There is no WIFI or bluetooth, no cammera for scanning QR-codes.  There's not even a fingerprint reader.  This is all because we want the TREZOR to be as secure as possible.  The less the TREZOR talks to, the less likely it is to get infected.

The TREZOR also has no battery.  When its unplugged its off, and your bitcoins are safe from cyber attack.
