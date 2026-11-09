# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/persistent_data_cache/configs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from dict2model import models as models, schemas as schemas, fields as fields
from section2dict import parse as parse
from constants import HAS_DEV_RESOURCES as HAS_DEV_RESOURCES
from ResMgr import DataSection as DataSection
PDC_SETTINGS_KEY = 'persistent_data_cache'
pdcSettingsSchema: Any

class PDCSettingsModel(models.Model):
    __slots__: tuple
    enabled: Any
    devEnabled: Any
    useThread: Any
    def __init__(self, enabled, devEnabled, useThread):
        ...
    def _reprArgs(self):
        ...

def createPDCSettings(scriptsConfig, engineConfig, userPreferences):
    ...
