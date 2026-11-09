# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/battle_quest_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_packer import packQuestBonuses as packQuestBonuses
from comp7_light.gui.impl.lobby.comp7_light_helpers.comp7_light_mission_packer import packMissionItem as packMissionItem
from comp7_light.gui.impl.lobby.comp7_light_helpers.comp7_light_packers import getComp7LightBonusPacker as getComp7LightBonusPacker
from frameworks.wulf import ViewSettings as ViewSettings
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel as WidgetQuestModel
from gui.impl.lobby.user_missions.tooltips.quest_tooltip import BaseQuestTooltip as BaseQuestTooltip
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel
from gui.shared.missions.packers.events import DailyQuestUIDataPacker as DailyQuestUIDataPacker

class BattleQuestTooltip(BaseQuestTooltip):
    def _getSettings(self):
        ...
    def _fillViewModel(self):
        ...
    def _getRewardsSortKey(self):
        ...
