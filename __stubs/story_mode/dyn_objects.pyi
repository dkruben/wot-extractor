# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/dyn_objects.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
from dyn_objects_cache import DynObjectsBase as DynObjectsBase, createTerrainCircleSettings as createTerrainCircleSettings
from story_mode_common.story_mode_constants import RECON_ABILITY as RECON_ABILITY, DISTRACTION_ABILITY as DISTRACTION_ABILITY, SCC_AIRSTRIKE_ABILITY as SCC_AIRSTRIKE_ABILITY, SCC_AIRSTRIKE_ABILITY_HARD as SCC_AIRSTRIKE_ABILITY_HARD
from ResMgr import DataSection as DataSection
DEFAULT = 'default'
EQUIPMENT_VISUALS: dict

class StoryModeDynObjects(DynObjectsBase):
    _circleSettings: Any
    def __init__(self):
        ...
    def init(self, dataSection):
        ...
    def destroy(self):
        ...
    def getAimingCircleRestrictionEffect(self, equipment):
        ...
