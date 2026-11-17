# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dog_tags_common/config/dog_tag_parser.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from future.utils import viewitems as viewitems
import ResMgr as ResMgr
import dog_tags_common.config.dog_tag_framework as dtf
from constants import IS_CLIENT as IS_CLIENT, IS_BASEAPP as IS_BASEAPP
from dog_tags_common.config.common import ParseException as ParseException, ParameterType as ParameterType, Visibility as Visibility, ComponentPurpose as ComponentPurpose, ComponentViewType as ComponentViewType, DOG_TAGS_FILE as DOG_TAGS_FILE, ComponentNumberType as ComponentNumberType
from soft_exception import SoftException as SoftException
from typing import List as List, Tuple as Tuple
from dog_tags_common.config.dog_tag_framework import StartingComponents as StartingComponents, ComponentDefinition as ComponentDefinition
PARAM_PARSERS: dict

def _parseInt(attrValue, path):
    ...
def _parseBool(attrValue, path):
    ...
def _parseStr(attrValue, path):
    ...
def _parseIntList(attrValue, path):
    ...
def _parseFloatList(attrValue, path):
    ...
def _parseStrList(attrValue, path):
    ...
def _parseViewType(attrValue, path):
    ...
def _parseType(attrValue, path):
    ...
def _parseNumberType(attrValue, path):
    ...
def _parseSection(sectionName, section, *builderAttrs):
    ...
def readDogTags(xmlPath=...):
    ...
