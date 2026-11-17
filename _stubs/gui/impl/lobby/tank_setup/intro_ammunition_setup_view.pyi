# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/intro_ammunition_setup_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS as UI_STORAGE_KEYS
import wg_async as wg_async
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.tank_setup.tank_setup_sounds import playEnterTankSetupView as playEnterTankSetupView, playExitTankSetupView as playExitTankSetupView
from gui.impl.lobby.common.info_view import InfoView as InfoView, getInfoWindowProc as getInfoWindowProc, createContentData as createContentData
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from gui.impl.lobby.common.info_view import IInfoWindowProcessor as IInfoWindowProcessor
_logger: Any

class _IntroAmmunitionSetupView(InfoView):
    _guiLoader: Any
    __slots__: tuple
    __hasTankSetupView: Any
    def __init__(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...

# decorador original: @wg_async.wg_async
def showIntro(introKey, *args, **kwargs):
    ...
def getIntroAmmunitionSetupWindowProc():
    ...
