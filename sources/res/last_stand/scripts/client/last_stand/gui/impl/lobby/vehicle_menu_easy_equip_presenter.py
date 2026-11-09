# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/vehicle_menu_easy_equip_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/lobby/vehicle_menu_easy_equip_presenter.py
from __future__ import absolute_import
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel
from gui.prb_control.entities.base.listener import IPrbListener
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter

class LSEasyEquipMenuEntrySubPresenter(BaseMenuEntrySubPresenter, IPrbListener):

    def _getState(self):
        return VehicleMenuModel.DISABLED

    def onNavigate(self):
        pass
