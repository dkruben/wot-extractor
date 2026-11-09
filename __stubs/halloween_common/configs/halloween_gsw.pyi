# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/common/halloween_common/configs/halloween_gsw.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from game_params_common.base_manager import GameParamsSchema as GameParamsSchema
from dict2model import models as models, fields as fields, schemas as schemas
from halloween_common.halloween_constants import HALLOWEEN_GSW_PARAMS_KEY as HALLOWEEN_GSW_PARAMS_KEY
from typing import List as List, Optional as Optional
cardSchema: Any
cardsSchema: Any
GSWSchema: Any

class CardModel(models.Model):
    __slots__: tuple
    visibleByToken: Any
    quests: Any
    def __init__(self, visibleByToken, quests):
        ...

class CardsModel(models.Model):
    __slots__: tuple
    card: Any
    def __init__(self, card):
        ...

class GSWModel(models.Model):
    __slots__: tuple
    cards: Any
    def __init__(self, cards):
        ...
