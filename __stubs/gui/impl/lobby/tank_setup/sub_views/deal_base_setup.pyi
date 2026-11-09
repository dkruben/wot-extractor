# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/sub_views/deal_base_setup.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from BWUtil import AsyncReturn as AsyncReturn
from gui.impl.lobby.tank_setup.configurations.base import BaseDealPanel as BaseDealPanel
from gui.impl.lobby.tank_setup.sub_views.base_setup import BaseSetupSubView as BaseSetupSubView
from gui.impl.lobby.tank_setup.tank_setup_sounds import playSound as playSound, TankSetupSoundEvents as TankSetupSoundEvents
from wg_async import wg_async as wg_async, await_callback as await_callback, wg_await as wg_await

class DealBaseSetupSubView(BaseSetupSubView):
    __slots__: tuple
    def update(self, fullUpdate=False):
        ...
    def updateSlots(self, slotID, fullUpdate=True, updateData=True):
        ...
    # decorador original: @wg_async
    def canQuit(self, skipApplyAutoRenewal=None):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _getDealPanel(self):
        ...
    def _updateDealPanel(self):
        ...
    # decorador original: @wg_async
    def _onDealConfirmed(self, _=None):
        ...
    def _onDealCancelled(self, _=None):
        ...
    def _onAutoRenewalChanged(self, args):
        ...
