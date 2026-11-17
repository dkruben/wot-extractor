# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/version.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import ResMgr as ResMgr
import section2dict as section2dict
from dict2model import models as models, schemas as schemas, fields as fields
from helpers import VERSION_FILE_PATH as VERSION_FILE_PATH, LOC_VERSION_FILE_PATH as LOC_VERSION_FILE_PATH
_clientVersion = None
_locVersion = None
_clientVersionMetaSchema: Any
_clientVersionSchema: Any
_localizationVersionSchema: Any

class ClientVersionMetaModel(models.Model):
    __slots__: tuple
    client: Any
    overrides: Any
    realm: Any
    branch: Any
    buildScriptsRevision: Any
    def __init__(self, client='', overrides='', realm='', branch='', buildScriptsRevision=''):
        ...
    def _reprArgs(self):
        ...

class ClientVersionModel(models.Model):
    __slots__: tuple
    appname: Any
    version: Any
    showLicense: Any
    ingameHelpVersion: Any
    meta: Any
    def __init__(self, appname='', version='', showLicense='', ingameHelpVersion='', meta=None):
        ...
    def _reprArgs(self):
        ...

class LocalizationVersionModel(models.Model):
    __slots__: tuple
    version: Any
    revision: Any
    language: Any
    def __init__(self, version='', revision='', language=''):
        ...
    def _reprArgs(self):
        ...

def getClientVersion(force=False):
    ...
def getLocalizationVersion(force=False):
    ...
