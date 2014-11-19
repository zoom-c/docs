Messages
========

Signing messages
----------------

Signing messages is used to prove ownership of the current wallet. Typically when you have your wallet address registered on exchange websites and protected with 2FA and you loose access to your 2FA. If you want to prove you are the owner of the current wallet, you can use signed message to do so.

In order to sign message, go to the account page in myTREZOR and press Sign & Verify in the right top corner.  You should see a payment page like this:

.. image:: images/signandverify_page.png

**1. Signing the message**

You can type in the message text into Message field, then copy&paste one of your **used** receiving addresses from one of your accounts in TREZOR into the Address field and press "Sign" button.

.. image:: images/signmessage.png

**2. Confirm the signature on your TREZOR**

Once you have press "Sign" button, you will be asked to confirm the signature.  Check the text of the message.  If the text is correct, press the right button on your TREZOR to confirm.  If it is wrong, press 'cancel'.  If it is wrong, it may mean that your computer has been infected with a virus and you can be happy that your bitcoins are safe in your TREZOR, and not already stolen.

.. image:: images/signmessageconfirmation.jpg

Once you have confirmed the signature on your TREZOR, the signature will appear on the screen:

.. image:: images/signmessagesigned.png


Verifying messages
------------------

In order to verify message, go to the account page in myTREZOR and press Sign & Verify in the right top corner.  You should see a payment page like this:

.. image:: images/signandverify_page.png

**1. Verifying the message**

You can copy&paste the signed message into Message field, then copy&paste specific address the message has been signed with into Address field, copy&paste the signature into Signature field and press "Verify" button.

.. image:: images/verifymessage.png

**2. Check the verification on TREZOR**

Once you have press "Verify" button and the message is trully signed with the specified address, TREZOR will show you text of the message on it's screen. If it was not signed with specified address you will get an error message on MyTREZOR page.

.. image:: images/verifymessageconfirmation.jpg

Once you have confirmed the verification on your TREZOR, the "Message verified" will apper on your screen:

.. image:: images/verifymessageverified.png
