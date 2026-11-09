# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/user_missions_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7_light.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import Comp7LightOverlapCtrlMixin as Comp7LightOverlapCtrlMixin
from comp7_light.gui.impl.lobby.entry_point_presenter import EntryPointPresenter as EntryPointPresenter
from comp7_light.gui.impl.lobby.progression_quests_presenter import ProgressionQuestsPresenter as ProgressionQuestsPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.battle_pass_presenter import BattlePassPresenter as BattlePassPresenter
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.presenters.user_missions_presenter import UserMissionsPresenter as UserMissionsPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.quests_presenter import QuestsPresenter as QuestsPresenter

class _BattlePassPresenter(BattlePassPresenter, Comp7LightOverlapCtrlMixin):
    ...

class _QuestsPresenter(QuestsPresenter, Comp7LightOverlapCtrlMixin):
    ...

class Comp7LightUserMissionsPresenter(UserMissionsPresenter):
    _CHILDREN: dict
    def _getChildComponents(self):
        ...
