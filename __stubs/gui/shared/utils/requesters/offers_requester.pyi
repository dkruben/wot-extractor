# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/offers_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IOffersRequester as IOffersRequester

class OffersRequester(AbstractSyncDataRequester, IOffersRequester):
    def getReceivedGifts(self, offerID):
        ...
    def isBannerSeen(self, offerID):
        ...
    def _requestCache(self, callback=None):
        ...
    def __getOffer(self, offerID):
        ...
