# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_cameras/hangar_camera_settings_listener.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from shared_utils import BoundMethodWeakref as BoundMethodWeakref
from .hangar_space_listener import HangarSpaceListener as HangarSpaceListener

class HangarCameraSettingsListener(HangarSpaceListener):
    settingsCore: Any
    __settingHandlers: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def registerSettingHandler(self, setting, handler):
        ...
    def unregisterSettingsHandler(self, setting):
        ...
    def _activate(self):
        ...
    def _deactivate(self, inited):
        ...
    def __onSettingsChanged(self, diff):
        ...
