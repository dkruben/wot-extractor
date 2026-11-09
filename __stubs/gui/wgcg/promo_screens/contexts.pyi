# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/promo_screens/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from gui.wgcg.promo_screens.parsers import PromoDataParser as PromoDataParser
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from helpers import dependency as dependency
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from typing import Dict as Dict

class BasePromoTeaserRequestCtx(CommonWebRequestCtx):
    __loginManager: Any
    def isAuthorizationRequired(self):
        ...
    def isClanSyncRequired(self):
        ...
    def isCaching(self):
        ...
    @classmethod
    def getAdditionalData(cls):
        ...

class PromoGetTeaserRequestCtx(BasePromoTeaserRequestCtx):
    def getDataObj(self, incomeData):
        ...
    def getRequestType(self):
        ...
    @classmethod
    def getAdditionalData(cls):
        ...

class PromoSendTeaserShownRequestCtx(BasePromoTeaserRequestCtx):
    __promoID: Any
    def __init__(self, promoID, waitingID=''):
        ...
    def getPromoID(self):
        ...
    def getRequestType(self):
        ...

class PromoGetUnreadCountRequestCtx(BasePromoTeaserRequestCtx):
    def getRequestType(self):
        ...
    @staticmethod
    def getCount(response):
        ...

class PromoSendActionLogCtx(CommonWebRequestCtx):
    __data: Any
    def __init__(self, data, waitingID=''):
        ...
    def isAuthorizationRequired(self):
        ...
    def isClanSyncRequired(self):
        ...
    def isCaching(self):
        ...
    def getRequestType(self):
        ...
    def getActionData(self):
        ...
