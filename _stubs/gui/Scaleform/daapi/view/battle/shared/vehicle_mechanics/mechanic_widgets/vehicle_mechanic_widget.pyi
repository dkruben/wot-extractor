# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/vehicle_mechanic_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from itertools import chain as chain
from gui.Scaleform.daapi.view.meta.BaseVehicleMechanicsWidgetMeta import BaseVehicleMechanicsWidgetMeta as BaseVehicleMechanicsWidgetMeta
from gui.shared.utils.key_mapping import getScaleformKey as getScaleformKey
from gui.veh_mechanics.battle.updaters.hotkey_updaters import IHotKeysView as IHotKeysView
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import IMechanicPassengerView as IMechanicPassengerView
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeyCommand as HotKeyCommand
HotKeyData: Any

class VehicleMechanicWidget(BaseVehicleMechanicsWidgetMeta, IHotKeysView, IMechanicPassengerView):
    _HOT_KEY_MAP: dict
    def setCrosshairType(self, crosshairType):
        ...
    def setHotkeys(self, hotKeyCommands):
        ...
    def setVisibleForPassenger(self, visibleForPassenger):
        ...
