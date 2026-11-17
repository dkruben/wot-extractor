# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/prb_control/entities/vehicle_switcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.impl.gen import R as R
from halloween.gui.halloween_account_settings import getSettings as getSettings, AccountSettingsKeys as AccountSettingsKeys, setSettings as setSettings
from halloween.gui.shared.event_dispatcher import isViewLoaded as isViewLoaded
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class VehicleSwitcher(object):
    _halloweenCtrl: Any
    _itemsCache: Any
    def startSwitcher(self):
        ...
    def stopSwitcher(self):
        ...
    def selectModeVehicle(self, vehInvID=0):
        ...
    def selectVehicleWithWaiting(self, vehInvID=0):
        ...
    def _getFavoriteVehInvID(self):
        ...
    def __onCurrentVehicleChanged(self):
        ...
