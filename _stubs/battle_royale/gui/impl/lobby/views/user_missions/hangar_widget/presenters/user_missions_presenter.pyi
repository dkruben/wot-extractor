# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/user_missions/hangar_widget/presenters/user_missions_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.overlap_ctrl import BattleRoyaleOverlapCtrlMixin as BattleRoyaleOverlapCtrlMixin
from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.presenters.event_shop_presenter import BattleRoyaleEventShopPresenter as BattleRoyaleEventShopPresenter
from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.presenters.progression_presenter import BattleRoyaleProgressionPresenter as BattleRoyaleProgressionPresenter
from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.presenters.quests_presenter import BattleRoayaleQuestsPresenter as BattleRoayaleQuestsPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.battle_pass_presenter import BattlePassPresenter as BattlePassPresenter
from battle_royale.gui.impl.lobby.tooltips.battle_pass_in_progress_tooltip import BattleRoyaleBattlePassInProgressTooltipView as BattleRoyaleBattlePassInProgressTooltipView
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.presenters.user_missions_presenter import UserMissionsPresenter as UserMissionsPresenter

class _BattlePassPresenter(BattlePassPresenter, BattleRoyaleOverlapCtrlMixin):
    def _createInProgressTooltipView(self):
        ...

class BattleRoyaleUserMissionsPresenter(UserMissionsPresenter):
    _WIDGET_ALIAS = R.aliases.user_missions.hangarWidget
    _BATTLE_ROYALE_WIDGET_ALIAS = R.aliases.battle_royale.hangarWidget
    _CHILDREN: dict
    def _addChild(self, posId):
        ...
