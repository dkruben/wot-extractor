# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/quest_deltas_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from future.utils import PY3 as PY3, iteritems as iteritems
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import QUEST_DELTAS as QUEST_DELTAS, QUESTS as QUESTS
from collections import UserDict as IterableUserDict
from UserDict import IterableUserDict as IterableUserDict
from typing import Any as Any, Hashable as Hashable

class QuestDeltasSettings(IterableUserDict):
    _subKey: _Any
    def __init__(self, subKey=''):
        ...
    def __setitem__(self, key, item):
        ...
    def __delitem__(self, key):
        ...
    def _saveToSettings(self):
        ...
