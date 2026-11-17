# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/RankedRequester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IRankedRequester as IRankedRequester

class RankedRequester(AbstractSyncDataRequester, IRankedRequester):
    @property
    def season(self):
        ...
    @property
    def accRank(self):
        ...
    @property
    def maxRank(self):
        ...
    @property
    def stepsCount(self):
        ...
    @property
    def seasonStepsCount(self):
        ...
    @property
    def seasonEfficiencyStamp(self):
        ...
    @property
    def divisionsStats(self):
        ...
    @property
    def shields(self):
        ...
    @property
    def persistentBonusBattles(self):
        ...
    @property
    def dailyBonusBattles(self):
        ...
    def _requestCache(self, callback=None):
        ...
    def _preprocessValidData(self, data):
        ...
