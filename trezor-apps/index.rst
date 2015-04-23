TREZOR Apps
===========

.. image:: images/chapter02.jpg

Our TREZOR device is supported by multiple **client wallets and online services**. We call them **TREZOR Apps**. Find more information about them below.

Wallets supporting TREZOR
-------------------------

The following table summarizes TREZOR features supported in various client wallets on different platforms. Click on the wallet name for detailed information.

==================================================== ======================== ====================== ====================== ====================== ======================= ====================== ====================== ====================== ====================== ====================== ====================== ======================
Supported TREZOR features
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Wallet                                               :icon:`cog`              :icon:`life-ring`      :icon:`exchange`       :icon:`users`          :icon:`user-secret`     :icon:`bars`           :icon:`th`             :icon:`eye-slash`      :icon:`eye`            :icon:`upload`         :icon:`fire`           :icon:`lock`
`Coinprism <coinprism.html>`_                                                                        ✔                                             ✔                                              ✔
`Electrum <electrum.html>`_                          ✔                                               ✔                                             ✔                       ✔                      ✔                      ✔
`Encompass <encompass.html>`_                        ✔                                               ✔                                             ✔                       ✔                      ✔                      ✔
`MultiBit HD <multibit.html>`_                       ✔                                               ✔                                   	                                                      ✔                      ✔                                                                    ✔                      ✔
`Mycelium <mycelium.html>`_                                                                          ✔                                             ✔                       ✔                      ✔                      ✔
`myTREZOR <mytrezor.html>`_                          ✔                        ✔                      ✔                                             ✔                       ✔                      ✔                      ✔                      ✔                      ✔                      ✔
`myTREZOR Lite <mytrezor-lite.html>`_                                                                                                                                                                                    ✔
==================================================== ======================== ====================== ====================== ====================== ======================= ====================== ====================== ====================== ====================== ====================== ====================== ======================

LEGEND | 
:icon:`cog` Basic Setup | 
:icon:`life-ring` Safe Recovery | 
:icon:`exchange` Simple transactions | 
:icon:`users` Multisig transactions | 
:icon:`user-secret` Hidden Wallets | 
:icon:`bars` Multiple Accounts | 
:icon:`th` Smart PIN Matrix |
:icon:`eye-slash` Watch-only mode | 
:icon:`eye` Show on TREZOR | 
:icon:`upload` Update Firmware | 
:icon:`fire` Wipe device | 
:icon:`lock` `Sign in with TREZOR <../trezor-tech/api-connect.html>`_

Wallets supporting Seed Recovery
--------------------------------

The following wallets allow you to access your funds using the recovery seed in case your TREZOR device gets lost, is damaged or stolen:
 
- `Electrum <https://electrum.org/#download>`_ (Linux, Windows, OSX, Android)
- `Encompass <https://maza.club/encompass>`_ (Linux, Windows, Android)
- `MultiBit HD <https://beta.multibit.org>`_ (Linux, Windows, OSX)
- Mycelium (iOS)
- `Mycelium <https://play.google.com/store/apps/details?id=com.mycelium.wallet>`_ (Android)
- `Wallet32 <https://play.google.com/store/apps/details?id=com.bonsai.wallet32>`_ (Android)


Services supporting TREZOR
--------------------------

TREZOR device is also supported by various online services like exchanges, payment processors, mining pools and others. Most common supoprted feature is passwordless login through Sign in with TREZOR. Click on a name of service for more details.

==================================================== ===================================== ==============================================================================================
Service                                              Feature(s)                            Description
`Coinpayments <coinpayments.html>`_                  :icon:`lock`                          Payment processor service supporting various cryptocurrencies.
`Coinsimple <coinsimple.html>`_                      :icon:`eye-slash`                     Bitcoin invoicing service and wallet connector.
==================================================== ===================================== ==============================================================================================

.. `Slush pool <slush-pool.html>`_                      :icon:`lock`                          The first mining pool ever and inventor of mining concept.

LEGEND | 
:icon:`lock` `Sign in with TREZOR <../trezor-tech/api-connect.html>`_ | 
:icon:`eye-slash` Watch-only mode

Ongoing integrations
--------------------

If you actively working on TREZOR support or planing to support it, please let us know more details at integration@satoshilabs.com. 
We will gladly include you in the following list of **wallets and services with future TREZOR support**.

- `Armory <https://bitcoinarmory.com>`_ - wallet support planned
- `Bitstamp <https://www.bitstamp.net>`_  - `Sign in with TREZOR <../trezor-tech/api-connect.html>`_ planned
- `Coinkite <https://coinkite.com>`_ - wallet support planned
- `Coinmap <http://coinmap.org>`_ - `Sign in with TREZOR <../trezor-tech/api-connect.html>`_ work in progress
- `Coinsimple <coinsimple.html>`_  - `Sign in with TREZOR <../trezor-tech/api-connect.html>`_ work in progress
- `Copay <https://copay.io>`_ - multisig wallet support planned
- `GreenAddress <https://greenaddress.it/>`_ - multisig wallet support work in progress
- `Slush pool <http://mining.bitcoin.cz/home/>`_ - `Sign in with TREZOR <../trezor-tech/api-connect.html>`_ work in progress

.. `Bitstock <https://www.bitstock.com>`_               TREZOR Connect support planned

License
-------

The contents of this documentation are licensed under Creative Commons `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_ license.

Contributing
------------

The project is hosted `on GitHub <https://github.com/satoshilabs/docs>`_ and pull requests are welcome!

.. toctree::
   :hidden:
   :maxdepth: 1
   
   coinpayments 
   coinprism 
   coinsimple 
   electrum 
   encompass 
   multibit 
   mycelium 
   mytrezor 
   mytrezor-lite
