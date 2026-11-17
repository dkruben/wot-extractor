# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/extension_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import importlib as importlib
from soft_exception import SoftException as SoftException
from ExtensionsManager import g_extensionsManager as g_extensionsManager
from constants import IS_CLIENT as IS_CLIENT, IS_EDITOR as IS_EDITOR, IS_BOT as IS_BOT
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from extension_rules import isExtXML as isExtXML, READ_METHOD as READ_METHOD
from py2to3.patched_future import with_metaclass as with_metaclass
import ResMgr as rmgr
from realm_utils import ResMgr as rmgr
_ROOT_TAG = 'root'
_XML_NAMESPACE = ' xmlns:xmlref="http://bwt/xmlref"'
_MERGE_TAG = 'xmlref:merge'
_CONTENT_TAG = 'xmlref:content'
_INCLUDE_TAG = 'xmlref:include'
_INCLUDE_BY_PATH_TAG = 'xmlref:includeByPath'

class _MergeExtensionFile(object):
    @classmethod
    def makeMergeXMLString(cls, xmlPaths, mergeType, params):
        ...
    @classmethod
    def openSection(cls, xmlPath, mergeType, params):
        ...
    @classmethod
    def _openTag(cls, tag, attributes=None):
        ...
    @classmethod
    def _closeTag(cls, tag):
        ...
    @classmethod
    def _attributeTag(cls, tag, attrName, attrValue):
        ...

class _ResMrgMeta(type):
    def __getattr__(cls, item):
        ...

# base nao representavel no stub: with_metaclass(...)
class ResMgr:
    @classmethod
    def openSection(cls, filepath, createIfMissing=False):
        ...
    @staticmethod
    def addToCache(ftPath, xml):
        ...
    @staticmethod
    def isInCache(filePath):
        ...
    @staticmethod
    def findFirstPathOccurrence(filePath, extensionsOnly=False):
        ...
    @staticmethod
    def purge(resourceID, recurse=False):
        ...

def getRealmFilePath(filepath):
    ...
def importClass(classPath, defaultMod):
    ...
def mergeSection(xmlPath, mergeType, params):
    ...
def makeMergeXMLString(xmlPaths, mergeType, params):
    ...
