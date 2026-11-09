# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/minimap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent as ClassicMinimapComponent, GlobalSettingsPlugin as GlobalSettingsPlugin
from gui.Scaleform.daapi.view.battle.shared.points_of_interest import minimap as poi_plugins
from account_helpers.settings_core.settings_constants import GAME as GAME
from gui.Scaleform.daapi.view.battle.shared.minimap import settings as settings

class Comp7MinimapComponent(ClassicMinimapComponent):
    def _setupPlugins(self, arenaVisitor):
        ...

class Comp7GlobalSettingsPlugin(GlobalSettingsPlugin):
    __slots__: tuple
    _sizeIndex: Any
    _currentSizeSettings: Any
    def start(self):
        ...
    def stop(self):
        ...
    def __onBattleStarted(self):
        ...
