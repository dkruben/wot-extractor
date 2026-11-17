# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/gift_system_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IGiftSystemRequester as IGiftSystemRequester

class GiftSystemRequester(AbstractSyncDataRequester, IGiftSystemRequester):
    @property
    def isHistoryReady(self):
        ...
    def _requestCache(self, callback=None):
        ...
