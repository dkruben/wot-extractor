# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/storages/winback_storage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.storages.local_storage import SessionStorage as SessionStorage
from helpers import dependency as dependency
from skeletons.gui.game_control import IWinbackController as IWinbackController

class WinbackStorage(SessionStorage):
    __winbackController: Any
    def isModeSelected(self):
        ...
    def isModeAvailable(self):
        ...
    def _determineSelection(self, arenaVisitor):
        ...
