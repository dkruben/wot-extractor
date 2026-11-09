# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.view.battle import shared as shared
from gui.Scaleform.framework import ComponentSettings as ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from story_mode.gui.scaleform.daapi.view.battle.consumables_panel import SMConsumablesPanel as SMConsumablesPanel
from story_mode.gui.story_mode_gui_constants import VIEW_ALIAS as VIEW_ALIAS

class ConditionalStoryModeViewSettings(ComponentSettings):
    @staticmethod
    def __new__(cls, alias, onBoardingClazz, storyModeClazz, scope):
        ...

class _StoryModeBattlePackageBusinessHandler(PackageBusinessHandler):
    __slots__: tuple
    def __init__(self):
        ...
    def _loadPage(self, event):
        ...

def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getBusinessHandlers():
    ...
