# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/shared/tooltips/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.tooltips import TOOLTIP_COMPONENT as TOOLTIP_COMPONENT
from gui.shared.tooltips.contexts import ToolTipContext as ToolTipContext
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class Comp7LightRoleSkillBattleContext(ToolTipContext):
    __comp7LightController: Any
    def __init__(self):
        ...
    def buildItem(self, equipmentName):
        ...
    def getStartLevel(self, roleName):
        ...

class Comp7LightRoleSkillLobbyContext(ToolTipContext):
    def __init__(self):
        ...
    def buildItem(self, equipmentName):
        ...
