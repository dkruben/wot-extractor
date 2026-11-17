# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/hit_direction_ctrl/components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import typing as typing
from account_helpers.settings_core.settings_constants import DAMAGE_INDICATOR as DAMAGE_INDICATOR, GRAPHICS as GRAPHICS
from gui.battle_control.controllers.hit_direction_ctrl.base import IHitIndicator as IHitIndicator
from gui.battle_control.controllers.hit_direction_ctrl.pulls import BaseHitPull as BaseHitPull
_VISUAL_DAMAGE_INDICATOR_SETTINGS: tuple

class BaseHitComponent(object):
    _pull: Any
    _ui: Any
    def __init__(self, pull):
        ...
    @property
    def ui(self):
        ...
    @property
    def pull(self):
        ...
    def setVisible(self, isVisible):
        ...
    def setUI(self, ui, isVisible):
        ...
    def clear(self):
        ...
    def invalidateSettings(self, diff):
        ...

class HitDamageComponent(BaseHitComponent):
    def invalidateSettings(self, diff):
        ...
