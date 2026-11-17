# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/common/name_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from wg_async import wg_async as wg_async, wg_await as wg_await
from helpers import dependency as dependency
from skeletons.gui.platform.wgnp_controllers import IWGNPDemoAccRequestController as IWGNPDemoAccRequestController
from typing import Callable as Callable
from gui.platform.wgnp.demo_account.request import ValidateNicknameParams as ValidateNicknameParams

class ValidationRequestWrapper(object):
    __slots__: tuple
    _wgnpDemoAccCtrl: Any
    _instances: Any
    _isDisposed: Any
    def __init__(self):
        ...
    # decorador original: @wg_async
    def process(self, name, callback):
        ...
    def dispose(self):
        ...
    @staticmethod
    def create():
        ...
    @staticmethod
    def utilize(wrapper):
        ...
