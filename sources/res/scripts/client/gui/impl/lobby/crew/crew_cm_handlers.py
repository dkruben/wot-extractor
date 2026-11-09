# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/crew_cm_handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/crew_cm_handlers.py
from gui.impl.lobby.crew.widget.crew_widget_cm_handlers import CrewContextMenuHandler, CREW
from helpers import dependency
from skeletons.gui.shared import IItemsCache
VISIBLE_OPTIONS = (
 CREW.PERSONAL_FILE,
 CREW.DISMISS,
 CREW.QUICK_TRAINING,
 CREW.SEND_TO_BARRACKS)

class CrewTankmanContextMenuHandler(CrewContextMenuHandler):
    itemsCache = dependency.descriptor(IItemsCache)

    def _generateOptions(self, ctx=None):
        options = super(CrewTankmanContextMenuHandler, self)._generateOptions(ctx)
        return [option for option in options if option.get('id') in VISIBLE_OPTIONS]

    def _initFlashValues(self, ctx):
        tankmanID = int(ctx.tankmanID)
        self._slotIdx = int(ctx.slotIdx)
        self._tankmanID = tankmanID
        self._tankman = self.itemsCache.items.getTankman(tankmanID)
        self._vehicle = self.itemsCache.items.getVehicle(self._tankman.vehicleInvID)
        self._previousViewID = None
        return
