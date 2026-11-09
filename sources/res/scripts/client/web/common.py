# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/common.py
from __future__ import absolute_import
import typing
from gui.battle_pass.battle_pass_constants import ChapterState
from gui.game_control.wallet import WalletController
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController, IWalletController
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.utils.requesters import IStatsRequester
if typing.TYPE_CHECKING:
    from typing import Dict
_BATTLE_PASS_CHAPTER_STATE_NAME = {(ChapterState.NOT_STARTED): 'not_started', 
   (ChapterState.PAUSED): 'paused', 
   (ChapterState.ACTIVE): 'active', 
   (ChapterState.COMPLETED): 'completed'}

def formatBalance(stats):
    actualMoney = stats.actualMoney.toDict()
    balanceData = {Currency.currencyExternalName(currency): actualMoney.get(currency, 0) for currency in Currency.ALL}
    balanceData.update(stats.dynamicCurrencies)
    balanceData['free_xp'] = stats.freeXP
    return balanceData


@dependency.replace_none_kwargs(wallet=IWalletController, itemsCache=IItemsCache)
def formatWalletCurrencyStatuses(wallet=None, itemsCache=None):
    statuses = {Currency.currencyExternalName(currencyCode): WalletController.STATUS.getKeyByValue(wallet.status).lower() for currencyCode in Currency.ALL}
    statuses.update({currencyCode: WalletController.STATUS.getKeyByValue(wallet.status).lower() for currencyCode in itemsCache.items.stats.dynamicCurrencies})
    return statuses


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def formatBattlePassInfo(battlePass=None):
    return {'isActive': (not battlePass.isPaused() and battlePass.isVisible()), 
       'season': {'num': (battlePass.getSeasonNum()), 
                  'leftTime': (battlePass.getFinalOfferTime())}, 
       'chapters': {chapterID: {'isBought': (battlePass.isBought(chapterID=chapterID)), 'state': (_BATTLE_PASS_CHAPTER_STATE_NAME[battlePass.getChapterState(chapterID)])} for chapterID in battlePass.getMainChapterIDs()}}
