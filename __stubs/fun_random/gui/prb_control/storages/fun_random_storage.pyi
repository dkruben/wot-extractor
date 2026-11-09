# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/storages/fun_random_storage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID as UNKNOWN_EVENT_ID
from gui.prb_control.storages.local_storage import SessionStorage as SessionStorage
from helpers import dependency as dependency
from skeletons.gui.game_control import IFunRandomController as IFunRandomController

class FunRandomStorage(SessionStorage):
    __funRandomController: Any
    def isModeSelected(self):
        ...
