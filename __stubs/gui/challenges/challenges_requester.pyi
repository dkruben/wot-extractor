# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/challenges/challenges_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from challenges_common import CHALLENGES_PDATA_KEY as CHALLENGES_PDATA_KEY
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IChallengesRequester as IChallengesRequester

class ChallengesRequester(AbstractSyncDataRequester, IChallengesRequester):
    def getUsedFreeRestarts(self, challengeID):
        ...
    def _preprocessValidData(self, data):
        ...
    def _requestCache(self, callback=None):
        ...
