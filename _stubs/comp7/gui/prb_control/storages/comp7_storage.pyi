# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/prb_control/storages/comp7_storage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.storages.local_storage import SessionStorage as SessionStorage
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7_common.comp7_constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE

class Comp7Storage(SessionStorage):
    _GUI_TYPE = ARENA_GUI_TYPE.COMP7
    __comp7Controller: Any
    def isModeSelected(self):
        ...
    def _determineSelection(self, arenaVisitor):
        ...
