# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/hangar_selectable_objects/hangar_selectable_logic.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from gui.Scaleform.Waiting import Waiting as Waiting
from hangar_selectable_objects import ISelectableObject as ISelectableObject
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from .base_selectable_logic import BaseSelectableLogic as BaseSelectableLogic

class HangarSelectableLogic(BaseSelectableLogic):
    __hangarSpace: Any
    __selected3DEntity: Any
    __selected3DEntityUnderMouseDown: Any
    def __init__(self):
        ...
    def init(self, callback=None):
        ...
    def fini(self):
        ...
    def _onNotifyCursorOver3dScene(self, isCursorOver3dScene):
        ...
    def _filterEntity(self, entity):
        ...
    def _onMouseEnter(self, entity):
        ...
    def _onMouseExit(self, entity):
        ...
    def _onMouseDown(self):
        ...
    def _onMouseUp(self):
        ...
    def __onMouseEnter(self, entity):
        ...
    def __highlight3DEntity(self, entity):
        ...
    def __fade3DEntity(self, entity):
        ...
