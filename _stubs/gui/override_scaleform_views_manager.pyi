# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/override_scaleform_views_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import importlib as importlib
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from soft_exception import SoftException as SoftException
g_overrideScaleFormViewsConfig: Any

class _OverrideScaleFormViewsManager(object):
    __slots__: tuple
    _activeViewAliases: Any
    _activeContextMenuAliases: Any
    _lobbyPackages: Any
    _battlePackages: Any
    def __init__(self):
        ...
    @property
    def activeExtensionsViewAliases(self):
        ...
    @property
    def activeExtensionsCMAliases(self):
        ...
    @property
    def lobbyPackages(self):
        ...
    @property
    def battlePackages(self):
        ...
    def initExtensionLobbyPackages(self, extensionName, lobbyPackages):
        ...
    def initExtensionBattlePackages(self, extensionName, battlePackages, arenaGUIType):
        ...
    def __initHandlers(self, paths, extensionName, guiType=None):
        ...
