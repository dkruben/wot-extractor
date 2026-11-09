# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/ally_list.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/ally_list.py
from __future__ import absolute_import
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import BaseClientModel

class AllyListClientModel(BaseClientModel):
    __slots__ = ('showFrags', 'showVehicleTypeIcon', 'highlightElite')

    def __init__(self, showFrags, showVehicleTypeIcon, highlightElite):
        super(AllyListClientModel, self).__init__()
        self.showFrags = showFrags
        self.showVehicleTypeIcon = showVehicleTypeIcon
        self.highlightElite = highlightElite

    def __repr__(self):
        return '<AllyListClientModel>: showFrags=%s, showVehicleTypeIcon=%s, highlightElite=%s' % (
         self.showFrags, self.showVehicleTypeIcon, self.highlightElite)
