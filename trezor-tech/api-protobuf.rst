Low level protobuf API
--------------------

TREZOR communicates using a simple request-response model.
Messages are exchanged always in a purely synchronous fashion over `USB HID <https://en.wikipedia.org/wiki/USB_HID>`_.
These messages are serialized into binary format using `Protocol Buffers <https://en.wikipedia.org/wiki/Protocol_Buffers>`_.

Message definitions are stored in the `trezor-common <https://github.com/trezor/trezor-common/tree/master/protob>`_ repository.
File ``messages.proto`` describes messages and file ``types.proto`` described data structures used inside of the messages.


