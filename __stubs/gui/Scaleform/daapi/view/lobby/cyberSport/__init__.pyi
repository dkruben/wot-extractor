# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/cyberSport/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework import GroupedViewSettings as GroupedViewSettings, ComponentSettings as ComponentSettings
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler as PackageBusinessHandler
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES as CYBER_SPORT_ALIASES
from gui.app_loader.settings import APP_NAME_SPACE as APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ShowDialogEvent as ShowDialogEvent

class PLAYER_GUI_STATUS(object):
    NORMAL = 0
    READY = 2
    BATTLE = 3
    LOCKED = 4
    CREATOR = 5

class SLOT_LABEL(object):
    DEFAULT = ''
    LOCKED = 'freezed'
    CLOSED = 'locked'
    NOT_AVAILABLE = 'notAvailable'
    NOT_ALLOWED = 'notAllowed'
    EMPTY = 'emptySlot'
    REQUIRED = 'required'
    BATTLE_ROYALE = 'battleRoyale'

class _CyberSportBusinessHandler(PackageBusinessHandler):
    def __init__(self):
        ...

class _CyberSportDialogsHandler(PackageBusinessHandler):
    def __init__(self):
        ...
    def __showCyberSportDialog(self, event):
        ...

def getContextMenuHandlers():
    ...
def getViewSettings():
    ...
def getBusinessHandlers():
    ...
