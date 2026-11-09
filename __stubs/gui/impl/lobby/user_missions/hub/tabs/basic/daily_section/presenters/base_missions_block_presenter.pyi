# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/daily_section/presenters/base_missions_block_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl.lobby.user_missions.hangar_widget.utils import DailyMissionItemPacker as DailyMissionItemPacker
from gui.impl.lobby.user_missions.hub.tabs.basic.daily_section.presenters.base_block_presenter import BaseBlockPresenter as BaseBlockPresenter
from gui.impl.pub.view_impl import TViewModel as TViewModel
from gui.shared.missions.packers.bonus import getDailyMissionsBonusPacker as getDailyMissionsBonusPacker
from gui.shared.missions.packers.events import packQuestBonusModelAndTooltipData as packQuestBonusModelAndTooltipData
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.common.mission_base_model import MissionBaseModel as MissionBaseModel
from gui.server_events.event_items import Quest as Quest

# base nao representavel no stub: BaseBlockPresenter[...]
class BaseMissionsBlockPresenter:
    def __init__(self, model):
        ...
    def _onLeaveTab(self):
        ...
    def _fillMissionModel(self, mm, quest):
        ...
    def _disableCompletedQuestAnimation(self, vm):
        ...
