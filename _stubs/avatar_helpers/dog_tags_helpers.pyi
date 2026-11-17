# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/avatar_helpers/dog_tags_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
import BigWorld as BigWorld
from dog_tags_common.components_config import componentConfigAdapter as componentConfigAdapter
from dog_tags_common.components_packer import unpack_component as unpack_component
from dog_tags_common.config.common import ComponentViewType as ComponentViewType
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from soft_exception import SoftException as SoftException

class DogTagsHelpers(object):
    guiSessionProvider: Any
    @classmethod
    def showRandomVictimDogTag(cls):
        ...
    @classmethod
    def showRandomKillerDogTag(cls):
        ...
    @classmethod
    def _randomDogTag(cls):
        ...
    @classmethod
    def _getDeadReasonInfo(cls):
        ...
    @classmethod
    def _selectRandomEnemyVehicleInfo(cls):
        ...
    @classmethod
    def _getRandomDogTagForVehicle(cls, vInfo):
        ...
    @classmethod
    def _getDogTagController(cls):
        ...
