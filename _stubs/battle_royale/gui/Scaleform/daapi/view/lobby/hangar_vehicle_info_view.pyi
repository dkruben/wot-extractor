# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/hangar_vehicle_info_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import CommandMapping as CommandMapping
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.Scaleform.daapi.view.common.battle_royale import br_helpers as br_helpers
from gui.shared.gui_items.Vehicle import getTypeBigIconPath as getTypeBigIconPath
from battle_royale.gui.Scaleform.daapi.view.common.veh_modules_config_cmp import VehicleModulesConfiguratorCmp as VehicleModulesConfiguratorCmp
from battle_royale.gui.Scaleform.daapi.view.lobby.battle_royale_sounds import BATTLE_ROYALE_VEHICLE_INFO_SOUND_SPACE as BATTLE_ROYALE_VEHICLE_INFO_SOUND_SPACE
from gui.Scaleform.daapi.view.meta.BattleRoyaleVehicleInfoMeta import BattleRoyaleVehicleInfoMeta as BattleRoyaleVehicleInfoMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
_logger: Any

class HangarVehicleModulesConfigurator(VehicleModulesConfiguratorCmp):
    __itemsCache: Any
    __INITIAL_LEVEL = 2
    def setVehicle(self, vehicle):
        ...
    def setAvailableLevel(self, level):
        ...
    def getAvailableLevel(self):
        ...
    def _getItem(self, intCD):
        ...
    def _updateColumns(self):
        ...
    def _syncVehicle(self, intCD):
        ...
    def _recreate(self):
        ...
    def _getHighlightedModules(self):
        ...
    def _isModuleSelected(self, item, vehicle):
        ...
    def _canBeShown(self, intCD, level, unlocks):
        ...
    def _setCurrentLevel(self, moduleLevel):
        ...

class HangarVehicleInfo(BattleRoyaleVehicleInfoMeta, IGlobalListener):
    __itemsCache: Any
    __battleRoyaleController: Any
    _COMMON_SOUND_SPACE = BATTLE_ROYALE_VEHICLE_INFO_SOUND_SPACE
    __guiVehConfigurator: Any
    __vehicle: Any
    __introPage: Any
    __blur: Any
    def __init__(self, ctx=None):
        ...
    def getSelectedVehicle(self):
        ...
    def onClose(self):
        ...
    def onPrbEntitySwitching(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _populate(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _dispose(self):
        ...
    def __onBattleRoyaleEnabledChanged(self):
        ...
