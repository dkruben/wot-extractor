# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_post_progression/helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from itertools import chain as chain
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import VPP_ENTRY_POINT_LAST_SEEN_STEP as VPP_ENTRY_POINT_LAST_SEEN_STEP
from account_shared import LayoutIterator as LayoutIterator
from gui.veh_post_progression.models.ext_money import ExtendedMoney as ExtendedMoney
from post_progression_common import VehicleState as VehicleState, parseActionCompDescr as parseActionCompDescr, ACTION_TYPES as ACTION_TYPES, TankSetupLayouts as TankSetupLayouts, GROUP_ID_BY_LAYOUT as GROUP_ID_BY_LAYOUT
_LAYOUT_TO_INSTALLED: tuple

def getVehicleState(actionCDs):
    ...
def setFeatures(state, actionCDs):
    ...
def setDisabledSwitches(state, groupIDs):
    ...
def getInstalledShells(shellsCDs, shellsLayout):
    ...
def updateInvInstalled(invData, setupsIndexes):
    ...
def storeLastSeenStep(vehicleIntCD, stepID):
    ...
def needToShowCounter(vehicle):
    ...
