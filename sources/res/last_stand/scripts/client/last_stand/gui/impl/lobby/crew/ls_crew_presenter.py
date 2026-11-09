# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/crew/ls_crew_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/lobby/crew/ls_crew_presenter.py
from __future__ import absolute_import
from CurrentVehicle import g_currentVehicle
from gui.shared.gui_items import checkForTags
from gui.impl.lobby.hangar.presenters.crew_presenter import CrewPresenter
from items.tankmen import MAX_SKILL_LEVEL

class LSCrewPresenter(CrewPresenter):

    def _createTankmanModel(self, tman, battleBoosterBonus, isQuickTrainingEnabled, vehicleBonusDetails, vehicleCrewBoosterBonusDetails, optDeviceBonuses):
        model = super(LSCrewPresenter, self)._createTankmanModel(tman, battleBoosterBonus, isQuickTrainingEnabled, vehicleBonusDetails, vehicleCrewBoosterBonusDetails, optDeviceBonuses)
        if g_currentVehicle.isPresent() and checkForTags(g_currentVehicle.item.tags, 'lockCrewSkills'):
            model.setNewPerksCount(0)
            model.setNewBonusPerksCount(0)
            model.setTrainingProgress(MAX_SKILL_LEVEL)
        return model
