# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/impl/lobby/intro_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers as comp7_core_model_helpers
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport.backport_tooltip import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import event_dispatcher as event_dispatcher
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
_logger: Any

class IntroScreen(ViewImpl, IGlobalListener):
    __slots__: tuple
    __settingsCore: Any
    def __init__(self, layoutID):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def _modeController(self):
        ...
    @property
    def _modelClazz(self):
        ...
    @property
    def _seasonStateClazz(self):
        ...
    @property
    def _yearStateClazz(self):
        ...
    @property
    def _seasonNameClazz(self):
        ...
    @property
    def _calendarDayTooltipID(self):
        ...
    def createToolTip(self, event):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *_, **__):
        ...
    def _updateData(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onStatusUpdated(self, status):
        ...
    def __onClose(self):
        ...
    def __onPollServerTime(self):
        ...
