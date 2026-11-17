# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/battle/battle_page/ammunition_panel/groups_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from frontline.constants.common import FRONTLINE_GROUPS as FRONTLINE_GROUPS
from gui.impl.battle.battle_page.ammunition_panel.groups_controller import RespawnAmmunitionGroupsController as RespawnAmmunitionGroupsController
from gui.impl.common.ammunition_panel.ammunition_groups_controller import RANDOM_GROUPS as RANDOM_GROUPS
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class FLRespawnAmmunitionGroupsController(RespawnAmmunitionGroupsController):
    __sessionProvider: Any
    def _getGroups(self):
        ...
