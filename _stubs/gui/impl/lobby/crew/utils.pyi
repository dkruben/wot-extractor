# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import typing as typing
from collections import namedtuple as namedtuple, defaultdict as defaultdict
import Settings as Settings
import SoundGroups as SoundGroups
from SoundGroups import CREW_GENDER_SWITCHES as CREW_GENDER_SWITCHES
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.reward_item_model import RewardItemModel as RewardItemModel
from gui.impl.gen.view_models.views.lobby.crew.common.info_tip_model import InfoTipModel as InfoTipModel
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import strcmp as strcmp, i18n as i18n, dependency as dependency
from items.components.crew_books_constants import CREW_BOOK_RARITY as CREW_BOOK_RARITY
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.crew_book import CrewBook as CrewBook
VEHICLE_TAGS_FILTER: tuple
DocumentRecord: Any
ALT_VOICES_PREVIEW: Any
BOOSTER_ICON_MAPPING: dict

class TRAINING_TIPS(CONST_CONTAINER):
    NOT_TRAINED_THIS_VEHICLE = 'notTrainedThisVehicle'
    NOT_FULL_CREW = 'notFullCrew'
    NOT_FULL_AND_NOT_TRAINED_CREW = 'notFullAndNotTrainedCrew'
    LOW_PE_CREW = 'LowPECrew'
    LOW_PE_NOT_FULL_CREW = 'LowPENotFullCrew'
    LOW_PE_NOT_TRAINED_CREW = 'LowPENotTrainedCrew'
    LOW_PE_NOT_TRAINED_NOT_FULL_CREW = 'LowPENotTrainedNotFullCrew'
    LOW_PE_TIPS_PERSONAL = 'LowPEtipsPersonal'
    WILL_FULL_TRAINED_PERSONAL = 'WillFullTrainedPersonal'
    WILL_FULL_TRAINED_FEW_MEMBERS = 'WillFullTrainedFewMembers'
    WILL_FULL_TRAINED_CREW = 'WillFullTrainedCrew'
    FULL_TRAINED_PERSONAL = 'FullTrainedPersonal'
    FULL_TRAINED_FEW_MEMBERS = 'FullTrainedFewMembers'
    ALL_FULL_TRAINED = 'AllFullTrained'
    tips: dict

def setTextFormatter(tipID, forPlaceHolders):
    ...
def getTip(tipID, tipType, **forPlaceHolders):
    ...
def loadDoNotOpenTips():
    ...
def saveDoNotOpenTip(doNotOpenTip):
    ...
def getRentCriteria():
    ...
def getDocGroupValues(tankman, config, listGetter, valueGetter, sortNeeded=True):
    ...
def jsonArgsConverter(fields=...):
    ...
def playRecruitVoiceover(voiceoverParams):
    ...
def discountPercent(value, defaultValue):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def packCompensationData(books, rewardsArray, tooltipData, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def packBoostersCompensationData(boosters, rewardsArray, tooltipData, itemsCache=None):
    ...
def convertMoneyToTuple(money):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getMetoringLicensesAmount(goodiesCache=None):
    ...
