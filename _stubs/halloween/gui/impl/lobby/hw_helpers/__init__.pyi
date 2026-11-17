# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/hw_helpers/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel
from halloween_common.halloween_constants import KEY_DAILY_QUEST_TPL as KEY_DAILY_QUEST_TPL
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from halloween.gui.game_control.halloween_artefacts_controller import getBonusPriority as getBonusPriority
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel as BonusItemViewModel
from halloween.gui.impl.gen.view_models.views.lobby.widgets.hangar_carousel_vehicle_view_model import VehicleStates as VehicleStates
from halloween.gui.impl.gen.view_models.views.lobby.widgets.meta_view_model import ArtefactStates as ArtefactStates
from halloween.gui.impl.gen.view_models.views.lobby.vehicle_title_view_model import VehicleTypes as VehicleTypes, VehicleTitleViewModel as VehicleTitleViewModel
from halloween.gui.impl.lobby.hw_helpers.bonuses_formatters import getHWMetaAwardFormatter as getHWMetaAwardFormatter, getImgName as getImgName, HalloweenBonusesAwardsComposer as HalloweenBonusesAwardsComposer
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_bestiary_controller import IHalloweenBestiaryController as IHalloweenBestiaryController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from helpers import dependency as dependency
from halloween_common.halloween_constants import HWStoryChoiceSettings as HWStoryChoiceSettings
from typing import Optional as Optional, Tuple as Tuple, List as List, Dict as Dict, Any as Any
from frameworks.wulf import Array as Array
from gui.server_events.awards_formatters import PreformattedBonus as PreformattedBonus
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from gui.server_events.event_items import Quest as Quest
from halloween_common.configs.halloween_bestiary import EnemyModel as EnemyModel
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
PROMINENT_REWARD_TOOLTIP_ID = 'prominent_reward_tooltip'
INF_DISPLAY_BONUSES = 999

# decorador original: @dependency.replace_none_kwargs(...)
def isDailyKeyQuestCompleted(intCD, hwCtrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getDailyKeyQuestDescription(intCD, hwCtrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isCustomizationHangarDisabled(hwCtrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getVehicleState(vehicle, ctrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getArtefactState(artefactID, ctrl=None):
    ...
def fillRewardsForTooltips(bonusRewards, bonusModels, maxBonuseInView, skipBonuses=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def fillProminentBonus(resourceID, bonusRewards, bonusItemModel, ctrl=None):
    ...
def fillBaseBonusProperties(bonus, bonusModel):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def fillGiftVehicleModel(vehGiftModel, ctrl=None):
    ...
def getQuestSmallestFinishTimeLeft(quests):
    ...
def fillRewardsCommon(bonusRewards, bonusModels, maxBonuseInView, idGen, rewardsHighlight=None, skipBonusNames=None):
    ...
def fillRewards(artefact, bonusModels, maxBonuseInView, idGen, rewardsHighlight=None, skipBonusNames=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getEnemyByArtefactID(artefactID, hwArtefactCtrl=None, hwBestiaryCtrl=None):
    ...
def getEndingToken(choice):
    ...
