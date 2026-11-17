# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/missions_progress/comp7_light_progression_quests_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_results.pbs_helpers.common import getBattleResults as getBattleResults
from gui.battle_results.progress.progress_helpers import getReceivedTokensInfo as getReceivedTokensInfo
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.event_model import EventStatus as EventStatus
from gui.impl.gen.view_models.views.lobby.battle_results.progression.common_battle_quest_progress_model import CommonBattleQuestProgressModel as CommonBattleQuestProgressModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.common_battle_quests_progress_model import CommonBattleQuestsProgressModel as CommonBattleQuestsProgressModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.battle_results.missions_progress.progression_presenter_interface import IProgressionCategoryPresenter as IProgressionCategoryPresenter
from gui.impl.lobby.battle_results.missions_progress.rewards_helper import packBonusesWithActualTokensConvertion as packBonusesWithActualTokensConvertion
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events import conditions as conditions
from gui.shared.missions.packers.events import TokenUIDataPacker as TokenUIDataPacker, BattleQuestUIDataPacker as BattleQuestUIDataPacker
from comp7_light.gui.impl.lobby.comp7_light_helpers.comp7_light_packers import getComp7LightBonusPacker as getComp7LightBonusPacker
from quest_xml_source import MAX_BONUS_LIMIT as MAX_BONUS_LIMIT
from comp7_light.gui.shared.event_dispatcher import showComp7LightProgressionView as showComp7LightProgressionView
import constants as constants

# base nao representavel no stub: ViewComponent[...]
class Comp7LightProgressionQuestsPresenter(IProgressionCategoryPresenter):
    _PLUGIN_PATH: str
    __categoryProgressFilter: Any
    __arenaUniqueID: Any
    __allCommonQuests: Any
    __progress: Any
    __tooltipData: Any
    __bonusesModel: Any
    def __init__(self, categoryProgressFilter, arenaUniqueID, allCommonQuests):
        ...
    @classmethod
    def getPathToResource(cls):
        ...
    @classmethod
    def getViewAlias(cls):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateProgress(self):
        ...
    def _updateModel(self):
        ...
    def __createModel(self, event, pCur, pPrev, isCompleted, questTokensConvertion, questTokensCount):
        ...
    def __getTooltipData(self, event):
        ...
    # decorador original: @args2params(...)
    def __onNavigate(self, questId, eventType):
        ...
