# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/user_missions_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7.gui.Scaleform.genConsts.COMP7_HANGAR_ALIASES import COMP7_HANGAR_ALIASES as COMP7_HANGAR_ALIASES
from comp7.gui.impl.lobby.entry_point_presenter import EntryPointPresenter as EntryPointPresenter
from comp7.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import Comp7OverlapCtrlMixin as Comp7OverlapCtrlMixin
from comp7.gui.impl.lobby.weekly_quests_widget_presenter import WeeklyQuestsWidgetPresenter as WeeklyQuestsWidgetPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.battle_pass_presenter import BattlePassPresenter as BattlePassPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.event_banners_presenter import EventBannersPresenter as EventBannersPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.quests_presenter import QuestsPresenter as QuestsPresenter
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.presenters.user_missions_presenter import UserMissionsPresenter as UserMissionsPresenter

class _BattlePassPresenter(BattlePassPresenter, Comp7OverlapCtrlMixin):
    ...

class _QuestsPresenter(QuestsPresenter, Comp7OverlapCtrlMixin):
    ...

class _EventBannersPresenter(EventBannersPresenter, Comp7OverlapCtrlMixin):
    __ALLOWED_EVENT_IDS: tuple
    def _getEventEntries(self):
        ...

class Comp7UserMissionsPresenter(UserMissionsPresenter):
    _CHILDREN: dict
    def _getChildComponents(self):
        ...
