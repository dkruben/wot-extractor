# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import IS_FIRST_ENTRY_BY_DIVISION_ID as IS_FIRST_ENTRY_BY_DIVISION_ID
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_battles_page import IResetablePage as IResetablePage
from gui.Scaleform.daapi.view.meta.RankedBattlesDivisionProgressMeta import RankedBattlesDivisionProgressMeta as RankedBattlesDivisionProgressMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles import ranked_helpers as ranked_helpers
from gui.ranked_battles.ranked_builders import divisions_vos as divisions_vos
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class RankedBattlesProgress(RankedBattlesDivisionProgressMeta, IResetablePage):
    __rankedController: Any
    __slots__: tuple
    __selectedDivisionIdx: Any
    def __init__(self):
        ...
    def selectDivision(self, index):
        ...
    def reset(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getSelectedDivision(self):
        ...
    def __onRankedUpdate(self):
        ...
    def __dossierUpdateCallBack(self, *args):
        ...
    def __setBonusBattlesCount(self):
        ...
    def __setDivisionStats(self):
        ...
    def __setRankedData(self):
        ...
    def __setDivisionStatus(self):
        ...
    def __buildProgressData(self):
        ...
