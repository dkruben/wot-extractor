# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/achievements20_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import BigWorld as BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IAchievements20Requester as IAchievements20Requester
from constants import AchievementsLayoutStates as AchievementsLayoutStates
from typing import List as List

class Achievements20Requester(AbstractSyncDataRequester, IAchievements20Requester):
    def getLayout(self):
        ...
    def getLayoutState(self):
        ...
    def getAchievementBitmask(self):
        ...
    def getLayoutLength(self):
        ...
    def _preprocessValidData(self, data):
        ...
    def _requestCache(self, callback=None):
        ...
