# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/progression_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers as comp7_core_model_helpers
from comp7_light.gui.impl.gen.view_models.views.lobby.progression.progress_level_model import ProgressLevelModel as ProgressLevelModel
from comp7_light.gui.impl.lobby.comp7_light_helpers.comp7_light_packers import getComp7LightBonusPacker as getComp7LightBonusPacker, getComp7LightEventUIDataPacker as getComp7LightEventUIDataPacker
from comp7_light.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as SeasonState
from comp7_light.gui.impl.gen.view_models.views.lobby.year_model import YearState as YearState
from comp7_light.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7_light.gui.shared.event_dispatcher import showComp7LightInfoPage as showComp7LightInfoPage
from comp7_light.skeletons.gui.game_control import IComp7LightProgressionController as IComp7LightProgressionController
from comp7_light.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_LIGHT_TOOLTIPS
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from comp7_light.gui.impl.gen.view_models.views.lobby.progression.progression_view_model import ProgressionViewModel as ProgressionViewModel

class ProgressionView(SubModelPresenter):
    __slots__: tuple
    __comp7LightController: Any
    __comp7LightProgressionController: Any
    __eventsCache: Any
    __tooltipData: Any
    __bonuses: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def viewModel(self):
        ...
    def getParentWindow(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onClose(self):
        ...
    def __onAboutClicked(self):
        ...
    def __updateMissionVisitedArray(self, missionVisitedArray, questsIDs):
        ...
    def __onSyncCompleted(self, *_):
        ...
    def __updateProgressionPoints(self):
        ...
    def __updateModel(self):
        ...
    def __updateSchedule(self):
        ...
    def __updateProgression(self, data, model):
        ...
    def __updateBattleQuestsCards(self, battleQuestsModel, data):
        ...
    def __markAsVisited(self, data):
        ...
