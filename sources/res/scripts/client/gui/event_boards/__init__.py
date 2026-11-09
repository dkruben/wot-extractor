# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/event_boards/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/event_boards/__init__.py
from skeletons.gui.event_boards_controllers import IEventBoardController
__all__ = ('getEventServicesConfig', )

def getEventServicesConfig(manager):
    from gui.event_boards.event_boards_controller import EventBoardsController
    ctrl = EventBoardsController()
    manager.addInstance(IEventBoardController, ctrl, finalizer='fini')
