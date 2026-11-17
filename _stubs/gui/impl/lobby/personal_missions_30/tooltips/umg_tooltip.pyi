# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/tooltips/umg_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import nations as nations
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import ROLE_TYPE_TO_COMMON_ROLE as ROLE_TYPE_TO_COMMON_ROLE
from frameworks.wulf import ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import getBonusesWithModifyTokens as getBonusesWithModifyTokens
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from future.utils import viewvalues as viewvalues
from personal_missions import PM_BRANCH as PM_BRANCH, PM_BRANCH_TO_FREE_TOKEN_NAME as PM_BRANCH_TO_FREE_TOKEN_NAME
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.PERSONAL_MISSIONS_30 import PERSONAL_MISSIONS_30 as PERSONAL_MISSIONS_30
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.tooltips.umg_tooltip_model import UmgTooltipModel as UmgTooltipModel, MissionConditionModel as MissionConditionModel
from gui.impl.lobby.personal_missions_30.bonus_packers import getBonusPacker as getBonusPacker, packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData
from gui.impl.lobby.personal_missions_30.views_helpers import getMissionConfigData as getMissionConfigData
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.personal_progress.formatters import PMTooltipConditionsFormatters as PMTooltipConditionsFormatters
from skeletons.gui.server_events import IEventsCache as IEventsCache
from typing import Optional as Optional
from gui.server_events.event_items import PersonalMission as PersonalMission
from gui.server_events.bonuses import SimpleBonus as SimpleBonus

class UmgPersonalMissionsTooltip(ViewImpl):
    eventsCache: Any
    _branchID: Any
    _missionId: Any
    def __init__(self, campaignId, missionId):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillViewModel(self):
        ...
    def _fillCompleteState(self, vm):
        ...
    def _getOperation(self, quest):
        ...
    @staticmethod
    def _fillConditions(vm, quest):
        ...
    def _fillRewards(self, vm, quest):
        ...
    def _packPM1n2(self, bonuses, packer, rewards, quest):
        ...
    def _getMissionState(self, quest):
        ...
    @staticmethod
    def _getMissionIcon(operation, quest):
        ...
