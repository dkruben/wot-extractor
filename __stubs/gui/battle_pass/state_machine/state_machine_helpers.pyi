# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_pass/state_machine/state_machine_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
from future.builtins import range as range
from battle_pass_common import BATTLE_PASS_OFFER_TOKEN_PREFIX as BATTLE_PASS_OFFER_TOKEN_PREFIX, BATTLE_PASS_TOKEN_3D_STYLE as BATTLE_PASS_TOKEN_3D_STYLE, BattlePassRewardReason as BattlePassRewardReason, getBattlePassPassEntitlementName as getBattlePassPassEntitlementName, getBattlePassShopEntitlementName as getBattlePassShopEntitlementName, isPostProgressionChapter as isPostProgressionChapter
from gui.battle_pass.battle_pass_helpers import getOfferTokenByGift as getOfferTokenByGift, getStyleInfoForChapter as getStyleInfoForChapter, makeChapterMediaName as makeChapterMediaName
from gui.impl.gen import R as R
from gui.impl.pub.notification_commands import EventNotificationCommand as EventNotificationCommand, NotificationEvent as NotificationEvent
from gui.shared.event_dispatcher import showBattlePass as showBattlePass
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from account_helpers.offers.events_data import OfferEventData as OfferEventData
from typing import Any as Any, Callable as Callable, Dict as Dict, List as List, Optional as Optional
_logger: _Any

# decorador original: @dependency.replace_none_kwargs(...)
def isProgressionComplete(_, battlePass=None):
    ...
def separateRewards(rewards):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def packStartEvent(rewards, data, packageRewards, starterPack, eventMethod, battlePass=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def multipleBattlePassPurchasedEventMethod(rewards, data, packageRewards, starterPack, battlePass=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def defaultEventMethod(rewards, data, packageRewards, starterPack, battlePass=None):
    ...
def packToken(tokenID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def needToShowVideo(chapterID, level, battlePass=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def processRewardsToChoose(rewardsToChoose, offers=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getOfferByGiftToken(token, offers=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _isRewardChoiceToken(token, offers=None):
    ...
