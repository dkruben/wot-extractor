# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import os as os
from gui.Scaleform.locale.MENU import MENU as MENU
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
from skeletons.gui.techtree_events import ITechTreeEventsListener as ITechTreeEventsListener
import _Scaleform as _Scaleform
SCALEFORM_SUPPORT = True
SCALEFORM_SWF_PATH_V3 = 'gui/flash'
VEHICLE_TYPES_ICONS_DIR_PATH = '../maps/icons/filters/tanks/'
CUSTOMIZATION_TYPES_ICONS_DIR_PATH = '../maps/icons/filters/customization/'
NATION_FILTER_ICONS_DIR_PATH = '../maps/icons/filters/nations/'
BUTTON_FILTER_ICONS_DIR_PARH = '../maps/icons/library/'
LEVEL_FILTER_ICONS_DIR_PARH = '../maps/icons/filters/levels/'
DEFAULT_VIDEO_BUFFERING_TIME = 2.0

def getVehicleTypeAssetPath(vehicleType, extension='.png'):
    ...
def getCustomizationTypeAssetPath(type, extension='.png'):
    ...
def getButtonsAssetPath(button, extension='.png'):
    ...
def getNationsFilterAssetPath(nationName, extension='.png'):
    ...
def getLevelsAssetPath(level_str, extension='.png'):
    ...
def getNecessaryArenaFrameName(arenaSubType, hasBase=None):
    ...
def getPathForFlash(path, base=...):
    ...
def getScaleformConfig(manager):
    ...
