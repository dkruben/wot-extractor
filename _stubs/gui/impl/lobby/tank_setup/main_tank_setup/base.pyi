# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/main_tank_setup/base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from BWUtil import AsyncReturn as AsyncReturn
from wg_async import wg_async as wg_async, wg_await as wg_await, await_callback as await_callback
from gui.impl.common.base_sub_model_view import BaseSubModelView as BaseSubModelView
from gui.impl.lobby.tank_setup.tank_setup_sounds import playSectionSelectSound as playSectionSelectSound
_logger: Any

class MainTankSetupView(BaseSubModelView):
    __slots__: tuple
    _builder: Any
    _subViews: Any
    __isLocked: Any
    def __init__(self, viewModel, builder=None):
        ...
    def setLocked(self, value):
        ...
    def currentVehicleUpdated(self, vehicle):
        ...
    def resetVehicle(self, interactingItem):
        ...
    def onLoading(self, selectedSection='', selectedSlot=None):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def getSelectedSetup(self):
        ...
    def getCurrentSubView(self):
        ...
    def getSubView(self, sectionName):
        ...
    def update(self, fullUpdate=False):
        ...
    # decorador original: @wg_async
    def canQuit(self, skipApplyAutoRenewal=None):
        ...
    # decorador original: @wg_async
    def switch(self, setupName, slotID):
        ...
    # decorador original: @wg_async
    def _doSwitch(self, setupName, slotID):
        ...
