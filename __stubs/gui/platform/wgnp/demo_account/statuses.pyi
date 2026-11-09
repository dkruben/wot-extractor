# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/wgnp/demo_account/statuses.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import EMAIL_CONFIRMATION_TOKEN_NAME as EMAIL_CONFIRMATION_TOKEN_NAME
from gui.platform.base.response import Codes as Codes
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes
from gui.platform.base.statuses.status import Status as Status
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.platform.wgnp.demo_account.request import CredentialsStatusParams as CredentialsStatusParams

class DemoAccCredentialsStatus(Status):
    __slots__: tuple
    @property
    def isSpaWeakPassword(self):
        ...
    @property
    def login(self):
        ...

class DemoAccNicknameStatus(Status):
    __slots__: tuple
    @property
    def cost(self):
        ...

def createCredentialsConfirmationStatus():
    ...
def createCredentialStatusFromResponse(response):
    ...
def createNicknameStatusFromResponse(response):
    ...
