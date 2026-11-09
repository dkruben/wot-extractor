# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/main_menu_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.hangar.menu_item_model import MenuItemModel as MenuItemModel

class MainMenuModel(ViewModel):
    __slots__: tuple
    MODE_SELECTOR = 'modeSelector'
    SHOP = 'shop'
    STORAGE = 'storage'
    MISSIONS = 'missions'
    PERSONAL_MISSIONS = 'personalMissions'
    ACHIEVEMENTS = 'achievements'
    TECHTREE = 'techtree'
    TOURNAMENT = 'tournament'
    BARRACKS = 'barracks'
    CLANS = 'clans'
    REPLAYS = 'replays'
    onNavigate: Any
    def __init__(self, properties=5, commands=1):
        ...
    def getMenuItems(self):
        ...
    def setMenuItems(self, value):
        ...
    @staticmethod
    def getMenuItemsType():
        ...
    def getModeName(self):
        ...
    def setModeName(self, value):
        ...
    def getModeId(self):
        ...
    def setModeId(self, value):
        ...
    def getHasTechTreeEvents(self):
        ...
    def setHasTechTreeEvents(self, value):
        ...
    def getClanEmblem(self):
        ...
    def setClanEmblem(self, value):
        ...
    def _initialize(self):
        ...
