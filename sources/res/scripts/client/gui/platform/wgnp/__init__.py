# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/platform/wgnp/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/wgnp/__init__.py
import typing
from gui.platform.wgnp.steam_account.controller import WGNPSteamAccRequestController
from gui.platform.wgnp.demo_account.controller import WGNPDemoAccRequestController
from gui.platform.wgnp.general.controller import WGNPGeneralRequestController
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController, IWGNPDemoAccRequestController, IWGNPGeneralRequestController
if typing.TYPE_CHECKING:
    from helpers.dependency import DependencyManager
__all__ = ('getWGNPRequestControllers', )

def getWGNPRequestControllers(manager):
    wgnpSteamAccController = WGNPSteamAccRequestController()
    wgnpSteamAccController.init()
    manager.addInstance(IWGNPSteamAccRequestController, wgnpSteamAccController, finalizer='fini')
    wgnpDemoAccController = WGNPDemoAccRequestController()
    wgnpDemoAccController.init()
    manager.addInstance(IWGNPDemoAccRequestController, wgnpDemoAccController, finalizer='fini')
    wgnpGeneralController = WGNPGeneralRequestController()
    wgnpGeneralController.init()
    manager.addInstance(IWGNPGeneralRequestController, wgnpGeneralController, finalizer='fini')
