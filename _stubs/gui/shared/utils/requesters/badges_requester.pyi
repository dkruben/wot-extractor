# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/badges_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import BigWorld as BigWorld
from gui.doc_loaders.badges_loader import getAvailableBadges as getAvailableBadges
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IBadgesRequester as IBadgesRequester

class BadgesRequester(AbstractSyncDataRequester, IBadgesRequester):
    @property
    def available(self):
        ...
    @property
    def selected(self):
        ...
    def _requestCache(self, callback=None):
        ...
