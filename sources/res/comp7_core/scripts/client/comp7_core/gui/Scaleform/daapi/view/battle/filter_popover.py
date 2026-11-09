# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/filter_popover.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/filter_popover.py
from __future__ import absolute_import
from account_helpers import AccountSettings
from account_helpers.AccountSettings import COMP7_PREBATTLE_CAROUSEL_ROW_VALUE
from comp7_core.gui.Scaleform.daapi.view.battle.common import getSavedRowCountValue, rowValueToRowCount, rowCountToRowValue
from gui.Scaleform.daapi.view.common.common_constants import FILTER_POPOVER_SECTION
from gui.Scaleform.daapi.view.common.filter_popover import TankCarouselFilterPopover
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles

class Comp7TankCarouselFilterPopover(TankCarouselFilterPopover):

    def switchCarouselType(self, selected):
        self._carouselRowCount = 1 if selected else 0
        self.__saveRowCountValue()
        self._carousel.setRowCount(rowValueToRowCount(self._carouselRowCount))

    def _populate(self):
        super(Comp7TankCarouselFilterPopover, self)._populate()
        self.app.enterGuiControlMode(BATTLE_VIEW_ALIASES.COMP7_TANK_CAROUSEL_FILTER_POPOVER, enableAiming=False)

    def _dispose(self):
        self.app.leaveGuiControlMode(BATTLE_VIEW_ALIASES.COMP7_TANK_CAROUSEL_FILTER_POPOVER)
        super(Comp7TankCarouselFilterPopover, self)._dispose()

    def _readRowCount(self, ctx):
        savedRowValue, isSavedByPlayer = getSavedRowCountValue()
        if isSavedByPlayer:
            self._carouselRowCount = savedRowValue
        elif ctx and 'data' in ctx:
            data = ctx['data']
            self._carouselRowCount = rowCountToRowValue(getattr(data, 'rowCount', 1))

    def _saveRowCount(self):
        savedRowValue, isSavedByPlayer = getSavedRowCountValue()
        if isSavedByPlayer and savedRowValue != self._carouselRowCount:
            self.__saveRowCountValue()

    def _getInitialVO(self, filters, xpRateMultiplier):
        dataVO = super(Comp7TankCarouselFilterPopover, self)._getInitialVO(filters, xpRateMultiplier)
        dataVO['specialSectionVisible'] = True
        dataVO['searchSectionVisible'] = True
        dataVO['progressionsSectionVisible'] = False
        dataVO['additionalInfo'] = text_styles.stats(backport.text(R.strings.comp7_ext.battleCarousel.filterPopover.desc()))
        vehicleLevels = self._carousel.getCustomParams().get('vehicleLevelsFilter', [])
        if self._carousel is not None and not len(vehicleLevels) > 1:
            dataVO['tankTierSectionVisible'] = False
        return dataVO

    def _generateMapping(self, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        mapping = super(Comp7TankCarouselFilterPopover, self)._generateMapping(hasRented, hasEvent, hasRoles, hasCustomization, **kwargs)
        mapping[FILTER_POPOVER_SECTION.SPECIALS] = [
         'rented', 'favorite']
        vehicleLevels = kwargs.get('vehicleLevelsFilter', [])
        if len(vehicleLevels) > 1:
            mapping[FILTER_POPOVER_SECTION.LEVELS] = [('level_{}').format(lvl) for lvl in vehicleLevels]
        else:
            mapping[FILTER_POPOVER_SECTION.LEVELS] = []
        return mapping

    def __saveRowCountValue(self):
        AccountSettings.setSettings(COMP7_PREBATTLE_CAROUSEL_ROW_VALUE, self._carouselRowCount)
