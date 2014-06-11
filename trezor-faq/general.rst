General Information
===================

What is TREZOR?
---------------

TREZOR is a single purpose computer which signs Bitcoin transactions made through a desktop or web-wallet. It makes transactions completely safe even on a compromised or vulnerable computer. TREZOR provides the highest possible security for all Bitcoin and Litecoin users, even the non-technically savvy ones. Because the use of TREZOR is very easy and intuitive we believe it will help Bitcoin being adopted by common people.

How does TREZOR work?
---------------------

The mechanism of making transactions with TREZOR is simple as this:
1. Connect the device into the USB and run your wallet software.
2. The device is automatically recognized by your computer as a new USB device.
3. Once the wallet software asks for the master public key, it will show your addresses and their balances.
4. When you want to send some coins, your wallet software creates a template of the transaction and sends it to TREZOR.
5. TREZOR displays a transaction summary and asks you to confirm the transaction by pressing the confirmation button.
6. TREZOR signs the transaction using a private key stored in the device and sends a signed transaction to the wallet software.
7. The desktop software then sends the signed transaction to the Bitcoin network.

How do I connect TREZOR to my computer?
---------------------------------------

TREZOR acts like an USB HID device which connects to your computer via a micro USB cable (like a keyboard or a mouse). You won't need to install any drivers; everything you'll need is a Bitcoin wallet (like Multibit, Electrum etc.) capable to communicate with the device.

What happens when I use TREZOR for the first time?
--------------------------------------------------

When running TREZOR for the first time, a master private key is generated and written on a display in a form of 12, 18 or 24 words, depending on the protection strength you choose. It is recommended to write these words down and/or memorize them in order to be able to restore your TREZOR in case it's lost or stolen.

Do I have to install any drivers to my computer before using TREZOR?
--------------------------------------------------------------------

If using TREZOR with a desktop client, you won’t need to install any drivers. TREZOR is a Plug & Play device so everything you'll need is to have desktop Bitcoin wallet (like Multibit or Electrum) capable to talk with the device

In case you want to use TREZOR with a web wallet, you will be asked to install a simple web plugin for your browser (Firefox, Chrome or IE). The installation is a fast and easy process.

How does TREZOR keep my bitcoins safe if I connect it to a compromised computer?
--------------------------------------------------------------------------------

The private keys never leave the device and the malware cannot read the private keys from TREZOR. This is thanks to the wire protocol between TREZOR and the computer, which does only transfer unsigned transactions to the device and signed ones out of the device. Also, we have implemented a safe way of entering PIN, so no keylogger can be used to spy on your PIN.

How many different keys can TREZOR hold?
----------------------------------------

TREZOR uses a deterministic wallet structure which means it can hold an unlimited number of keys. Check out more information on `BIP-0032 <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`_.

Is it possible to reset/wipe the device?
----------------------------------------

Yes, it is. This is especially useful if you want to pass your TREZOR device on to someone else. You can do so by wiping the device in the TREZOR Settings. By doing so, all sensitive user data will be erased. After that you can continue with a new Setup of the device (a completely new security key is generated and the old one is definitively lost) or you can restore it to previous setting with your paper backup.
