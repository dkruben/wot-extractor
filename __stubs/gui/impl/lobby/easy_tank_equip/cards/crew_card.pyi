# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/cards/crew_card.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import nations as nations
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.crew_preset_model import CrewPresetModel as CrewPresetModel
from gui.impl.lobby.crew.crew_helpers.model_setters import setTankmanModel as setTankmanModel, setTmanSkillsModel as setTmanSkillsModel
from gui.impl.lobby.easy_tank_equip.cards.base_card import BaseCard as BaseCard, BasePreset as BasePreset
from gui.impl.lobby.easy_tank_equip.data_providers.crew_data_provider import CrewPresetInfo as CrewPresetInfo
from gui.shared.money import Money as Money
from typing import Optional as Optional

class CrewCard(BaseCard):
    def _getPreset(self):
        ...
    def _onPricesUpdated(self, balance):
        ...

class CrewPreset(BasePreset):
    @classmethod
    def getPresetModel(cls):
        ...
    @classmethod
    def fillPresetModel(cls, model, presetInfo, balance=None):
        ...
    @classmethod
    def __fillPresetTankmenModel(cls, model, presetInfo):
        ...
