# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/login/login_modes/base_mode.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/login_modes/base_mode.py
from __future__ import absolute_import
import weakref
from helpers import dependency
from skeletons.gui.login_manager import ILoginManager

class INVALID_FIELDS(object):
    ALL_VALID = 0
    LOGIN_INVALID = 1
    PWD_INVALID = 2
    SERVER_INVALID = 4
    LOGIN_PWD_INVALID = LOGIN_INVALID | PWD_INVALID


class BaseMode(object):
    _loginManager = dependency.descriptor(ILoginManager)

    def __init__(self, view, fallbackMode=None):
        self._view = weakref.proxy(view)
        self._fallbackMode = fallbackMode

    def onPopulate(self):
        pass

    def destroy(self):
        self._view = None
        self._fallbackMode = None
        return

    @property
    def login(self):
        raise NotImplementedError

    def doLogin(self, *args):
        raise NotImplementedError

    def updateForm(self):
        raise NotImplementedError

    @property
    def rememberUser(self):
        return False

    @property
    def password(self):
        return ''

    @property
    def rememberPassVisible(self):
        return False

    @property
    def showRememberServerWarning(self):
        return False

    def setRememberPassword(self, *args):
        pass

    def isToken2(self):
        return False

    def resetToken(self):
        pass

    def doSocialLogin(self, *args):
        pass

    def changeAccount(self):
        pass

    def skipRejectionError(self, *args):
        return False
