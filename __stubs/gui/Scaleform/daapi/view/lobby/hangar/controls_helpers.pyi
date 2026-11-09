# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/controls_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency
from skeletons.gui.game_control import IEasyTankEquipController as IEasyTankEquipController, ILimitedUIController as ILimitedUIController
from gui.vehicle_view_states import IVehicleViewState as IVehicleViewState
EasyTankEquipSetupData: Any

class IHangarControlsHelper(object):
    __slots__: tuple
    @classmethod
    def getEasyTankEquipSetupData(cls, state, needToShowRepairButton, isAvailableForVehicleByLevel):
        ...

class DefaultHangarControlsHelper(IHangarControlsHelper):
    __slots__: tuple
    @classmethod
    def getEasyTankEquipSetupData(cls, state, needToShowRepairButton, isAvailableForVehicleByLevel):
        ...

class RandomHangarControlsHelper(IHangarControlsHelper):
    __slots__: tuple
    __limitedUIController: Any
    __easyTankEquipController: Any
    _RES_SHORTCUT = R.strings.tooltips.hangar.easyTankEquip
    @classmethod
    def getEasyTankEquipSetupData(cls, state, needToShowRepairButton, isAvailableForVehicleByLevel):
        ...
