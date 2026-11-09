# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/processors/winback.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/processors/winback.py
from __future__ import absolute_import
import typing, BigWorld
from gui import SystemMessages
from gui.Scaleform.Waiting import Waiting
from gui.SystemMessages import SM_TYPE
from gui.impl import backport
from gui.impl.dialogs.dialogs import showSingleDialogWithResultData
from gui.impl.gen import R
from gui.shared.gui_items.processors import Processor, plugins
if typing.TYPE_CHECKING:
    from typing import Optional
    from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView
    from frameworks import wulf
_WINBACK_MESSAGES = R.strings.system_messages.winback

class WinbackTurnOffBattlesProcessor(Processor):

    def __init__(self, reason, dialog=None, parent=None):
        confirmators = None
        if dialog is not None:
            layoutID = R.views.mono.winback.winback_leave_mode_dialog_view()
            confirmators = [plugins.AsyncDialogConfirmator(showSingleDialogWithResultData, dialog, layoutID, parent)]
        super(WinbackTurnOffBattlesProcessor, self).__init__(confirmators)
        self.__reason = reason
        return

    def _request(self, callback):
        Waiting.show('updating')
        BigWorld.player().winback.turnOffBattles(self.__reason, (lambda code, errStr: self._response(code, callback, errStr=errStr)))

    def _successHandler(self, code, ctx=None):
        Waiting.hide('updating')
        return super(WinbackTurnOffBattlesProcessor, self)._successHandler(code, ctx)

    def _errorHandler(self, code, errStr='', ctx=None):
        Waiting.hide('updating')
        SystemMessages.pushMessage(text=backport.text(_WINBACK_MESSAGES.turnOffBattlesError()), type=SM_TYPE.ErrorSimple)
        return super(WinbackTurnOffBattlesProcessor, self)._errorHandler(code, errStr, ctx)
