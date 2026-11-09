# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgnc/client.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgnc/client.py
from gui.wgnc.settings import WGNC_GUI_TYPE

class ClosePollWindowFromPopUp(object):
    __slots__ = ('_target', )

    def __init__(self, target):
        super(ClosePollWindowFromPopUp, self).__init__()
        self._target = target

    def process(self, actor, notID, actions, items):
        if actor.getType() != WGNC_GUI_TYPE.POP_UP:
            return
        submit = actor.getSubmitButton()
        if not submit:
            return
        if submit.action != actions:
            return
        item = items.getItemByName(self._target)
        if item:
            item.close(notID)


class ClientLogic(object):
    __slots__ = ('_seq', )

    def __init__(self, seq):
        super(ClientLogic, self).__init__()
        self._seq = seq

    def process(self, actor, notID, actions, items):
        for logic in self._seq:
            logic.process(actor, notID, actions, items)
