# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/user_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import DEATH_REASON_ALIVE as DEATH_REASON_ALIVE
from gui.battle_results.pbs_helpers.common import isRealNameVisible as isRealNameVisible, isPersonalBattleResult as isPersonalBattleResult, getUserNames as getUserNames
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.battle_results.presenters.packers.interfaces import IBattleResultsPacker as IBattleResultsPacker
from gui.impl.gen.view_models.common.user_name_model import UserNameModel as UserNameModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo

class PersonalInfo(IBattleResultsPacker):
    @classmethod
    def packModel(cls, model, battleResults):
        ...

class UserNames(object):
    __slots__: tuple
    @classmethod
    def packBaseUserNames(cls, model, playerInfo, vehicleInfo, battleResults):
        ...
    @classmethod
    def packFullUserNames(cls, model, vehicleInfo, battleResults):
        ...
    @classmethod
    def _packNames(cls, model, playerInfo, battleResults):
        ...
    @classmethod
    def _setBadges(cls, model, reusable, playerDbID):
        ...
    @classmethod
    def _packBadges(cls, model, badgeInfo, suffixBadge):
        ...

class AccountInfo(UserNames):
    __slots__: tuple
    @classmethod
    def _packNames(cls, model, playerInfo, battleResults):
        ...
    @classmethod
    def _packBadges(cls, model, badgeInfo, suffixBadge):
        ...

class UserStatus(object):
    _USER_INFO_PACKER = UserNames
    @classmethod
    def packUserStatus(cls, model, battleResults, vehicleSumInfo):
        ...

class PlayerInfo(object):
    __slots__: tuple
    @classmethod
    def packModel(cls, model, battleResults, vehicleSumInfo):
        ...
    @classmethod
    def _packAccountInfo(cls, model, battleResults, vehicleSumInfo):
        ...
