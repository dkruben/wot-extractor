# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/VehiclePreviewBottomPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePreviewBottomPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehiclePreviewBottomPanelMeta(BaseDAAPIComponent):

    def onBuyOrResearchClick(self):
        self._printOverrideError('onBuyOrResearchClick')

    def onCarouselVehicleSelected(self, intCD):
        self._printOverrideError('onCarouselVehicleSelected')

    def onOfferSelected(self, offerID):
        self._printOverrideError('onOfferSelected')

    def showTooltip(self, intCD, itemType):
        self._printOverrideError('showTooltip')

    def updateData(self, useCompactData):
        self._printOverrideError('updateData')

    def onCouponSelected(self, isActive):
        self._printOverrideError('onCouponSelected')

    def as_setBuyDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuyData(data)

    def as_setSetItemsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSetItemsData(data)

    def as_setCouponS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoupon(data)

    def as_setSetVehiclesDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSetVehiclesData(data)

    def as_setOffersDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setOffersData(data)

    def as_setSetTitleTooltipS(self, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setSetTitleTooltip(tooltip)

    def as_updateLeftTimeS(self, formattedTime, hasHoursAndMinutes=False):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLeftTime(formattedTime, hasHoursAndMinutes)
