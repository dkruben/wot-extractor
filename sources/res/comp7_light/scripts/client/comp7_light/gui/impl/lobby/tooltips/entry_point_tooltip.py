# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/entry_point_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/entry_point_tooltip.py
from __future__ import absolute_import
from comp7_core.gui.impl.lobby.tooltips.entry_point_tooltip import Comp7CoreEntryPointTooltip
from comp7_light.gui.impl.gen.view_models.views.lobby.enums import SeasonName as Comp7LightSeasonName
from comp7_light.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as Comp7LightSeasonState
from comp7_light.gui.impl.gen.view_models.views.lobby.tooltips.entry_point_tooltip_model import EntryPointTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class Comp7LightEntryPointTooltip(Comp7CoreEntryPointTooltip):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    def __init__(self, eventBanner):
        settings = ViewSettings(R.views.comp7_light.mono.lobby.entry_point_tooltip())
        settings.model = EntryPointTooltipModel()
        super(Comp7LightEntryPointTooltip, self).__init__(settings, eventBanner=eventBanner)

    @property
    def _modeController(self):
        return self.__comp7LightController

    @property
    def _seasonStateClazz(self):
        return Comp7LightSeasonState

    @property
    def _seasonNameClazz(self):
        return Comp7LightSeasonName
