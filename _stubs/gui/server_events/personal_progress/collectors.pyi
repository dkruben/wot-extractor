# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/personal_progress/collectors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import quest_progress as quest_progress
from constants import QUEST_PROGRESS_STATE as QUEST_PROGRESS_STATE
from personal_missions_constants import VISIBLE_SCOPE as VISIBLE_SCOPE, CONTAINER as CONTAINER

class ClientProgressCollector(quest_progress.IDataCollector):
    @classmethod
    def validate(cls, progress):
        ...
    @classmethod
    def collect(cls, progress):
        ...

class HeaderProgressCollector(ClientProgressCollector):
    @classmethod
    def validate(cls, progress):
        ...

class BodyProgressCollector(ClientProgressCollector):
    @classmethod
    def validate(cls, progress):
        ...

class UniqueProgressCollector(ClientProgressCollector):
    @classmethod
    def validate(cls, progress):
        ...

class LobbyProgressCollector(ClientProgressCollector):
    @classmethod
    def validate(cls, progress):
        ...

class BattleProgressCollector(ClientProgressCollector):
    @classmethod
    def validate(cls, progress):
        ...

class SubQuestProgressCollector(ClientProgressCollector):
    __slots__: tuple
    _isMain: Any
    def __init__(self, isMain=None):
        ...
    def validate(self, progress):
        ...

class LobbyHeaderProgressCollector(SubQuestProgressCollector):
    def validate(self, progress):
        ...

class LobbyBodyProgressCollector(SubQuestProgressCollector):
    def validate(self, progress):
        ...

class BattleHeaderProgressCollector(SubQuestProgressCollector):
    def validate(self, progress):
        ...

class BattleBodyProgressCollector(SubQuestProgressCollector):
    def validate(self, progress):
        ...

class BattleUniqueProgressCollector(SubQuestProgressCollector):
    def validate(self, progress):
        ...

class ChangedProgressCollector(BattleBodyProgressCollector):
    def validate(self, condProgress):
        ...

class ProgressWithTimerCollector(BattleBodyProgressCollector):
    def validate(self, condProgress):
        ...
