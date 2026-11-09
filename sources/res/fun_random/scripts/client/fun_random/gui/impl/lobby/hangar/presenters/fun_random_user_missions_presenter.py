# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_user_missions_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_user_missions_presenter.py
from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_progression_presenter import FunRandomProgressionPresenter
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_progression_quests_presenter import FunRandomProgressionQuestsPresenter
from gui.impl.gen import R
from gui.impl.lobby.hangar.presenters.user_missions_presenter import UserMissionsPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.battle_pass_presenter import BattlePassPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.quests_presenter import QuestsPresenter

class _BattlePassPresenter(BattlePassPresenter):
    pass


class _QuestsPresenter(QuestsPresenter):
    pass


class FunRandomUserMissionsPresenter(UserMissionsPresenter, FunProgressionWatcher):
    _CHILDREN = {(R.aliases.user_missions.hangarWidget.BattlePass()): _BattlePassPresenter, 
       (R.aliases.user_missions.hangarWidget.Quests()): _QuestsPresenter}

    def _getChildComponents(self):
        return {(R.aliases.fun_random.shared.ProgressionEntryPoint()): FunRandomProgressionPresenter, 
           (R.aliases.fun_random.shared.ProgressionQuests()): FunRandomProgressionQuestsPresenter}
