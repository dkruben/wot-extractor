# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/alert_message_block.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/alert_message_block.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.AlertMessageBlockMeta import AlertMessageBlockMeta

class AlertMessageBlock(AlertMessageBlockMeta):

    def __init__(self):
        super(AlertMessageBlock, self).__init__()
        self.__onBtnClickCallback = None
        self.__onBlockClickCallback = None
        return

    def update(self, alertMsgData, callbacks=None):
        callbacks = callbacks or {}
        self.__onBtnClickCallback = callbacks.get('onButtonClick')
        self.__onBlockClickCallback = callbacks.get('onBlockClick')
        self.as_setDataS(alertMsgData)

    def onBlockClick(self):
        if self.__onBlockClickCallback:
            self.__onBlockClickCallback()

    def onButtonClick(self):
        if self.__onBtnClickCallback:
            self.__onBtnClickCallback()

    def _dispose(self):
        super(AlertMessageBlock, self)._dispose()
        self.__onBtnClickCallback = None
        self.__onBlockClickCallback = None
        return
