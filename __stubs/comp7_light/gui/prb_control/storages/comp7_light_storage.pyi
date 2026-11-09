# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/prb_control/storages/comp7_light_storage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_light_constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from gui.prb_control.storages.local_storage import SessionStorage as SessionStorage
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

class Comp7LightStorage(SessionStorage):
    _GUI_TYPE = ARENA_GUI_TYPE.COMP7_LIGHT
    __comp7LightController: Any
    def isModeSelected(self):
        ...
    def _determineSelection(self, arenaVisitor):
        ...
