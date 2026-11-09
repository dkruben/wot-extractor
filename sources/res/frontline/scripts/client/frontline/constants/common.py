# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/constants/common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/constants/common.py
from __future__ import absolute_import
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineState, FrontlineConst
from gui.impl.common.ammunition_panel.ammunition_groups_controller import RANDOM_GROUPS, GroupData
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_constants import AmmunitionPanelConstants
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
STATES_MAP = {(FrontlineState.ANNOUNCE): (EventBannerState.ANNOUNCE), 
   (FrontlineState.ACTIVE): (EventBannerState.IN_PROGRESS), 
   (FrontlineState.FROZEN): (EventBannerState.INACTIVE), 
   (FrontlineState.FINISHED): (EventBannerState.FINISHED), 
   (FrontlineState.INTRO): (EventBannerState.INTRO)}
FRONTLINE_GROUPS = RANDOM_GROUPS + (
 GroupData(AmmunitionPanelConstants.NO_GROUP, (FrontlineConst.BATTLE_ABILITIES,)),)
HIDDEN_PARAMS = [
 'inactivationDelay',
 '#epic_battle:abilityInfo/params/fl_regenerationKit/minesDamageReduceFactor/value',
 'projectilesNumber']
PLUS_SIGN = '+'
SKILL_PARAM_SIGN = {'increaseFactors/crewRolesFactor': PLUS_SIGN, 
   'resupplyCooldownFactor': PLUS_SIGN, 
   'resupplyHealthPointsFactor': PLUS_SIGN, 
   'captureSpeedFactor': PLUS_SIGN, 
   'captureBlockBonusTime': PLUS_SIGN}
