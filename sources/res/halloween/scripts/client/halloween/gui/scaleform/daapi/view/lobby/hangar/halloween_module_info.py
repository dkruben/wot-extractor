# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/lobby/hangar/halloween_module_info.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/lobby/hangar/halloween_module_info.py
from __future__ import absolute_import
from gui.Scaleform.framework.entities.View import View
from gui.Scaleform.locale.MENU import MENU
from gui.shared.tooltips import contexts
from halloween.gui.scaleform.daapi.view.tooltips.event import EventModuleBlockTooltipData
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache
from gui.Scaleform.daapi.view.lobby.ModuleInfoWindow import ModuleInfoWindow
from gui.impl import backport
from gui.impl.gen import R

class HalloweenModuleInfoWindow(ModuleInfoWindow):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx=None):
        super(HalloweenModuleInfoWindow, self).__init__(ctx=ctx)
        self.__vehicleDescr = ctx.get('vehicleDescr')

    def _populate(self):
        super(View, self)._populate()
        module = self.itemsCache.items.getItemByCD(self.moduleCompactDescr)
        tooltipArgs = [self.moduleCompactDescr, self.__vehicleDescr]
        dataProvider = EventModuleBlockTooltipData(context=contexts.ModuleInfoContext())
        data = dataProvider.buildToolTip(*tooltipArgs)
        titleArr = [backport.text(R.strings.tank_setup.menu.hw_equipment.title()),
         module.shortUserName, _ms(MENU.MODULEINFO_TITLE)]
        data['windowTitle'] = (' ').join(titleArr)
        data['overlayType'] = module.getOverlayType()
        data['highlightType'] = module.getBigHighlightType()
        self._updateModuleInfo(data)
