# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/cards/styles_card.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.style_preset_model import StylePresetModel as StylePresetModel
from gui.impl.lobby.easy_tank_equip.cards.base_card import BasePreset as BasePreset, BaseCard as BaseCard
from gui.impl.lobby.easy_tank_equip.data_providers.styles_data_provider import StylesPresetInfo as StylesPresetInfo
from gui.shared.money import Money as Money
from typing import Optional as Optional

class StylesCard(BaseCard):
    def _getPreset(self):
        ...

class StylesPreset(BasePreset):
    @classmethod
    def getPresetModel(cls):
        ...
    @classmethod
    def fillPresetModel(cls, model, presetInfo, balance=None):
        ...
