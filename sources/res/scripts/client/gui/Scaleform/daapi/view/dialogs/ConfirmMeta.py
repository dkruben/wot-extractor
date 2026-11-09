# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/ConfirmMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/ConfirmMeta.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.dialogs import IDialogMeta
from gui.Scaleform.framework import ScopeTemplates
from gui.shared import events
from helpers import i18n

class ConfirmMeta(IDialogMeta):

    def __init__(self, title, description, submitBtn, cancelBtn, checkBox, selected=False):
        self.__title = title
        self.__description = description
        self.__submitLabel = submitBtn
        self.__cancelLabel = cancelBtn
        self.__checkBoxLabel = checkBox
        self.__checkBoxSelected = selected

    def destroy(self):
        pass

    def getEventType(self):
        return events.ShowDialogEvent.SHOW_CONFIRM_DIALOG

    def getTitle(self):
        return i18n.makeString(self.__title)

    def getDescription(self):
        return i18n.makeString(self.__description)

    def getSubmitButtonLabel(self):
        return i18n.makeString(self.__submitLabel)

    def getCancelButtonLabel(self):
        return i18n.makeString(self.__cancelLabel)

    def getCheckBoxButtonLabel(self):
        return i18n.makeString(self.__checkBoxLabel)

    def getCheckBoxSelected(self):
        return self.__checkBoxSelected

    def getViewScopeType(self):
        return ScopeTemplates.DYNAMIC_SCOPE
