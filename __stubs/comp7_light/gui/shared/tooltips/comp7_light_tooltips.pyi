# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/shared/tooltips/comp7_light_tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_core.gui.shared.tooltips.comp7_core_tooltips import RoleSkillLobbyTooltipData as RoleSkillLobbyTooltipData, RoleSkillBattleTooltipData as RoleSkillBattleTooltipData
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class Comp7LightRoleSkillLobbyTooltipData(RoleSkillLobbyTooltipData):
    __comp7LightController: Any
    @property
    def _modeController(self):
        ...

class Comp7LightRoleSkillBattleTooltipData(RoleSkillBattleTooltipData):
    __comp7LightController: Any
    @property
    def _modeController(self):
        ...
