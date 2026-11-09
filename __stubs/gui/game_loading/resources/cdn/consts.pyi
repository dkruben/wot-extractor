# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/resources/cdn/consts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import enum as enum
import typing as typing
MAX_CONFIG_SEQUENCE_SLIDES_COUNT = 250
MAX_CONFIG_SEQUENCES_COUNT = 50
MIN_SLIDES_COUNT_TO_VIEW = 5
DOWNLOAD_SLIDES_MULTIPLAYER = 2
CDN_CACHE_SYNC_TIMEOUT = 300.0
NEWBIES_BATTLES_LIMIT = 400

# decorador original: @enum.unique
class SequenceOrders(str, enum.Enum):
    RANDOM = 'random'
    SUBSEQUENTLY = 'subsequently'

# decorador original: @enum.unique
class SequenceCohorts(str, enum.Enum):
    DEFAULT = 'default'
    NEWBIES = 'newbies'
    @classmethod
    def getDefaults(cls):
        ...
