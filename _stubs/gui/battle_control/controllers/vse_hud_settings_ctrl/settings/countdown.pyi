# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/countdown.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import TextClientModel as TextClientModel

class CountdownClientModel(TextClientModel):
    __slots__: tuple
    header: Any
    subheader: Any
    battleStartMessage: Any
    def __init__(self, header, subheader, battleStartMessage):
        ...
    def getHeader(self):
        ...
    def getSubheader(self):
        ...
    def getBattleStartMessage(self):
        ...
    def __repr__(self):
        ...
