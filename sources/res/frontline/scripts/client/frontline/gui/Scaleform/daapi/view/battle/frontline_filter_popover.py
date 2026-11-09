# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_filter_popover.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_filter_popover.py
from __future__ import absolute_import
from frontline.gui.Scaleform.daapi.view.meta.FrontlineCarouselFilterPopoverMeta import FrontlineCarouselFilterPopoverMeta
from gui.filters.carousel_filter import FILTER_KEYS
from gui.Scaleform.daapi.view.common.common_constants import FILTER_POPOVER_SECTION
from helpers import dependency
from skeletons.gui.game_control import IVehiclePlaylistsController

class FrontlineBattleTankCarouselFilterPopover(FrontlineCarouselFilterPopoverMeta):
    _BASE_SPECIALS_LIST = [
     FILTER_KEYS.FAVORITE, FILTER_KEYS.PREMIUM]
    __vehiclePlaylistsCtrl = dependency.descriptor(IVehiclePlaylistsController)

    def _getInitialVO(self, filters, xpRateMultiplier):
        dataVO = super(FrontlineBattleTankCarouselFilterPopover, self)._getInitialVO(filters, xpRateMultiplier)
        dataVO['specialSectionVisible'] = True
        dataVO['searchSectionVisible'] = True
        dataVO['progressionsSectionVisible'] = False
        vehicleLevels = self._carousel.getCustomParams().get('vehicleLevelsFilter', [])
        if self._carousel is not None and not len(vehicleLevels) > 1:
            dataVO['tankTierSectionVisible'] = False
        return dataVO

    def _generateMapping(self, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        mapping = super(FrontlineBattleTankCarouselFilterPopover, self)._generateMapping(hasRented, hasEvent, hasRoles, hasCustomization, **kwargs)
        vehicleLevels = kwargs.get('vehicleLevelsFilter', [])
        if len(vehicleLevels) > 1:
            mapping[FILTER_POPOVER_SECTION.LEVELS] = [('level_{}').format(lvl) for lvl in vehicleLevels]
        else:
            mapping[FILTER_POPOVER_SECTION.LEVELS] = []
        return mapping

    def onPlayListsChange(self, playListId):
        self.__vehiclePlaylistsCtrl.setSelectedID(playListId)
        self._carousel.sortVehicles(None)
        self._update()
        return

    def setTankCarousel(self, carousel):
        super(FrontlineBattleTankCarouselFilterPopover, self).setTankCarousel(carousel)
        self.as_updatePlayListsS(self._carousel.getVehiclePlayList())
