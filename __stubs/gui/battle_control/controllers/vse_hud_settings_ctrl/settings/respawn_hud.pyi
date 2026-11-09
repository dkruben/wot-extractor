# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/respawn_hud.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import TextClientModel as TextClientModel

class RespawnHUDClientModel(TextClientModel):
    __slots__: tuple
    dynamicRespawnHeader: Any
    dynamicRespawnSubheader: Any
    staticRespawnHeader: Any
    staticRespawnSubheader: Any
    battleOverHeader: Any
    battleOverSubheader: Any
    staticRespawnSound: Any
    dynamicRespawnSound: Any
    battleOverSound: Any
    showLivesInAlliesList: Any
    showLivesInTankPanel: Any
    def __init__(self, dynamicRespawnHeader, dynamicRespawnSubheader, staticRespawnHeader, staticRespawnSubheader, battleOverHeader, battleOverSubheader, staticRespawnSound, dynamicRespawnSound, battleOverSound, showLivesInAlliesList, showLivesInTankPanel):
        ...
    def getDynamicRespawnHeader(self):
        ...
    def getDynamicRespawnSubheader(self):
        ...
    def getStaticRespawnHeader(self):
        ...
    def getStaticRespawnSubheader(self):
        ...
    def getBattleOverHeader(self):
        ...
    def getBattleOverSubheader(self):
        ...
    def __repr__(self):
        ...
