# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/reusable/avatars.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.battle_results.reusable import shared as shared, ReusableInfoFactory as ReusableInfoFactory
from gui.doc_loaders.badges_loader import getSelectedByLayout as getSelectedByLayout
from gui.shared.badges import buildBadge as buildBadge

class AvatarInfo(shared.ItemInfo):
    __slots__: tuple
    __totalDamaged: Any
    __avatarKills: Any
    __avatarDamaged: Any
    __avatarDamageDealt: Any
    __fairplayViolations: Any
    __accRank: Any
    __prevAccRank: Any
    __extInfo: Any
    __badge: Any
    __suffixBadge: Any
    __badgesInfo: Any
    def __init__(self, bonusType, totalDamaged=0, avatarKills=0, avatarDamaged=0, avatarDamageDealt=0, fairplayViolations=None, wasInBattle=True, accRank=None, prevAccRank=None, badges=..., **kwargs):
        ...
    @property
    def totalDamaged(self):
        ...
    @property
    def avatarKills(self):
        ...
    @property
    def avatarDamaged(self):
        ...
    @property
    def avatarDamageDealt(self):
        ...
    def hasPenalties(self):
        ...
    @property
    def accRank(self):
        ...
    @property
    def extensionInfo(self):
        ...
    @property
    def prevAccRank(self):
        ...
    @property
    def badge(self):
        ...
    @property
    def suffixBadge(self):
        ...
    def getFullBadgeInfo(self):
        ...

class AvatarsInfo(shared.UnpackedInfo):
    __slots__: tuple
    __avatars: Any
    __bonusType: Any
    def __init__(self, bonusType, avatars):
        ...
    def getAvatarInfo(self, dbID):
        ...
