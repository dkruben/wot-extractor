# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/comp7_light_flag_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/comp7_light_flag_view.py
from __future__ import absolute_import
from gui.impl.lobby.battle_results.flag_view import FlagView, _TEXTURE_PATH
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_flag_view_model import Comp7LightFlagViewModel
from gui.impl.pub import WindowImpl
from frameworks.wulf import WindowFlags
from gui.impl.gen import R

class Comp7LightFlagWindow(WindowImpl):

    def __init__(self):
        super(Comp7LightFlagWindow, self).__init__(wndFlags=WindowFlags.SURFACE, content=Comp7LightFlagView(), name=_TEXTURE_PATH)


class Comp7LightFlagView(FlagView):
    _VIEW_SETTINGS_LAYOUT_ID = R.views.comp7_light.mono.lobby.flag()
    _VIEW_MODEL = Comp7LightFlagViewModel

    def _getLsmStateClass(self):
        from comp7_light.gui.impl.lobby.battle_results.states import Comp7LightPostBattleResultsState
        return Comp7LightPostBattleResultsState

    @property
    def viewModel(self):
        return super(Comp7LightFlagView, self).getViewModel()
