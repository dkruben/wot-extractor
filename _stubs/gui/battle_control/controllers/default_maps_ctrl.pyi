# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/default_maps_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from gui.battle_control import minimap_utils as minimap_utils
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.view_components import IViewComponentsController as IViewComponentsController
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class DefaultMapsController(IViewComponentsController):
    _plugins: Any
    _miniMapUi: Any
    _eManager: Any
    def __init__(self, setup):
        ...
    def getMinimapPositionById(self, cellId):
        ...
    def getMinimapCellIdByPosition(self, position):
        ...
    def getMinimapCellNameById(self, cellId):
        ...
    def hasMinimapGrid(self):
        ...
    def setViewComponents(self, *components):
        ...
    def getControllerID(self):
        ...
    def clearViewComponents(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
