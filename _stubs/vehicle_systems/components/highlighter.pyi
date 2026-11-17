# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/highlighter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import CGF as CGF
from EdgeDrawer import EdgeHighlightComponent as EdgeHighlightComponent
from cgf_script.registration import registerComponent as registerComponent
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
EdgeHighlightComponentArgs: Any

# decorador original: @registerComponent
class Highlighter(object):
    domain = CGF.Domain.ClientEditor
    userVisible = False
    vseVisible = False
    HIGHLIGHT_OFF = 0
    HIGHLIGHT_SIMPLE = 1
    HIGHLIGHT_ON = 2
    HIGHLIGHT_DISABLED = 4
    HIGHLIGHT_SUSPENDED = 8
    status: Any
    sessionProvider: Any
    __vehicleRef: Any
    __highlightStatus: Any
    __isPlayersVehicle: Any
    __suspendedHighlightArgs: Any
    __forceSimpleEdge: Any
    @property
    def isOn(self):
        ...
    @property
    def isDisabled(self):
        ...
    @property
    def isSimpleEdge(self):
        ...
    def __init__(self, enabled):
        ...
    def setVehicle(self, vehicle):
        ...
    def setVehicleOwnership(self):
        ...
    def activate(self, collisions):
        ...
    def deactivate(self):
        ...
    def suspendHighlight(self):
        ...
    def resumeHighlight(self):
        ...
    def destroy(self):
        ...
    def removeHighlight(self):
        ...
    def highlight(self, enable, forceSimpleEdge=False, afterSuspend=False):
        ...
    def __getVehicle(self):
        ...
    def __doHighlightOperation(self, vehicle, status, args):
        ...
    def __updateHighlightComponent(self, vehicle, status, args):
        ...
    def __removeHighlightComponent(self, vehicle):
        ...

class HighlighterSystem(CGF.System):
    Activate: Any
    Reactions: Any
    def update(self):
        ...
