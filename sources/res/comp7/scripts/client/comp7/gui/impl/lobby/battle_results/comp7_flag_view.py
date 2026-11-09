# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/comp7_flag_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/battle_results/comp7_flag_view.py
from __future__ import absolute_import
from gui.impl.lobby.battle_results.flag_view import FlagView, _TEXTURE_PATH
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_flag_view_model import Comp7FlagViewModel
from gui.impl.pub import WindowImpl
from frameworks.wulf import WindowFlags
from gui.impl.gen import R

class Comp7FlagWindow(WindowImpl):

    def __init__(self):
        super(Comp7FlagWindow, self).__init__(wndFlags=WindowFlags.SURFACE, content=Comp7FlagView(), name=_TEXTURE_PATH)


class Comp7FlagView(FlagView):
    _VIEW_SETTINGS_LAYOUT_ID = R.views.comp7.mono.lobby.flag()
    _VIEW_MODEL = Comp7FlagViewModel

    def _getLsmStateClass(self):
        from comp7.gui.impl.lobby.battle_results.states import Comp7PostBattleResultsState
        return Comp7PostBattleResultsState

    @property
    def viewModel(self):
        return super(Comp7FlagView, self).getViewModel()
