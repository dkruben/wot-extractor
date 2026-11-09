# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/missions_dialogs_meta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/missions_dialogs_meta.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.dialogs import IDialogMeta
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS
from gui.server_events.events_helpers import AwardSheetPresenter
from gui.shared import events
from helpers.i18n import makeString as _ms

class UseAwardSheetDialogMeta(IDialogMeta):

    def __init__(self, quest, freeSheets):
        self.__quest = quest
        self.__freeSheets = freeSheets
        self.__title = PERSONAL_MISSIONS.USEAWARDSHEETWINDOW_TITLE
        self.__submitLabel = PERSONAL_MISSIONS.USEAWARDSHEETWINDOW_SUBMITBTN
        self.__cancelLabel = PERSONAL_MISSIONS.USEAWARDSHEETWINDOW_CANCELBTN

    def getQuest(self):
        return self.__quest

    def getEventType(self):
        return events.ShowDialogEvent.SHOW_USE_AWARD_SHEET_DIALOG

    def getTitle(self):
        return _ms(self.__title)

    def getSubmitButtonLabel(self):
        return _ms(self.__submitLabel)

    def getCancelButtonLabel(self):
        return _ms(self.__cancelLabel)

    def getViewScopeType(self):
        return ScopeTemplates.DEFAULT_SCOPE

    def getTotalText(self):
        return _ms(PERSONAL_MISSIONS.USEAWARDSHEETWINDOW_SHEETSTOTAL)

    def getNeededText(self):
        return _ms(PERSONAL_MISSIONS.USEAWARDSHEETWINDOW_NEEDAMOUNT)

    def getIcon(self):
        return AwardSheetPresenter.getIcon(AwardSheetPresenter.Size.BIG)

    def isAvailable(self):
        return self.__quest.isUnlocked() and self.__quest.hasRequiredVehicles()

    def getInfoText(self):
        return _ms(PERSONAL_MISSIONS.USEAWARDSHEETWINDOW_INFO)

    def getWarningText(self):
        if not self.__quest.hasRequiredVehicles():
            classifier = self.__quest.getQuestClassifier().classificationAttr
            return _ms(PERSONAL_MISSIONS.sheetNoVehicleWarning(self.__quest.getQuestBranchName()), vehicleClass=_ms('#menu:classes/short/' + classifier))
        if not self.__quest.isUnlocked():
            return _ms(PERSONAL_MISSIONS.USEAWARDSHEETWINDOW_LOCKED)
        return ''

    def getFreeSheets(self):
        return self.__freeSheets

    def getPawnCost(self):
        return self.__quest.getPawnCost()
