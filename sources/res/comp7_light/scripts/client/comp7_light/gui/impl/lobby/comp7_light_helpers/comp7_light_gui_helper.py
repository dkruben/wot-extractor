# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/comp7_light_helpers/comp7_light_gui_helper.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/comp7_light_helpers/comp7_light_gui_helper.py
from __future__ import absolute_import
from account_helpers import AccountSettings
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController
from account_helpers.AccountSettings import COMP7_LIGHT_UI_SECTION, COMP7_LIGHT_LAST_SEASON

@dependency.replace_none_kwargs(comp7LightController=IComp7LightController)
def isComp7LightIntroShouldBeShown(comp7LightController=None):
    if not comp7LightController.isAvailable():
        return False
    season = comp7LightController.getCurrentSeason()
    if not season:
        return False
    settings = AccountSettings.getUIFlag(COMP7_LIGHT_UI_SECTION)
    return settings.get(COMP7_LIGHT_LAST_SEASON) != season.getNumber()


@dependency.replace_none_kwargs(comp7LightController=IComp7LightController)
def updateComp7LightLastSeason(comp7LightController=None):
    season = comp7LightController.getCurrentSeason(includePreannounced=True)
    if not season:
        return
    settings = AccountSettings.getUIFlag(COMP7_LIGHT_UI_SECTION)
    settings[COMP7_LIGHT_LAST_SEASON] = season.getNumber()
    AccountSettings.setUIFlag(COMP7_LIGHT_UI_SECTION, settings)
