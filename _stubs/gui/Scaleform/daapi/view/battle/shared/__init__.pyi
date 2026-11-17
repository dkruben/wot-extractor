# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.battle.shared.page import SharedPage as SharedPage
from gui.Scaleform.framework import ViewSettings as ViewSettings, ScopeTemplates as ScopeTemplates, ComponentSettings as ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import LoadViewEvent as LoadViewEvent
__all__: tuple

class BattlePackageBusinessHandler(PackageBusinessHandler):
    __slots__: tuple
    def __init__(self):
        ...
    def __handleIngameMenuEvent(self, event):
        ...
    def __handleHelpEvent(self, _):
        ...
    def __handleDetailsHelpEvent(self, event):
        ...
    def __isFullStatsShown(self, ctx):
        ...

def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getBusinessHandlers():
    ...
