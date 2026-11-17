# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/widgets/user_missions_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.presenters.user_missions_presenter import UserMissionsPresenter as UserMissionsPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.battle_pass_presenter import BattlePassPresenter as BattlePassPresenter
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from last_stand.gui.impl.lobby.gsw_cards.quests_card_presenter import QuestsCardPresenter as QuestsCardPresenter
from last_stand.gui.impl.lobby.gsw_cards.reward_path_presenter import RewardPathCardPresenter as RewardPathCardPresenter
from last_stand.gui.impl.lobby.gsw_cards.shop_card_presenter import ShopCardPresenter as ShopCardPresenter
from last_stand.gui.impl.lobby.tooltips.battle_pass_in_progress_tooltip import LSBattlePassInProgressTooltipView as LSBattlePassInProgressTooltipView
from last_stand.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import LastStandOverlapCtrlMixin as LastStandOverlapCtrlMixin
from frameworks.wulf import View as View

class _BattlePassPresenter(BattlePassPresenter, LastStandOverlapCtrlMixin):
    _battlePassController: Any
    @property
    def isPaused(self):
        ...
    def _createInProgressTooltipView(self):
        ...
    def isVisible(self):
        ...

class _QuestsCardPresenter(TooltipPositionerMixin, LastStandOverlapCtrlMixin, QuestsCardPresenter):
    def _onLoading(self, *args, **kwargs):
        ...
    def isVisible(self):
        ...

class LastStandUserMissionsPresenter(UserMissionsPresenter):
    _CHILDREN: dict
