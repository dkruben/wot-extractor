# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/BattleRoyaleRequester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IBattleRoyaleRequester as IBattleRoyaleRequester

class BattleRoyaleRequester(AbstractSyncDataRequester, IBattleRoyaleRequester):
    @property
    def accTitle(self):
        ...
    @property
    def battleCount(self):
        ...
    @property
    def killCount(self):
        ...
    @property
    def topCount(self):
        ...
    @property
    def dailyBonusUsedVehicles(self):
        ...
    def getStats(self, arenaBonusType, playerDatabaseID=None):
        ...
    def _requestCache(self, callback=None):
        ...
    def _preprocessValidData(self, data):
        ...
