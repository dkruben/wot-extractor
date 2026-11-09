# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/login/login_modes/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/login_modes/__init__.py
from __future__ import absolute_import
import typing
from gui import GUI_SETTINGS
from gui.Scaleform.daapi.view.login.login_modes.wgc_mode import WgcMode
from gui.Scaleform.daapi.view.login.login_modes.steam_mode import SteamMode
from gui.Scaleform.daapi.view.login.login_modes.credentials_mode import CredentialsMode
from gui.Scaleform.daapi.view.login.login_modes.social_mode import SocialMode
from helpers import dependency
from skeletons.gui.login_manager import ILoginManager
if typing.TYPE_CHECKING:
    from gui.Scaleform.daapi.view.login.login_modes.base_mode import BaseMode

@dependency.replace_none_kwargs(loginManager=ILoginManager)
def createLoginMode(view, loginManager=None):
    if loginManager.isWgcSteam:
        return SteamMode(view)
    mode = CredentialsMode(view)
    if GUI_SETTINGS.socialNetworkLogin['enabled']:
        mode = SocialMode(view, mode)
    if loginManager.wgcAvailable:
        mode = WgcMode(view, mode)
    return mode
