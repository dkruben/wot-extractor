# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/clan_supply/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/clan_supply/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class ClanSupplyRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.CLAN_SUPPLY_GET_QUESTS): (self.__getQuests), 
           (WebRequestDataType.CLAN_SUPPLY_POST_QUESTS): (self.__postQuests), 
           (WebRequestDataType.CLAN_SUPPLY_CLAIM_QUESTS_REWARDS): (self.__claimQuestRewards), 
           (WebRequestDataType.CLAN_SUPPLY_GET_PROGRESSION_SETTINGS): (self.__getProgressionSettings), 
           (WebRequestDataType.CLAN_SUPPLY_GET_PROGRESSION_PROGRESS): (self.__getProgressionProgress), 
           (WebRequestDataType.CLAN_SUPPLY_PURCHASE_PROGRESSION_STAGE): (self.__purchaseProgressionStage)}
        return handlers

    def __getQuests(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clan_supply', 'get_clan_supply_quests'))

    def __postQuests(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clan_supply', 'post_clan_supply_quests'))

    def __claimQuestRewards(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clan_supply', 'claim_quest_rewards'))

    def __getProgressionSettings(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clan_supply', 'get_progression_settings'))

    def __getProgressionProgress(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clan_supply', 'get_progression_progress'))

    def __purchaseProgressionStage(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('clan_supply', 'purchase_progression_stage'), *ctx.getRequestArgs())
