# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/game_restrictions_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import BigWorld as BigWorld
from constants import RESTRICTION_KEY as RESTRICTION_KEY
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IGameRestrictionsRequester as IGameRestrictionsRequester

class GameRestrictionsRequester(AbstractSyncDataRequester, IGameRestrictionsRequester):
    @property
    def session(self):
        ...
    @property
    def hasSessionLimit(self):
        ...
    def getKickAt(self):
        ...
    @property
    def settings(self):
        ...
    @property
    def privateChat(self):
        ...
    def _requestCache(self, callback=None):
        ...
