# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/proto/xmpp/extensions/ping.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/xmpp/extensions/ping.py
from __future__ import absolute_import
from messenger.proto.xmpp.extensions import PyQuery, PyExtension
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.gloox_constants import IQ_TYPE

class PingExtension(PyExtension):

    def __init__(self):
        super(PingExtension, self).__init__(_TAG.PING)
        self.setXmlNs(_NS.PING)


class PingQuery(PyQuery):

    def __init__(self, to):
        super(PingQuery, self).__init__(IQ_TYPE.GET, PingExtension(), to)
