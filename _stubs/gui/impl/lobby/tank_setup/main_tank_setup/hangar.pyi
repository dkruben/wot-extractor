# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/main_tank_setup/hangar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from BWUtil import AsyncReturn as AsyncReturn
from wg_async import wg_async as wg_async
from gui.impl.lobby.tank_setup.intro_ammunition_setup_view import showIntro as showIntro
from gui.impl.lobby.tank_setup.main_tank_setup.base import MainTankSetupView as MainTankSetupView

class HangarMainTankSetupView(MainTankSetupView):
    __slots__: tuple
    @property
    def currentInteractor(self):
        ...
    # decorador original: @wg_async
    def _doSwitch(self, setupName, slotID):
        ...
