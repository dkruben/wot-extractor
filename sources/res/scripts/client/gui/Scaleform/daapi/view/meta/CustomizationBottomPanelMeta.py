# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/CustomizationBottomPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationBottomPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CustomizationBottomPanelMeta(BaseDAAPIComponent):

    def resetFilter(self):
        self._printOverrideError('resetFilter')

    def showBuyWindow(self):
        self._printOverrideError('showBuyWindow')

    def refreshFilterData(self):
        self._printOverrideError('refreshFilterData')

    def onSelectItem(self, index, intCD, progressionLevel):
        self._printOverrideError('onSelectItem')

    def onEditItem(self, intCD):
        self._printOverrideError('onEditItem')

    def showGroupFromTab(self, groupId):
        self._printOverrideError('showGroupFromTab')

    def onSelectHotFilter(self, index, value):
        self._printOverrideError('onSelectHotFilter')

    def switchMode(self, index):
        self._printOverrideError('switchMode')

    def onItemIsNewAnimationShown(self, intCD):
        self._printOverrideError('onItemIsNewAnimationShown')

    def showVideo(self):
        self._printOverrideError('showVideo')

    def showVehiclesSideBar(self):
        self._printOverrideError('showVehiclesSideBar')

    def as_showBillS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showBill()

    def as_hideBillS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBill()

    def as_setBottomPanelInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanelInitData(data)

    def as_setBottomPanelTabsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanelTabsData(data)

    def as_setCarouselDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselData(data)

    def as_setCarouselInfoLabelDataS(self, text, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselInfoLabelData(text, tooltip)

    def as_setFilterDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setFilterData(data)

    def as_setBottomPanelPriceStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanelPriceState(data)

    def as_setCarouselFiltersDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselFiltersData(data)

    def as_setProjectionDecalHintVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setProjectionDecalHintVisibility(value)

    def as_showPopoverBtnS(self, alias, src, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_showPopoverBtn(alias, src, tooltip)

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()

    def as_setItemsPopoverBtnEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setItemsPopoverBtnEnabled(value)

    def as_setNotificationCountersS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNotificationCounters(data)

    def as_scrollToSlotS(self, intCD, immediately=False):
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToSlot(intCD, immediately)

    def as_playFilterBlinkS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_playFilterBlink()

    def as_updateEscHelpMessageS(self, visibility):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEscHelpMessage(visibility)

    def as_setFilterFallbackDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setFilterFallbackData(data)

    def as_setStageSwitcherVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setStageSwitcherVisibility(value)

    def as_setVehiclesSidebarBtnVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesSidebarBtnVisibility(value)
