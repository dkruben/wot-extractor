# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/ammunition_setup/hangar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.impl.lobby.tank_setup.ammunition_panel.hangar import HangarAmmunitionPanel as HangarAmmunitionPanel
from gui.impl.lobby.tank_setup.ammunition_setup.base_hangar import BaseHangarAmmunitionSetupView as BaseHangarAmmunitionSetupView
from gui.impl.lobby.tank_setup.main_tank_setup.hangar import HangarMainTankSetupView as HangarMainTankSetupView
from gui.impl.lobby.tank_setup.optional_devices_assistant.hangar import OptionalDevicesAssistantView as OptionalDevicesAssistantView
from gui.impl.lobby.tank_setup.tank_setup_builder import HangarTankSetupBuilder as HangarTankSetupBuilder
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
_logger: Any

class HangarAmmunitionSetupView(BaseHangarAmmunitionSetupView, IGlobalListener):
    __slots__: tuple
    _wotPlusController: Any
    _optionalDevicesAssistant: Any
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _createOptionalDevicesAssistantPanel(self):
        ...
    def _createMainTankSetup(self):
        ...
    def _createAmmunitionPanel(self):
        ...
    def __getTankSetupBuilder(self):
        ...
    def __onWotPlusDataChanged(self, isEnabledVal):
        ...
