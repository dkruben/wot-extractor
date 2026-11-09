# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/shared/team_utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/shared/team_utils.py
from __future__ import absolute_import
from fort_rush.gui.impl.gen.view_models.views.battle.views.fort_rush_hud_base_capture_indicator_model import FortRushBaseCaptureTeam
from fort_rush_common.fort_rush_constants import CAPTURE_POINT_NO_TEAM
from gui.battle_control import avatar_getter

def getTeamValue(ownersTeamId):
    if ownersTeamId == CAPTURE_POINT_NO_TEAM:
        return FortRushBaseCaptureTeam.NEUTRAL
    if avatar_getter.getPlayerTeam() == ownersTeamId:
        return FortRushBaseCaptureTeam.ALLY
    return FortRushBaseCaptureTeam.ENEMY
