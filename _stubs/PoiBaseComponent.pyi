# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PoiBaseComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class PoiBaseComponent(DynamicScriptComponent):
    _POI_GO_NAME = 'PointOfInterest{id}'
    __sessionProvider: Any
    _poiGameObject: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def __getPoiGameObject(self):
        ...
