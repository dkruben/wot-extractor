# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/ammunition_panel/hangar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import adisp as adisp
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from gui.impl.lobby.tank_setup.ammunition_panel.groups_controller import HangarAmmunitionGroupsController as HangarAmmunitionGroupsController
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from gui.impl.common.ammunition_panel.base import BaseAmmunitionPanel as BaseAmmunitionPanel
from gui.impl.common.ammunition_panel.ammunition_groups_controller import GROUPS_MAP as GROUPS_MAP
from gui.veh_post_progression.sounds import playSound as playSound, Sounds as Sounds
from helpers import dependency as dependency
from post_progression_common import TankSetupGroupsId as TankSetupGroupsId
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

class HangarAmmunitionPanel(BaseAmmunitionPanel):
    _settingsCore: Any
    # decorador original: @adisp.adisp_process
    def onChangeSetupLayoutIndex(self, hudGroupID, layoutIdx, callback=None):
        ...
    def _createAmmunitionGroupsController(self, vehicle):
        ...
    def __markHintUsed(self, groupId):
        ...
