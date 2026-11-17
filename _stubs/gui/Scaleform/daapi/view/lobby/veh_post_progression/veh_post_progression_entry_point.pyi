# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/veh_post_progression/veh_post_progression_entry_point.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import BECOME_ELITE_VEHICLES_WATCHED as BECOME_ELITE_VEHICLES_WATCHED
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.genConsts.POSTPROGRESSION_CONSTS import POSTPROGRESSION_CONSTS as POSTPROGRESSION_CONSTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import events as events
from gui.veh_post_progression.helpers import needToShowCounter as needToShowCounter
from soft_exception import SoftException as SoftException
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.gui_items.Vehicle import EliteStatusProgress as EliteStatusProgress

class VehPostProgressionEntryPoint(EventSystemEntity):
    __slots__: tuple
    _eliteWatchedList: Any
    _parentObj: Any
    _vehicle: Any
    _watchedListDirty: Any
    _modulesToUnlock: Any
    def __init__(self, parentObj):
        ...
    def dispose(self):
        ...
    def redraw(self, vehicle):
        ...
    def invalidateUnlocks(self, unlocks):
        ...
    @property
    def isUnlockShowed(self):
        ...
    def tryUnlock(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def __onEliteWindowClosed(self, _):
        ...
    def __onBuyVehicleWindowClosed(self, event):
        ...
    def __updatePostProgressionData(self):
        ...
    def __getPostProgressionData(self):
        ...
    def __getLabel(self, eliteProgress):
        ...
    def __getUnlockState(self):
        ...

def _validateVehicle(vehicle):
    ...
