TREZOR Frequently Asked Questions
===================

What is TREZOR?
---------------

.. image:: images/trezor_transparent.png

TREZOR is a single purpose computer which allows you to make secure Bitcoin transactions. With TREZOR, transactions are completely safe even on a compromised or vulnerable computer.  Because the use of TREZOR is very easy and intuitive we believe it will help Bitcoin adoption among common people.

How does TREZOR work?
----------------------

The Bitcoin protocol works by sending signed notes of payment across the internet.  These messages(which are refered to as Transactions) are signed using a special algorithm.  In order to sign a Bitcoin transaction, you need to have a special key or password.  TREZOR holds that key.  Since TREZOR's job is to help you securely sign Transaction messages, you can think of you TREZOR as a modern day stamp.

.. image:: images/stamp.jpg

(image credit  `Petr Kvashin <http://www.publicdomainpictures.net/view-image.php?image=038943>`_)

TREZOR is much superior to an ordinary mechanical stamping mechanism, however.  The TREZOR has a PIN code, so if it gets stolen theives cannot missuse it to steal your money.  TREZOR has also been cleaverly designed so that even if the computer with wich you use your TREZOR is hacked, the hackers will never know your PIN.

In contrast to the various peices of software and web services that allow you to store your Bitcoins TREZOR is secure.  Software and web based solutions keep your Bitcoin signing keys either on your computer, or worse, on the Internet!  When you use such a service, hackers can easilly steal your bitcoins by hacking your computers or hacking the servers of the service that you use.

Which operating systems and devices support TREZOR?
--------------------------------------------------

There is full support in Windows, Mac OSx, Linux.  Support for using your TREZOR with Android devices which have USB On The Go support is planned in a future release. 

Can I use TREZOR with more than one Bitcoin account?
---------------------------------------------
Yes, the TREZOR can store the keys to an unlimited number of active Bitcoin accounts.  You can read about the cryptography that allows for this in the TREZOR Technical Manual in the `Cryptography <http://doc.satoshilabs.com/trezor-tech/cryptography.html>`_ section.


What kind of hardware specs does the TREZOR have?
----------------------------------------------

**CPU**
  TREZOR is using a 120 MHz embedded ARM processor (Cortex M3 to be precise) with a custom developed system.

**Screen**
  Bright bluish OLED - 128x64 pixels.  Enough to hold four lines of text.  Can display all the details you need to verify a transaction in a single screenfull.

**Case**
  Both TREZOR Classic and TREZOR Metallic will have a similar case with dimensions of approx. 59 x 30 x 6 mm. The Classic edition is made of a reinforced plastic providing great durability. The Metallic TREZOR is made of a polished  CNC milled aluminum.

**Safety and certifications**
  The TREZOR is CE and RoHS certified.  Its fine to take your TREZOR with you on the airplane.  Like all modern electronics, the XRays won't hurt it.

**Operating temperature**
  -20°C to +60°C (-4F - +140F)

What if I lose my TREZOR?
-------------------------

TREZOR comes with excelent support for so called paper wallets.  When you set up your TREZOR for the first time, you will be told a list of secret words to write down.  Once you have written down this list, you can recover your Bitcoins at any time using a replacement TREZOR.

How is TREZOR different from a USB flash drive?
-----------------------------------------------

A USB flash drive is just storage for private keys. It means that when you want to make a transaction, you must attach your drive to the computer and let your bitcoin software read the keys from the device. At this point your private keys are accessible to viruses and malware, just as to any other software on your desktop computer.

On the contrary, TREZOR is a single-purpose computer, which stores your private keys and actively signs transactions without sending your private keys to the computer. When you want to make a bitcoin transaction, your bitcoin software just sends a transaction template to the TREZOR device and asks for a digital signature. TREZOR shows the requested amount and target address on its display. You will then confirm the transaction by pressing the hardware button. TREZOR will sign transaction internally and send the digital signature back to the computer, without leaking your private keys. Thanks to this, you can use TREZOR even on a vulnerable or hacked computer.

How is TREZOR different from an encrypted wallet?
-------------------------------------------------

Even using a strong password doesn't prevent viruses to silently sit on your computer and wait until you want to transfer coins out of your wallet. This is a vulnerable point, because a virus has access to the wallet file and can read your passphrase from your keyboard.

On the contrary, TREZOR never sends private keys to the computer, because when you want to send some coins out of your wallet, TREZOR asks bitcoin software for payment details, signs the transaction internally and then sends back just a digital signature of the transaction. There's no point where malware on your computer could access the private keys or send away your coins without your permission.

What is the difference between TREZOR and Yubikey?
--------------------------------------------------
There is a significant difference between the two. The Yubikey is a device which helps the service to verify that it is actually you who is signing the transaction. However, it does not protect you against signing a different transaction than you intend to.

What is the difference between using TREZOR and a paper backup of my keys?
--------------------------------------------------------------------------

A paper backup is a quite safe method to protect bitcoins, but you still need to load private keys from paper using a trusted computer to send your coins to somebody else.

Sales & Marketing
=================

Where can I get some press information, photos and logos?
---------------------------------------------------------

Please, talk to Alena at info@bitcointrezor.com

I am a significant regional or local player, can I resell TREZOR?
-----------------------------------------------------------------

Yes, please contact Alena at info@bitcointrezor.com.

I run a bitcoin site or service; can I earn bitcoins with TREZOR?
-----------------------------------------------------------------

Yes, we would like our supporters and TREZOR owners to be able to participate on our success. That's why we are preparing an affiliate program. Please `subscribe to our newsletter <http://www.bitcointrezor.com/>`_ and we'll inform you when it's ready.

Developer's Corner
==================

I want to participate on implementing TREZOR with my wallet or service.
-----------------------------------------------------------------------

We will be happy talking to you, please contact us at info@bitcointrezor.com.

Is it possible to flash the device?
-----------------------------------

Yes, it is. Devices sold by us have an USB bootloader that allows firmware flashing. Upon start the firmware signature is checked and if it does not match ours a warning is issued. User can continue on his own risk after pressing the button. This small inconvenience is to increase the security of the end users.

Where can I find the source code?
---------------------------------

Some of the sources are at `Github <http://github.com/trezor/>`_. We are in the process of finalizing and cleaning up the sources and preparing a security audit of the code. We will publish the sources before shipping TREZOR to our customers. We will notify our `newsletter subscribers <http://www.bitcointrezor.com/>`_ once this is done.