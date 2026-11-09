# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/shared/events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/shared/events.py
from __future__ import absolute_import
from gui.shared.event_bus import SharedEvent
from gui.shared.events import HasCtxEvent

class HWHangarEvent(SharedEvent):
    REFRESH = 'hwHangarEvent/refresh'


class HWBattleLootEvent(HasCtxEvent):
    VEH_CAPTURING_START = 'HWBattleLootEvent/VEH_CAPTURING_START'
    VEH_CAPTURING_CANCEL = 'HWBattleLootEvent/VEH_CAPTURING_CANCEL'
    APPEAR = 'HWBattleLootEvent/APPEAR'
    CAPTURED = 'HWBattleLootEvent/CAPTURED'
