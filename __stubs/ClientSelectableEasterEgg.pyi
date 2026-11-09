# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ClientSelectableEasterEgg.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import AnimationSequence as AnimationSequence
from ClientSelectableObject import ClientSelectableObject as ClientSelectableObject
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.shared import g_eventBus as g_eventBus, events as events
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import getClientLanguage as getClientLanguage
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak

class ClientSelectableEasterEgg(ClientSelectableObject):
    __animator: Any
    def __init__(self):
        ...
    def prerequisites(self):
        ...
    def _getCollisionModelsPrereqs(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def onMouseClick(self):
        ...
    def __getImageName(self):
        ...
    def __createAnimationSequence(self, resourceName):
        ...
    def __onAnimatorLoaded(self, resourceName, resourceList):
        ...
    def _addEdgeDetect(self):
        ...
    def _delEdgeDetect(self):
        ...
