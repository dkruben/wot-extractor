# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/dog_tag_composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from dog_tags_common.config.common import ComponentViewType as ComponentViewType, ComponentPurpose as ComponentPurpose
from dog_tags_common.number_formatter import formatComponentValue as formatComponentValue
from dog_tags_common.player_dog_tag import DisplayableDogTag as DisplayableDogTag
from gui.dog_tag_composer import DogTagComposerClient as DogTagComposerClient
from helpers import getLanguageCode as getLanguageCode
STARTING_GRADE_OFFSET = 1
layoutComposer: Any

class DogTagComposerInBattleGF(DogTagComposerClient):
    def fillModel(self, model, dogTag):
        ...

class DogTagComposerInBattleSF(DogTagComposerClient):
    def getModel(self, dt):
        ...
    def getModelFromDict(self, dogTag):
        ...
