# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/progression_quests_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_packer import packQuestBonuses as packQuestBonuses
from comp7_light.gui.impl.gen.view_models.views.lobby.progression_quests_model import ProgressionQuestsModel as ProgressionQuestsModel
from comp7_light.gui.impl.lobby.comp7_light_helpers.account_settings import getLastSeenQuestData as getLastSeenQuestData, setLastSeenQuestData as setLastSeenQuestData
from comp7_light.gui.impl.lobby.comp7_light_helpers.comp7_light_mission_packer import packMissionItem as packMissionItem
from comp7_light.gui.impl.lobby.comp7_light_helpers.comp7_light_packers import getComp7LightBonusPacker as getComp7LightBonusPacker
from comp7_light.gui.impl.lobby.tooltips.battle_quest_tooltip import BattleQuestTooltip as BattleQuestTooltip
from comp7_light.gui.impl.lobby.tooltips.battle_quests_done_tooltip import BattleQuestsDoneTooltip as BattleQuestsDoneTooltip
from comp7_light.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import Comp7LightOverlapCtrlMixin as Comp7LightOverlapCtrlMixin
from frameworks.wulf import Array as Array
from comp7_light.gui.shared.event_dispatcher import showComp7LightProgressionView as showComp7LightProgressionView
from comp7_light.skeletons.gui.game_control import IComp7LightProgressionController as IComp7LightProgressionController
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel as WidgetQuestModel
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.missions.packers.events import DailyQuestUIDataPacker as DailyQuestUIDataPacker
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7LightController as IComp7LightController
from skeletons.gui.server_events import IEventsCache as IEventsCache

# base nao representavel no stub: ViewComponent[...]
class ProgressionQuestsPresenter(TooltipPositionerMixin, Comp7LightOverlapCtrlMixin, IGlobalListener):
    __eventsCache: Any
    __comp7LightController: Any
    __comp7LightProgressionController: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _finalize(self):
        ...
    def _updateViewModel(self):
        ...
    def _rawUpdate(self):
        ...
    def __updateBattleQuestData(self, quest):
        ...
    def __onMarkAsViewed(self):
        ...
    def __onOpenProgression(self):
        ...
