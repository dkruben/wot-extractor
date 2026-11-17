# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_pass/battle_pass_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import itertools as itertools
import logging as logging
from collections import namedtuple as namedtuple
from future.utils import viewvalues as viewvalues, viewitems as viewitems
import nations as nations
import typing as typing
from battle_pass_common import BattlePassConsts as BattlePassConsts, BattlePassTankmenSource as BattlePassTankmenSource, HOLIDAY_SEASON_OFFSET as HOLIDAY_SEASON_OFFSET, isPostProgressionChapter as isPostProgressionChapter, FinalReward as FinalReward
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, QUEUE_TYPE as QUEUE_TYPE
from enum import Enum as Enum
from items.tankmen import getNationGroups as getNationGroups
from nations import INDICES as INDICES
from shared_utils import findFirst as findFirst, first as first
from account_helpers.AccountSettings import AccountSettings as AccountSettings, IS_BATTLE_PASS_COLLECTION_SEEN as IS_BATTLE_PASS_COLLECTION_SEEN, IS_BATTLE_PASS_EXTRA_START_NOTIFICATION_SEEN as IS_BATTLE_PASS_EXTRA_START_NOTIFICATION_SEEN, EXTRA_CHAPTERS_VIDEO_SHOWN as EXTRA_CHAPTERS_VIDEO_SHOWN, BUY_ANIMATIONS_WAS_SHOWN as BUY_ANIMATIONS_WAS_SHOWN, IS_BATTLE_PASS_START_ANIMATION_SEEN as IS_BATTLE_PASS_START_ANIMATION_SEEN, IS_BATTLE_PASS_START_NOTIFICATION_SEEN as IS_BATTLE_PASS_START_NOTIFICATION_SEEN, LAST_BATTLE_PASS_CYCLES_SEEN as LAST_BATTLE_PASS_CYCLES_SEEN, LAST_BATTLE_PASS_POINTS_SEEN as LAST_BATTLE_PASS_POINTS_SEEN
from account_helpers.settings_core.settings_constants import BattlePassStorageKeys as BattlePassStorageKeys
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.price_model import PriceModel as PriceModel
from gui.impl.gen.view_models.views.lobby.customization.attachments_preview.attachments_preview_model import AttachmentsPreviewFeature as AttachmentsPreviewFeature
from gui.impl.wrappers.user_compound_price_model import PriceModelBuilder as PriceModelBuilder
from gui.impl.gen.view_models.views.lobby.vehicle_preview.top_panel.top_panel_tabs_model import TabID as TabID
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.server_events.bonuses import VehiclesBonus as VehiclesBonus, parseAttachmentsSetToken as parseAttachmentsSetToken, AttachmentsSetTokenBonus as AttachmentsSetTokenBonus
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.formatters import time_formatters as time_formatters
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from gui.shared.event_dispatcher import showBattlePassStyleProgressionPreview as showBattlePassStyleProgressionPreview, showStylePreview as showStylePreview, showVehicleHubOverview as showVehicleHubOverview, showAttachmentsSetPreview as showAttachmentsSetPreview
from helpers import dependency as dependency, time_utils as time_utils
from helpers.dependency import replace_none_kwargs as replace_none_kwargs
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from web.web_client_api.common import ItemPackEntry as ItemPackEntry, ItemPackType as ItemPackType
from typing import Dict as Dict, List as List, Optional as Optional, Tuple as Tuple
from gui.impl.wrappers.user_compound_price_model import UserCompoundPriceModel as UserCompoundPriceModel
from gui.server_events.bonuses import TmanTemplateTokensBonus as TmanTemplateTokensBonus
_logger: Any
_CUSTOMIZATION_BONUS_NAME = 'customizations'
TANKMAN_BONUS_NAME = 'tmanToken'
TokenPositions: Any
_BATTLE_PASS_PRICE_CURRENCY_PRIORITY: tuple

class BattlePassMediaPatterns(str, Enum):
    STYLE = 'style'
    MEDIA = 'media'
    CHAPTER = 'ch'
    LEVEL = 'lvl'
    PART = 'pt'

class ChapterType(str, Enum):
    COMMON = 'common'
    EXTRA = 'extra'
    HOLIDAY = 'holiday'
    POST_PROGRESSION = 'postProgression'

# decorador original: @dependency.replace_none_kwargs(...)
def getChapterType(chapterID, battlePass=None):
    ...
def isBattlePassActiveSeason():
    ...
def getPointsInfoStringID(gameMode=...):
    ...
def isSeasonEndingSoon():
    ...
def getFormattedTimeLeft(seconds):
    ...
def getBattlePassUrl(urlPathName):
    ...
def getInfoPageURL():
    ...
def getExtraInfoPageURL():
    ...
def getIntroVideoURL():
    ...
def getExtraVideoURL():
    ...
def getIntroSlidesNames():
    ...
def isIntroEnabled():
    ...
def isIntroVideoEnabled():
    ...
def isExtraIntroVideoEnabled():
    ...
def getBattlePassSetting(settingName):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getMainChaptersNumbers(battlePass=None):
    ...
def getSupportedArenaBonusTypeFor(queueType, isInUnit):
    ...
def getSupportedCurrentArenaBonusType(queueType=None):
    ...
def getTankmanFirstNationGroup(tankmanGroupName):
    ...
def makeProgressionStyleMediaName(chapterID, styleLevel):
    ...
def makeChapterMediaName(chapterID, part=''):
    ...
def asBPVideoName(filename):
    ...
def showBPFullscreenVideo(videoName, audioName, onVideoClosed=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getAllFinalRewards(chapterID, battlePass=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getRewardSourceByType(reward, chapter, battlePass=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getStyleForChapter(chapter, battlePass=None, c11nService=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getStyleInfoForChapter(chapter, battlePass=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getAttachmentsSetInfoForChapter(chapter, battlePass=None, awardSource=...):
    ...
# decorador original: @replace_none_kwargs(...)
def getAttachmentsSetTokenForChapter(chapter, battlePass=None, awardSource=...):
    ...
# decorador original: @replace_none_kwargs(...)
def getTimeExpirations(chapterID, battlePass=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getVehicleInfoForChapter(chapter, battlePass=None, c11nService=None, awardSource=...):
    ...
def getRecruitNation(recruitInfo):
    ...
def getTankmanInfo(bonus):
    ...
def getDataByTankman(tankman):
    ...
# decorador original: @replace_none_kwargs(...)
def getReceivedTankmenCount(tankman, tankmanPostfix='', battlePass=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getTankmenShopPackages(battlePass=None):
    ...
def getOfferTokenByGift(tokenID):
    ...
def fillBattlePassCompoundPrice(compoundPriceModel, compoundPrice):
    ...
def getCompoundPriceDefaultID(compoundPrice):
    ...
# decorador original: @replace_none_kwargs(...)
def getFinalTankmen(chapterID, awardType, battlePass=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getChapterForTankmenScreen(screenID, battlePass=None):
    ...
def updateBuyAnimationFlag(chapterID):
    ...
def extractCompensationMoney(data):
    ...
# decorador original: @replace_none_kwargs(...)
def updateBattlePassSettings(data, battlePass=None):
    ...
def _updateClientSettings():
    ...
def _updateServerSettings(data):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showFinalRewardPreviewBattlePassState(chapterID, bonusID=None, level=None, itemsCache=None):
    ...
