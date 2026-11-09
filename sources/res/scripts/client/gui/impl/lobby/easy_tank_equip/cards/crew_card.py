# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/cards/crew_card.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/easy_tank_equip/cards/crew_card.py
import typing, nations
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.crew_preset_model import CrewPresetModel
from gui.impl.lobby.crew.crew_helpers.model_setters import setTankmanModel, setTmanSkillsModel
from gui.impl.lobby.easy_tank_equip.cards.base_card import BaseCard, BasePreset
if typing.TYPE_CHECKING:
    from gui.impl.lobby.easy_tank_equip.data_providers.crew_data_provider import CrewPresetInfo
    from gui.shared.money import Money
    from typing import Optional

class CrewCard(BaseCard):

    def _getPreset(self):
        return CrewPreset

    def _onPricesUpdated(self, balance):
        pass


class CrewPreset(BasePreset):

    @classmethod
    def getPresetModel(cls):
        return CrewPresetModel()

    @classmethod
    def fillPresetModel(cls, model, presetInfo, balance=None):
        super(CrewPreset, cls).fillPresetModel(model, presetInfo, balance)
        model.setType(presetInfo.presetType)
        model.setRecruitsCount(presetInfo.recruitsCount)
        cls.__fillPresetTankmenModel(model, presetInfo)

    @classmethod
    def __fillPresetTankmenModel(cls, model, presetInfo):
        tankmenModels = model.getTankmen()
        tankmanModel = model.getTankmenType()
        tankmenModels.clear()
        for tankmanIndex, tankman in enumerate(presetInfo.tankmen):
            if tankman is not None:
                tm = tankmanModel()
                setTankmanModel(tm, tankman, tmanNativeVeh=presetInfo.tankmenNativeVeh[tankmanIndex])
                setTmanSkillsModel(tm.skills, tankman, fillBonusSkills=True)
                tm.setNation(nations.NAMES[tankman.nationID])
                tankmenModels.addViewModel(tm)

        tankmenModels.invalidate()
        return
