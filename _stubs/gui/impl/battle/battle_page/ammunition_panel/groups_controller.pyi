# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/battle_page/ammunition_panel/groups_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CommandMapping as CommandMapping
from gui.Scaleform.daapi.view.common.keybord_helpers import getHotKeyList as getHotKeyList
from gui.impl.battle.battle_page.ammunition_panel.blocks_controller import PrebattleAmmunitionBlocksController as PrebattleAmmunitionBlocksController, RespawnAmmunitionBlocksController as RespawnAmmunitionBlocksController
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_ammunition_items_group import PrebattleAmmunitionItemsGroup as PrebattleAmmunitionItemsGroup
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_constants import AmmunitionPanelConstants as AmmunitionPanelConstants
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController as AmmunitionGroupsController, RANDOM_GROUPS as RANDOM_GROUPS
COMMAND_MAPPING: dict
_GROUPS_COMMANDS: dict

class PrebattleAmmunitionGroupsController(AmmunitionGroupsController):
    def onNextShellChanged(self, intCD):
        ...
    def onCurrentShellChanged(self, intCD):
        ...
    def _getGroups(self):
        ...
    def _createViewModel(self):
        ...
    def _setupStates(self, setupSelectorModel, groupSettings):
        ...
    def _createAmmunitionBlockController(self, vehicle, ctx=None):
        ...
    def _isSwitchEnabled(self, groupSettings):
        ...

class RespawnAmmunitionGroupsController(AmmunitionGroupsController):
    __sessionProvider: Any
    def _getGroups(self):
        ...
    def _createAmmunitionBlockController(self, vehicle, ctx=None):
        ...
    def _isPrebattleSwitchDisabled(self, _):
        ...
