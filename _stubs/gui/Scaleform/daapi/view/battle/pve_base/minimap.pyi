# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/minimap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CommandMapping as CommandMapping
import GUI as GUI
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from constants import PVE_MINIMAP_DEFAULT_ZOOM as PVE_MINIMAP_DEFAULT_ZOOM, PVE_MINIMAP_DEFAULT_BORDERS as PVE_MINIMAP_DEFAULT_BORDERS
from gui.Scaleform.daapi.view.battle.classic.minimap import GlobalSettingsPlugin as GlobalSettingsPlugin
from gui.Scaleform.daapi.view.battle.shared.minimap import settings as settings
from gui.Scaleform.daapi.view.battle.shared.minimap.plugins import PersonalEntriesPlugin as PersonalEntriesPlugin
from gui.Scaleform.daapi.view.meta.PveMinimapMeta import PveMinimapMeta as PveMinimapMeta
from gui.battle_control import avatar_getter as avatar_getter
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ScalableBattleMinimapEvent as ScalableBattleMinimapEvent
from gui.shared.utils.key_mapping import getReadableKey as getReadableKey
from helpers import dependency as dependency
from pve_battle_hud import WidgetType as WidgetType, getPveHudLogger as getPveHudLogger
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from Math import Vector2 as Vector2
_S_NAME = settings.ENTRY_SYMBOL_NAME
_logger: Any

class PveMinimapGlobalSettingsPlugin(GlobalSettingsPlugin):
    _sessionProvider: Any
    def _toogleVisible(self):
        ...

class PveScaleCenteredPersonalEntriesPlugin(PersonalEntriesPlugin):
    __slots__: tuple
    _isInBordersMode: Any
    def __init__(self, parentObj):
        ...
    def initControlMode(self, mode, available):
        ...
    def updateControlMode(self, mode, vehicleID):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _onMinimapBordersUpdated(self, event):
        ...
    def _onZoomLevelUpdated(self, event):
        ...
    def _getPostmortemCenterEntry(self):
        ...
    def _centerMapBasedOnMode(self):
        ...

class PveMinimapComponent(PveMinimapMeta):
    _sessionProvider: Any
    _canToggleFullMap: Any
    def __init__(self):
        ...
    def setVisibleRect(self, bl, tr):
        ...
    def setZoom(self, zoom):
        ...
    def setMinimapCenterEntry(self, entityID):
        ...
    def _createFlashComponent(self):
        ...
    def _setupPlugins(self, arenaVisitor):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _mappingChangeHandler(self, *_):
        ...
    def _setMinimapShortcutLabel(self):
        ...
    def _settingsChangeHandler(self, settingsID):
        ...
