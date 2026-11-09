# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/proto/xmpp/extensions/blocking_cmd.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/xmpp/extensions/blocking_cmd.py
from __future__ import absolute_import
from messenger.proto.xmpp.extensions import PyExtension, PyQuery
from messenger.proto.xmpp.extensions.contact_item import ContactItemExtension
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.shared_handlers import IQChildHandler
from messenger.proto.xmpp.gloox_constants import IQ_TYPE

def _createBlockListExt():
    return PyExtension(_TAG.BLOCK_LIST).setXmlNs(_NS.BLOCKING_CMD)


def _createBlockItemExt(jid=None):
    return PyExtension(_TAG.BLOCK_ITEM).setXmlNs(_NS.BLOCKING_CMD).setChild(ContactItemExtension(jid))


def _createUnblockItemExt(jid=None):
    return PyExtension(_TAG.UNBLOCK_ITEM).setXmlNs(_NS.BLOCKING_CMD).setChild(ContactItemExtension(jid))


class BlockListQuery(PyQuery):

    def __init__(self):
        super(BlockListQuery, self).__init__(IQ_TYPE.GET, _createBlockListExt())


class BlockListHandler(IQChildHandler):

    def __init__(self):
        super(BlockListHandler, self).__init__(_createBlockListExt().setChild(ContactItemExtension()))


class BlockItemQuery(PyQuery):

    def __init__(self, jid):
        super(BlockItemQuery, self).__init__(IQ_TYPE.SET, _createBlockItemExt(jid))


class BlockItemHandler(IQChildHandler):

    def __init__(self):
        super(BlockItemHandler, self).__init__(_createBlockItemExt())


class UnblockItemQuery(PyQuery):

    def __init__(self, jid):
        super(UnblockItemQuery, self).__init__(IQ_TYPE.SET, _createUnblockItemExt(jid))


class UnblockItemHandler(IQChildHandler):

    def __init__(self):
        super(UnblockItemHandler, self).__init__(_createUnblockItemExt())
