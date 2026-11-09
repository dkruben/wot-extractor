# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import listitems as listitems, listvalues as listvalues
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.view.battle.shared.page import BattlePageBusinessHandler as BattlePageBusinessHandler
from gui.Scaleform.framework import GroupedViewSettings as GroupedViewSettings, ViewSettings as ViewSettings, ScopeTemplates as ScopeTemplates, ComponentSettings as ComponentSettings
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler as AbstractContextMenuHandler
from gui.Scaleform.daapi.view.battle.pve_base.page import PveBaseBattlePage as PveBaseBattlePage
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler

class OverridableViewSettingsMapping(object):
    __slots__: tuple
    _settingsMap: Any
    def __init__(self, settings):
        ...
    def getSettings(self):
        ...
    def extend(self, settings=None):
        ...

class OverridableContextMenuHandlers(object):
    __slots__: tuple
    _handlers: Any
    def __init__(self, handlers=None):
        ...
    def extend(self, handlers=None):
        ...
    def getHandlers(self):
        ...

def getDefaultViewSettings(battlePageAlias, battlePageClass, swfUrl='pveBaseBattlePage.swf'):
    ...
def getDefaultContextMenuHandler():
    ...
def getDefaultBusinessHandlers(battlePageAlias):
    ...
