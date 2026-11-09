# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dog_tags_common/dog_tags_storage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from dog_tags_common.components_config import componentConfigAdapter as componentConfigAdapter
from dog_tags_common.config.common import NO_PROGRESS as NO_PROGRESS, DEFAULT_GRADE as DEFAULT_GRADE
from dog_tags_common.player_dog_tag import PlayerDogTag as PlayerDogTag, DogTagComponent as DogTagComponent
ProgressRecord: Any
EMPTY_PROGRESS_RECORD: Any
SkillDataRecord: Any

class Storage(object):
    key = ''
    _section: Any
    def __init__(self, data):
        ...
    @classmethod
    def empty(cls):
        ...
    @classmethod
    def default(cls):
        ...

class UnlockedComponentsStorage(Storage):
    key = 'unlockedComponents'
    @classmethod
    def default(cls):
        ...
    @classmethod
    def empty(cls):
        ...
    def getAll(self):
        ...
    def isUnlocked(self, compId):
        ...

class ProgressStorage(Storage):
    key = 'progress'
    @classmethod
    def default(cls):
        ...
    @classmethod
    def empty(cls):
        ...
    def getAllItems(self):
        ...
    def get(self, compId):
        ...

class ExtraDataStorage(Storage):
    key = 'extra'
    skillDataKey = 'skillData'
    @classmethod
    def default(cls):
        ...
    @classmethod
    def empty(cls):
        ...
    def getSkillData(self, compId):
        ...

class PlayerDogTagStorage(Storage):
    key = 'playerDogTag'
    _progressStorage: Any
    def __init__(self, data):
        ...
    @classmethod
    def default(cls):
        ...
    @classmethod
    def empty(cls):
        ...
    def get(self):
        ...
    def getData(self):
        ...
    def buildPlayerDogTag(self, compIds):
        ...
    def buildComponentForAccount(self, compId):
        ...
