# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/comp7_light_event_banner.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/comp7_light_event_banner.py
from __future__ import absolute_import
import weakref
from gui.impl import backport
from gui.impl.gen import R
from account_helpers.AccountSettings import COMP7_LIGHT_BANNER_FIRST_APPEARANCE_TIMESTAMP
from comp7_core.gui.impl.lobby.event_banner import Comp7CoreEventBanner
from comp7_light.gui.comp7_light_constants import SELECTOR_BATTLE_TYPES, COMP7_LIGHT_ENTRY_POINT_ALIAS
from comp7_light.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as Comp7LightSeasonState
from comp7_light.gui.impl.lobby.tooltips.entry_point_tooltip import Comp7LightEntryPointTooltip
from comp7_light.gui.prb_control.entities.comp7_light_prb_helpers import selectComp7Light
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class Comp7LightEventBanner(Comp7CoreEventBanner):
    NAME = COMP7_LIGHT_ENTRY_POINT_ALIAS
    __comp7LightController = dependency.descriptor(IComp7LightController)

    @property
    def _modeController(self):
        return self.__comp7LightController

    @property
    def _seasonStateClazz(self):
        return Comp7LightSeasonState

    @property
    def _accountSettingsTimestampFlag(self):
        return COMP7_LIGHT_BANNER_FIRST_APPEARANCE_TIMESTAMP

    @property
    def _selectorBattleType(self):
        return SELECTOR_BATTLE_TYPES.COMP7_LIGHT

    @staticmethod
    def _selectMode():
        selectComp7Light()

    @property
    def introDescription(self):
        return backport.text(R.strings.hangar_event_banners.event.Comp7LightEntryPoint.intro.description(), level=self._vehicleLevel)

    @property
    def inProgressDescription(self):
        return backport.text(R.strings.hangar_event_banners.event.Comp7LightEntryPoint.inProgress.description(), level=self._vehicleLevel)

    @property
    def borderColor(self):
        return '#65DEFF'

    @staticmethod
    @dependency.replace_none_kwargs(modeCtrl=IComp7LightController)
    def isEntryPointAvailable(modeCtrl=None):
        return modeCtrl.hasActiveSeason()

    def createToolTipContent(self, event):
        super(Comp7LightEventBanner, self).createToolTipContent(event)
        return Comp7LightEntryPointTooltip(eventBanner=weakref.proxy(self))
