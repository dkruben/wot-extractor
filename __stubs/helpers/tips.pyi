# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/tips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
import random as random
import re as re
from collections import namedtuple as namedtuple
from future.utils import lfilter as lfilter
import nations as nations
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import ROYALE_SQUAD_TIP_SHOWN_FOR_SEASON as ROYALE_SQUAD_TIP_SHOWN_FOR_SEASON
from account_helpers.AccountSettings import WATCHED_PRE_BATTLE_TIPS_SECTION as WATCHED_PRE_BATTLE_TIPS_SECTION
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, IS_DEVELOPMENT as IS_DEVELOPMENT
from gui.battle_pass.battle_pass_helpers import isBattlePassActiveSeason as isBattlePassActiveSeason
from gui.doc_loaders.prebattle_tips_loader import getPreBattleTipsConfig as getPreBattleTipsConfig
from gui.impl.gen import R as R
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore
from gui.shared.system_factory import registerBattleTipCriteria as registerBattleTipCriteria, registerBattleTipsCriteria as registerBattleTipsCriteria, collectBattleTipsCriteria as collectBattleTipsCriteria
from helpers import dependency as dependency
from realm import CURRENT_REALM as CURRENT_REALM
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController, IRankedBattlesController as IRankedBattlesController, IVehiclePostProgressionController as IVehiclePostProgressionController
from typing import Optional as Optional
_logger: Any
_RANDOM_TIPS_PATTERN = '^(tip\\d+)'
_EPIC_BATTLE_TIPS_PATTERN = '^(epicTip\\d+)'
_EPIC_RANDOM_TIPS_PATTERN = '^(epicRandom\\d+)'
_RANKED_BATTLES_TIPS_PATTERN = '^(ranked\\d+)'
_BATTLE_ROYALE_TIPS_PATTERN = '^(battleRoyale\\d+$)'
_ST_PATRICK_PATTERN = '^(stPatrick\\d+$)'
_WINBACK_TIPS_PATTERN = '^(winback\\d+$)'
_MAPBOX_TIPS_PATTERN = '^(mapbox\\d+)'
_DEV_MAPS_PATTERN = '^(devMaps\\d+)'
_watchedTipsCache = None
_tipsConfig: Any
_randomTips: Any
_rankedTips: Any
_epicBattleTips: Any
_epicRandomTips: Any
_battleRoyaleTips: Any
_stPatrickTips: Any
_winbackTips: Any
_mapboxTips: Any
_devMapsTips: Any

class _BattleLoadingTipPriority(object):
    GENERIC = 1
    PRECEDING = 2

# base nao representavel no stub: namedtuple(...)
class TipData:
    def isValid(self):
        ...

class TipsCriteria(object):
    __slots__: tuple
    _ctx: Any
    _tipsValidator: Any
    def __init__(self, *_):
        ...
    def setContext(self, ctx):
        ...
    def find(self):
        ...
    def _findRandomTip(self):
        ...
    def _getArenaGuiType(self):
        ...
    def _getTipsValidator(self):
        ...
    def _suitableTipPredicate(self, tip):
        ...
    def _getTargetList(self):
        ...

class _RandomTipsCriteria(TipsCriteria):
    def _getTargetList(self):
        ...
    def _getArenaGuiType(self):
        ...

class _EpicBattleTipsCriteria(TipsCriteria):
    def find(self):
        ...
    def _getTargetList(self):
        ...
    def _getArenaGuiType(self):
        ...

class _EventTipsCriteria(TipsCriteria):
    def find(self):
        ...

class _DevMapsTipsCriteria(TipsCriteria):
    def _getTargetList(self):
        ...

class _RankedTipsCriteria(TipsCriteria):
    def _getTargetList(self):
        ...

class _EpicRandomTipsCriteria(TipsCriteria):
    def _getTargetList(self):
        ...

class _WinbackTipsCriteria(TipsCriteria):
    def _getTargetList(self):
        ...
    def _getArenaGuiType(self):
        ...

class BattleRoyaleTipsCriteria(TipsCriteria):
    __battleRoyaleController: Any
    _arenaVisitor: Any
    def __init__(self, arenaVisitor):
        ...
    def find(self):
        ...
    def _getTargetList(self):
        ...
    def _getArenaGuiType(self):
        ...
    # decorador original: @dependency.replace_none_kwargs(...)
    def __getSquadTip(self, battleRoyaleController=None):
        ...
    def __getTipIcon(self, tipId):
        ...

class _MapboxTipsCriteria(TipsCriteria):
    def _getTargetList(self):
        ...
    def _getArenaGuiType(self):
        ...

class ExactTipsCriteria(TipsCriteria):
    __slots__: tuple
    _exactTip: Any
    def __init__(self, _exactTipPattern):
        ...
    def find(self):
        ...

class _TipsValidator(object):
    _validatorsList: Any
    def __init__(self):
        ...
    def validateRegularTip(self, tipFilter, ctx=None):
        ...

class _BattleLoadingTip(object):
    __slots__: tuple
    _tipId: Any
    _statusResId: Any
    _iconResId: Any
    _descriptionResId: Any
    _tipFilter: Any
    def __init__(self):
        ...
    def build(self, tipID, descriptionResID, config):
        ...
    @property
    def tipFilter(self):
        ...
    def markWatched(self):
        ...
    def getPriority(self):
        ...
    def getTipId(self):
        ...
    def getData(self):
        ...
    def __repr__(self):
        ...

class _PrecedingBattleLoadingTip(_BattleLoadingTip):
    __slots__: tuple
    _showLimit: Any
    def __init__(self):
        ...
    def setShowLimit(self, limit):
        ...
    def markWatched(self):
        ...
    def getPriority(self):
        ...

class _ChassisTypeValidator(object):
    @staticmethod
    def validate(tipFilter, ctx):
        ...

class _VehPropertyValidator(object):
    @staticmethod
    def validate(tipFilter, ctx):
        ...

class _MechanicsValidator(object):
    @staticmethod
    def validate(tipFilter, ctx):
        ...

class _BattlesValidator(object):
    @staticmethod
    def validate(tipFilter, ctx):
        ...

class _ArenaGuiTypeValidator(object):
    @staticmethod
    def validate(tipFilter, ctx):
        ...

class _TagsValidator(object):
    @staticmethod
    def validate(tipFilter, ctx):
        ...

class _LevelValidator(object):
    @staticmethod
    def validate(tipFilter, ctx):
        ...

class _NationValidator(object):
    @staticmethod
    def validate(tipFilter, ctx):
        ...

class _VehicleClassValidator(object):
    @staticmethod
    def validate(tipFilter, ctx):
        ...

class _RealmsValidator(object):
    @staticmethod
    def validate(tipFilter, _):
        ...

class _BattlePassValidator(object):
    __slots__: tuple
    _isActiveSeason: Any
    def __init__(self):
        ...
    def validate(self, tipFilter, _):
        ...

class _RankedBattlesValidator(object):
    __slots__: tuple
    _rankedController: Any
    _isYearRewardEnabled: Any
    _isLeaderboardEnabled: Any
    _isShopEnabled: Any
    def __init__(self):
        ...
    def validate(self, tipFilter, _):
        ...

class _PostProgressionValidator(object):
    __slots__: tuple
    _postProgressionCtrl: Any
    _isPostProgressionEnabled: Any
    def __init__(self):
        ...
    def validate(self, tipFilter, _):
        ...

def getTipsCriteria(arenaVisitor):
    ...
def showExactTip(exactTipID):
    ...
def readTips(pattern):
    ...
def _buildBattleLoadingTip(tipID, descriptionResID):
    ...
def _getRandomTipsCriteria(arenaVisitor):
    ...
def _getTipIconRes(tipID, group):
    ...
def _getTipWatchedCounter(tipID):
    ...
def _increaseTipWatchedCounter(tipID):
    ...
def _getWatchedCache():
    ...
