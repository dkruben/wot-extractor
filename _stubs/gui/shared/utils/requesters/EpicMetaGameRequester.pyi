# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/EpicMetaGameRequester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from past.utils import old_div as old_div
import BigWorld as BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IEpicMetaGameRequester as IEpicMetaGameRequester

class EpicMetaGameRequester(AbstractSyncDataRequester, IEpicMetaGameRequester):
    @property
    def playerLevelInfo(self):
        ...
    @property
    def seasonData(self):
        ...
    @property
    def skillPoints(self):
        ...
    def selectedSkills(self, vehicleCD):
        ...
    @property
    def skillLevels(self):
        ...
    @property
    def battleCount(self):
        ...
    @property
    def averageXP(self):
        ...
    def _requestCache(self, callback=None):
        ...
    def _preprocessValidData(self, data):
        ...
