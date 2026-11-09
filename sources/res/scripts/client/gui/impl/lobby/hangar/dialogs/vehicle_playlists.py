# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/hangar/dialogs/vehicle_playlists.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/hangar/dialogs/vehicle_playlists.py
from __future__ import absolute_import
from BWUtil import AsyncReturn
from gui.impl.gen import R
from gui.impl.lobby.hangar.dialogs import showTypeParamConfirmDialog
from wg_async import wg_async, wg_await
EMPTY_DIALOG_PARAMS = '{}'

class VehPlaylistsDialogType(object):
    IMPORT = 'import'
    DELETE = 'delete'
    SAVE_BEFORE_LEAVE = 'save'


@wg_async
def showTypeParamPlaylistDialog(dialogType, dialogParams):
    result = yield wg_await(showTypeParamConfirmDialog(layoutID=R.views.mono.hangar.overlays.playlist(), dialogType=dialogType, dialogParams=dialogParams))
    raise AsyncReturn(result)


@wg_async
def showSaveBeforeLeavePlaylistDialog(dialogParams=None):
    result = yield wg_await(showTypeParamPlaylistDialog(VehPlaylistsDialogType.SAVE_BEFORE_LEAVE, dialogParams or EMPTY_DIALOG_PARAMS))
    raise AsyncReturn(result)
