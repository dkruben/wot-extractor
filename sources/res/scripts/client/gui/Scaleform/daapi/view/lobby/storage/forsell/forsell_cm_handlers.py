# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/forsell/forsell_cm_handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/storage/forsell/forsell_cm_handlers.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import option, CMLabel, ContextMenu
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.shared import EVENT_BUS_SCOPE, events
from gui.shared import event_dispatcher as shared_events
from ids_generators import SequenceIDGenerator
from gui.shared.event_dispatcher import showSellDialog

class ForSellCMHandler(ContextMenu, EventSystemEntity):
    __sqGen = SequenceIDGenerator()

    @option(__sqGen.nextSequenceID, CMLabel.INFORMATION)
    def showInfo(self):
        shared_events.showStorageModuleInfo(self._id)

    @option(__sqGen.nextSequenceID, CMLabel.SELL)
    def sell(self):
        showSellDialog(self._id)

    @option(__sqGen.nextSequenceID, CMLabel.SALE_OPTION)
    def switchSaleOption(self):
        self.fireEvent(events.StorageEvent(events.StorageEvent.SELECT_MODULE_FOR_SELL, ctx={'intCD': (self._id)}), scope=EVENT_BUS_SCOPE.LOBBY)

    def _getOptionCustomData(self, label):
        optionData = super(ForSellCMHandler, self)._getOptionCustomData(label)
        if label == CMLabel.SALE_OPTION:
            optionData.label = 'prohibitSale' if self._selected else 'allowSale'
        return optionData

    def _initFlashValues(self, ctx):
        super(ForSellCMHandler, self)._initFlashValues(ctx)
        self._selected = ctx.selected
