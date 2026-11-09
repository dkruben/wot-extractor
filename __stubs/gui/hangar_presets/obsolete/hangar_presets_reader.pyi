# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/obsolete/hangar_presets_reader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import ResMgr as ResMgr
from gui.hangar_presets.obsolete.hangar_gui_config import HangarGuiPreset as HangarGuiPreset, HangarGuiSettings as HangarGuiSettings, PresetSettings as PresetSettings
from soft_exception import SoftException as SoftException
_ERR_TEMPLATE = "[HangarGUI] {} in the preset '{}'"

class IPresetReader(object):
    @classmethod
    def readConfig(cls, fullConfig):
        ...
    @staticmethod
    def isDefault():
        ...

class DefaultPresetReader(IPresetReader):
    _CONFIG_PATH = 'gui/hangar_gui_presets.xml'
    @classmethod
    def readConfig(cls, fullConfig):
        ...
    @staticmethod
    def isDefault():
        ...
    @classmethod
    def _getPreset(cls, presetName, config):
        ...
    @classmethod
    def _updateItems(cls, items, queueType, preset):
        ...
    @classmethod
    def __readComponents(cls, config, presetName):
        ...
    @classmethod
    def __readGuiHangarConfig(cls, configPath, fullConfig):
        ...
    @classmethod
    def __readPresets(cls, config, fullConfig):
        ...
    @classmethod
    def __readPresetsForQueueTypes(cls, config):
        ...
    @staticmethod
    def __updateComponents(baseComponents, override):
        ...

class DefaultSubPresetReader(DefaultPresetReader):
    _SUB_TYPES_KEY = 'subTypes'
    @staticmethod
    def isDefault():
        ...
    @classmethod
    def _getPreset(cls, presetName, config):
        ...
    @classmethod
    def _updateItems(cls, items, queueType, preset):
        ...

class SpecBattlePresetReader(DefaultSubPresetReader):
    _CONFIG_PATH = 'gui/hangar_gui_spec_presets.xml'
    _SUB_TYPES_KEY = 'guiTypes'
