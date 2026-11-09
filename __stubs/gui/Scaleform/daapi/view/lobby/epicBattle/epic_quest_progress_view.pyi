# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/epicBattle/epic_quest_progress_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.battle_results_window import IBattleResultsComponent as IBattleResultsComponent
from gui.Scaleform.daapi.view.meta.EpicQuestProgressInfoMeta import EpicQuestProgressInfoMeta as EpicQuestProgressInfoMeta
from gui.shared import g_eventBus as g_eventBus, events as events
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService

class EpicQuestProgressView(EpicQuestProgressInfoMeta, IBattleResultsComponent):
    __slots__: tuple
    __battleResults: Any
    def showQuestById(self, questId, eventType):
        ...
    def setArenaUniqueID(self, arenaUniqueID):
        ...
    def updateQuestsInfo(self, arenaUniqueID):
        ...
    @staticmethod
    def __getRewards(quest):
        ...
