# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_user_missions_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher as FunProgressionWatcher
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_progression_presenter import FunRandomProgressionPresenter as FunRandomProgressionPresenter
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_progression_quests_presenter import FunRandomProgressionQuestsPresenter as FunRandomProgressionQuestsPresenter
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.presenters.user_missions_presenter import UserMissionsPresenter as UserMissionsPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.battle_pass_presenter import BattlePassPresenter as BattlePassPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.quests_presenter import QuestsPresenter as QuestsPresenter

class _BattlePassPresenter(BattlePassPresenter):
    ...

class _QuestsPresenter(QuestsPresenter):
    ...

class FunRandomUserMissionsPresenter(UserMissionsPresenter, FunProgressionWatcher):
    _CHILDREN: dict
    def _getChildComponents(self):
        ...
