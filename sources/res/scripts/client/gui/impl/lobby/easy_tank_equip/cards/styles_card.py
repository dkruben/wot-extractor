# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/cards/styles_card.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/easy_tank_equip/cards/styles_card.py
import typing
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.style_preset_model import StylePresetModel
from gui.impl.lobby.easy_tank_equip.cards.base_card import BasePreset, BaseCard
if typing.TYPE_CHECKING:
    from gui.impl.lobby.easy_tank_equip.data_providers.styles_data_provider import StylesPresetInfo
    from gui.shared.money import Money
    from typing import Optional

class StylesCard(BaseCard):

    def _getPreset(self):
        return StylesPreset


class StylesPreset(BasePreset):

    @classmethod
    def getPresetModel(cls):
        return StylePresetModel()

    @classmethod
    def fillPresetModel(cls, model, presetInfo, balance=None):
        super(StylesPreset, cls).fillPresetModel(model, presetInfo, balance)
        model.setName(presetInfo.style.userName)
        model.setImage(presetInfo.style.iconUrl)
        model.setRentDuration(presetInfo.style.rentCount)
