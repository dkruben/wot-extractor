# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/plan_tags.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS, ALLOWED_ARENA_BONUS_TYPE_CAPS as ALLOWED_ARENA_BONUS_TYPE_CAPS
from constants import IS_CLIENT as IS_CLIENT, IS_DEVELOPMENT as IS_DEVELOPMENT
import BattleReplay as BattleReplay

class PlanTags(object):
    _tags: dict
    EXTRA_TAGS: list
    _tagsList: Any
    def __init__(self, arenaBonusType=0):
        ...
    @property
    def tags(self):
        ...

def bonusCapToTag(cap):
    ...
def notInReplay():
    ...
def getAllTags():
    ...
