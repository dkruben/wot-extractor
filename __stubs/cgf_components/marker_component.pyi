# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/marker_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import importlib as importlib
import logging as logging
import typing as typing
import CGF as CGF
import EntitySync as EntitySync
import Event as Event
import Math as Math
import math_utils as math_utils
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from constants import IS_CLIENT as IS_CLIENT, IS_CGF_DUMP as IS_CGF_DUMP
from helpers import dependency as dependency
from UIComponents import GamefaceMarkerComponent as GamefaceMarkerComponent
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.app_loader.settings import APP_NAME_SPACE as APP_NAME_SPACE
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers import AreaMarker as AreaMarker
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import ComponentBitMask as ComponentBitMask
from gui.impl.pub import WindowImpl as WindowImpl
from frameworks.wulf import WindowFlags as WindowFlags, WindowLayer as WindowLayer
import BigWorld as BigWorld
_logger: Any

class IBattleSessionProvider(object):
    ...

class IAppLoader(object):
    ...

class IGuiLoader(object):
    ...

# decorador original: @registerComponent
class LobbyFlashMarker(object):
    domain = CGF.Domain.Client
    editorTitle = 'Lobby Flash Marker'
    icon: Any
    textKey: Any

# decorador original: @registerComponent
class LobbyFlashMarkerVisibility(object):
    domain = CGF.Domain.Client
    editorTitle = 'Lobby Flash Marker Visibility'
    mainTankMarkerGO: Any
    heroTankMarkerGO: Any

# decorador original: @registerComponent
class CombatMarker(object):
    group = 'UI'
    editorTitle = 'Combat Marker'
    domain = CGF.Domain.Client
    shape: Any
    offset: Any
    areaRadius: Any
    disappearanceRadius: Any
    reverseDisappearing: Any
    distanceFieldColor: Any
    marker: Any
    markerID: Any
    def __init__(self):
        ...

class LobbyMarkersSystem(CGF.System):
    __appLoader: Any
    MarkerActivated: Any
    MarkerDeactivated: Any
    EntitySyncAccess: Any
    Reactions: Any
    onMarkerComponentAdded: Any
    onMarkerComponentRemoved: Any
    def __init__(self, *args):
        ...
    def update(self):
        ...
    def handleMarkerAdded(self, gameObject, flashMarkerComponent, transformComponent, entitySyncAccess):
        ...
    def handleMarkerRemoved(self, gameObject, entitySyncAccess):
        ...
    def __getRootEntity(self, gameObject, entitySyncAccess):
        ...
    def __getMarkerView(self):
        ...

class LobbyMarkersVisibilitySystem(CGF.System):
    VisibilityActivated: Any
    VisibilityDeactivated: Any
    VisibilityAccess: Any
    Reactions: Any
    def update(self):
        ...
    def handleVisibilityAdded(self, gameObject, lobbyFlashMarkerVisibility):
        ...
    def handleVisibilityRemoved(self, gameObject):
        ...
    def __onHeroTankAction(self, gameObject, visibilityComponent=None):
        ...
    @staticmethod
    def __activateMarkerFromNonHeroTank(component, gameObjectManager):
        ...
    @staticmethod
    def __activateMarkerFromHeroTank(component, gameObjectManager):
        ...

class CombatMarkerSystem(CGF.System):
    __guiSessionProvider: Any
    MarkerActivated: Any
    MarkerDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def onAddedMarker(self, combatMarker, transform):
        ...
    def onRemovedMarker(self, combatMarker):
        ...

class GFMarkersCreatorSystem(CGF.System):
    __gui: Any
    MarkerActivated: Any
    MarkerDeactivated: Any
    Reactions: Any
    def update(self):
        ...
    def onMarkerAdded(self, markerComponent):
        ...
    def onMarkerRemoved(self, markerComponent):
        ...
