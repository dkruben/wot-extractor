# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/app_loader/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/app_loader/__init__.py
from gui.app_loader import settings, decorators
from gui.app_loader.decorators import app_getter, def_lobby, def_battle, sf_lobby, sf_battle
__all__ = ('getAppLoaderConfig', 'decorators', 'settings', 'app_getter', 'def_lobby',
           'def_battle', 'sf_lobby', 'sf_battle')

def getAppLoaderConfig(manager):
    from gui.app_loader.loader import AppLoader
    from skeletons.gui.app_loader import IAppLoader
    manager.addInstance(IAppLoader, AppLoader(), finalizer='fini')
