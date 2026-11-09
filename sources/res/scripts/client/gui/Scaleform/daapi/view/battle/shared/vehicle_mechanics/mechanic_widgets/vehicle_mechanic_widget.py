# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/vehicle_mechanic_widget.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/vehicle_mechanic_widget.py
from __future__ import absolute_import
import typing
from collections import namedtuple
from itertools import chain
from gui.Scaleform.daapi.view.meta.BaseVehicleMechanicsWidgetMeta import BaseVehicleMechanicsWidgetMeta
from gui.shared.utils.key_mapping import getScaleformKey
from gui.veh_mechanics.battle.updaters.hotkey_updaters import IHotKeysView
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import IMechanicPassengerView
if typing.TYPE_CHECKING:
    from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeyCommand
HotKeyData = namedtuple('HotKeyData', ['command', 'isLong'])

class VehicleMechanicWidget(BaseVehicleMechanicsWidgetMeta, IHotKeysView, IMechanicPassengerView):
    _HOT_KEY_MAP = {}

    def setCrosshairType(self, crosshairType):
        self.as_setCrosshairTypeS(crosshairType)

    def setHotkeys(self, hotKeyCommands):
        self.as_setHotKeysS(tuple(chain.from_iterable([[{'keyCode': (getScaleformKey(hotKeyCommand.key)), 'command': (data.command), 'isLong': (data.isLong)} for data in self._HOT_KEY_MAP.get(hotKeyCommand.command, ())] for hotKeyCommand in hotKeyCommands])))

    def setVisibleForPassenger(self, visibleForPassenger):
        self.as_setVisibleS(visibleForPassenger)
