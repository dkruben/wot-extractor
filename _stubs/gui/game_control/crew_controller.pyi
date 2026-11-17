# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/crew_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.gui_items.Tankman import NO_SLOT as NO_SLOT, NO_TANKMAN as NO_TANKMAN
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
import Event as Event
from skeletons.gui.game_control import ICrewController as ICrewController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.impl import IGuiLoader as IGuiLoader

class CrewController(ICrewController, IGlobalListener):
    __lobbyContext: Any
    __uiLoader: Any
    __widgetSlotIdx: Any
    __widgetTankmanID: Any
    __isActiveJunkTankmen: Any
    onJunkStatusChanged: Any
    def __init__(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def setWidgetData(self, viewKey):
        ...
    def getWidgetData(self):
        ...
    def onDisconnected(self):
        ...
    @property
    def isActiveJunkTankmen(self):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    def __subscribe(self):
        ...
    def __unSubscribe(self):
        ...
    def __dispose(self):
        ...
