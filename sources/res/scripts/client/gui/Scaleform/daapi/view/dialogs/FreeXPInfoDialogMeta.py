# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/FreeXPInfoDialogMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/FreeXPInfoDialogMeta.py
from __future__ import absolute_import
from gui import makeHtmlString
from gui.Scaleform.daapi.view.dialogs import IDialogMeta
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.locale.DIALOGS import DIALOGS
from helpers import i18n
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS

class FreeXPInfoBaseMeta(IDialogMeta):

    def getTitle(self):
        return ''

    def getSubmitLbl(self):
        return ''

    def getTextInfo(self):
        return ''

    def getViewScopeType(self):
        return ScopeTemplates.DEFAULT_SCOPE

    def getEventType(self):
        return VIEW_ALIAS.FREE_X_P_INFO_WINDOW


class FreeXPInfoMeta(FreeXPInfoBaseMeta):

    def getTitle(self):
        return i18n.makeString(DIALOGS.FREEXPINFO_TITLE)

    def getSubmitLbl(self):
        return i18n.makeString(DIALOGS.FREEXPINFO_SUBMITBTNLBL)

    def getTextInfo(self):
        text = {}
        msgFormatted = makeHtmlString('html_templates:lobby/dialogs', 'freeXPInfo', {})
        text['body'] = msgFormatted
        return text
