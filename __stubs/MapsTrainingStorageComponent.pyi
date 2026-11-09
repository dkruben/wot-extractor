# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/MapsTrainingStorageComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from maps_training_common.maps_training_constants import VEHICLE_CLASSES_ORDER as VEHICLE_CLASSES_ORDER

class MapsTrainingStorageComponent(BigWorld.DynamicScriptComponent):
    sessionProvider: Any
    _globalGoalsData: Any
    def __init__(self):
        ...
    def getGlobalGoal(self, key):
        ...
    def set_localGoal(self, *args, **kwargs):
        ...
    def set_globalGoals(self, *args, **kwargs):
        ...
