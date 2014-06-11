Comparing TREZOR to ...
=======================

What is the difference between the two editions?
------------------------------------------------

Both editions have identical electronics and functionality. Thus the main difference is in the case material. The Classic TREZOR case is made of a durable reinforced plastic. The Metallic TREZOR is made from a polished aluminum.

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

There is a significant difference between the two. The Yubikey is a device which helps the service to verify that it is actually you who is signing the transaction. However, it does not protect you against signing a different transaction than you intent to.

What is the difference between using TREZOR and a paper backup of my keys?
--------------------------------------------------------------------------

A paper backup is a quite safe method to protect bitcoins, but you still need to load private keys from paper using a trusted computer to send your coins to somebody else.
