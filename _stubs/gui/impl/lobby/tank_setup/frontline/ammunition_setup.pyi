# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/frontline/ammunition_setup.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.lobby.tank_setup.ammunition_setup.hangar import HangarAmmunitionSetupView as HangarAmmunitionSetupView
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class FrontlineAmmunitionSetupView(HangarAmmunitionSetupView):
    __epicController: Any
    def createToolTipContent(self, event, contentID):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def __onEpicUpdated(self, diff):
        ...
