# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/server_events/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/__init__.py
from gui.server_events.EventsCache import EventsCache as _EventsCache
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.battle_matters import IBattleMattersController
__all__ = ('getServerEventsConfig', 'getBattleMattersController')

def getServerEventsConfig(manager):
    cache = _EventsCache()
    cache.init()
    manager.addInstance(IEventsCache, cache, finalizer='fini')


def getBattleMattersController(manager):
    from gui.game_control.battle_matters_controller import BattleMattersController
    controller = BattleMattersController()
    controller.init()
    manager.addInstance(IBattleMattersController, controller, finalizer='fini')
