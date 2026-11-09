# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/user_missions/fort_rush_user_missions_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/user_missions/fort_rush_user_missions_presenter.py
from __future__ import absolute_import
from fort_rush.gui.impl.lobby.presenters.fort_rush_progression_entry_point_presenter import FortRushProgressionEntryPointPresenter
from fort_rush.gui.impl.lobby.user_missions.fort_rush_quests_presenter import FortRushQuestsPresenter
from gui.impl.gen import R
from gui.impl.lobby.hangar.presenters.user_missions_presenter import UserMissionsPresenter

class FortRushUserMissionsPresenter(UserMissionsPresenter):
    _WIDGET_ALIAS = R.aliases.user_missions.hangarWidget
    _FORT_RUSH_ALIAS = R.aliases.fort_rush.shared
    _CHILDREN = {(_WIDGET_ALIAS.Quests()): FortRushQuestsPresenter, 
       (_FORT_RUSH_ALIAS.Progression()): FortRushProgressionEntryPointPresenter}
