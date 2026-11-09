# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/secondary_objectives/settings_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.daapi.view.battle.pve_base.base.settings_model import BaseWidgetSettingsModel as BaseWidgetSettingsModel
from pve_battle_hud import SecondaryObjectiveState as SecondaryObjectiveState

class SecondaryObjectiveServerModel(BaseWidgetSettingsModel):
    __slots__: tuple
    timer: Any
    finishTime: Any
    progress: Any
    params: Any
    def __init__(self, id, type, state, timer, finishTime, progress, params):
        ...
    def __repr__(self):
        ...
