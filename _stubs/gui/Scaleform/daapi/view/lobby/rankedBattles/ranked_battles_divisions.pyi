# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_divisions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_battles_page import IResetablePage as IResetablePage
from gui.Scaleform.daapi.view.meta.RankedBattlesDivisionsViewMeta import RankedBattlesDivisionsViewMeta as RankedBattlesDivisionsViewMeta
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.ranked_battles.ranked_builders import divisions_vos as divisions_vos
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class RankedBattlesDivisionsView(RankedBattlesDivisionsViewMeta, IResetablePage):
    __rankedController: Any
    __slots__: tuple
    __selectedDivisionIdx: Any
    def __init__(self):
        ...
    def onDivisionChanged(self, index):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def reset(self):
        ...
    @property
    def progressComponent(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getSelectedDivision(self):
        ...
    def __getDivisionsData(self):
        ...
    def __setDivisionHeader(self):
        ...
    def __updateSounds(self):
        ...
