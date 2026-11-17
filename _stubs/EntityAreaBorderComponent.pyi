# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/EntityAreaBorderComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from Math import Vector3 as Vector3
from cache import cached_property as cached_property
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from account_helpers.settings_core import ISettingsCore as ISettingsCore, settings_constants as settings_constants
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent

class EntityAreaBorderComponent(DynamicScriptComponent):
    DRAW_TYPE_NORMAL = 0
    COLOR_BLINDNESS_MATERIAL_PARAM_NAME = 'g_isColorBlind'
    STRIPES_ENABLED_MATERIAL_PARAM_NAME = 'g_stripesEnabled'
    sessionProvider: Any
    settingsCore: Any
    _border: Any
    def __init__(self):
        ...
    def onDestroy(self):
        ...
    def set_isVisible(self, oldValue):
        ...
    @property
    def isBorderVisible(self):
        ...
    def updateBorderVisibility(self):
        ...
    def updateColorBlindness(self):
        ...
    def getClosestPoint(self, pos, searchRadius):
        ...
    def updateDrawStyle(self):
        ...
    def getDimensions(self):
        ...
    # decorador original: @cached_property
    def polygonCenter(self):
        ...
    def _onAvatarReady(self):
        ...
    def _onSettingsChanged(self, diff):
        ...
    def _onArenaBorderTypeChanged(self, event):
        ...
