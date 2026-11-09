# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/hangar/dialogs/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/hangar/dialogs/__init__.py
from __future__ import absolute_import
from BWUtil import AsyncReturn
from gui.impl.dialogs import dialogs
from gui.impl.lobby.dialogs.full_screen_param_dialog_view import FullScreenParamDialogView
from wg_async import wg_async, wg_await

@wg_async
def showTypeParamConfirmDialog(layoutID, dialogType, dialogParams, wrappedViewClass=None):
    result = yield wg_await(dialogs.showSingleDialogWithResultData(layoutID=layoutID, wrappedViewClass=wrappedViewClass or FullScreenParamDialogView, dialogLayoutID=layoutID, dialogType=dialogType, dialogParams=dialogParams))
    if result.busy:
        raise AsyncReturn((False, {}))
    raise AsyncReturn(result.result)
