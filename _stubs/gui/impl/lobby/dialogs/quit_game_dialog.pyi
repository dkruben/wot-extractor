# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/quit_game_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import GUI as GUI
from gui.Scaleform.managers.battle_input import BattleGUIKeyHandler as BattleGUIKeyHandler
from gui.app_loader.settings import APP_NAME_SPACE as APP_NAME_SPACE
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets as DialogPresets
from gui.impl.pub.dialog_window import DialogWindow as DialogWindow, DialogButtons as DialogButtons
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
_logger: Any
_RESIZE_TRIGER_WIDTH = 1450

class QuitGameDialogWindow(DialogWindow, BattleGUIKeyHandler):
    __appLoader: Any
    __slots__: tuple
    def __init__(self, parent=None):
        ...
    def handleEscKey(self, isDown):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    @property
    def _battleApp(self):
        ...
    def __onResize(self, event):
        ...
