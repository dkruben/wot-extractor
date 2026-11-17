# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/wgcg/data_wrappers/server_replays.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import NamedTuple as NamedTuple, List as List, Optional as Optional
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
ShortReplay: Any
PageReplays: Any
TopReplays: Any
ReplayLink: Any

class DataNames(CONST_CONTAINER):
    TOP_REPLAYS = 'TOP_REPLAYS'
    BEST_REPLAYS = 'BEST_REPLAYS'
    MY_REPLAYS = 'MY_REPLAYS'
    REPLAY_LINK = 'REPLAY_LINK'
    FIND_REPLAY = 'FIND_REPLAY'
    ONE_REPLAY = 'ONE_REPLAY'

class StatParams(CONST_CONTAINER):
    DAMAGE_DEALT = 'damage_dealt'
    DAMAGE_ASSISTED = 'damage_assisted'
    DAMAGE_BLOCKED = 'damage_blocked'
    KILLS = 'kills_made'
    EXP = 'exp'
    MARK_OF_MASTERY = 'mastery_mark'
    LIKE_COUNT = 'likes_received'
