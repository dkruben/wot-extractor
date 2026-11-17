# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/badges_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import struct as struct
from typing import TYPE_CHECKING as TYPE_CHECKING, List as List, Tuple as Tuple, Any as Any
from BaseAccount import BaseAccount as BaseAccount
ExtraInfo: _Any
BadgesInfo: _Any

class BadgesCommon(object):
    _BADGE_IDS_LEN_FORMAT = '<B'
    _BADGE_IDS = '<{}I'
    _BADGES_EXTRA_INFO = '<I'
    @staticmethod
    def getExtraInfo(account):
        ...
    @staticmethod
    def selectedBadgesEmpty():
        ...
    @staticmethod
    def packPlayerBadges(badgesInfo):
        ...
    @staticmethod
    def unpackPlayerBadges(packedData, initialOffset):
        ...
    @staticmethod
    def _getBadgeIDsFormat(badgesLen):
        ...
    @staticmethod
    def _packLen(lenValue):
        ...
    @staticmethod
    def _unpackLen(packedData, offset):
        ...
