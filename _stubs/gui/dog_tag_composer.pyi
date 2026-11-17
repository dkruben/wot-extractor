# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/dog_tag_composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
import logging as logging
import typing as typing
from dog_tags_common.components_config import componentConfigAdapter as componentConfig
from dog_tags_common.config.common import ComponentViewType as ComponentViewType, ComponentPurpose as ComponentPurpose
from gui.impl import backport as backport
from gui.impl.gen import R as R
from typing import Optional as Optional
from frameworks.wulf import PyResAccessor as PyResAccessor
from dog_tags_common.config.dog_tag_framework import ComponentDefinition as ComponentDefinition
_logger: Any
ViewTypeToImageFolderMap: dict
LANGUAGE_CODE: Any
SUPPORTED_LANGUAGES: list
dogTagComposer: Any

class AssetSize(Enum):
    BIG = 'big'
    SMALL = 'small'
    MINI = 'mini'

class DogTagComposerClient(object):
    MAX_NAME_LENGTH = 12
    @staticmethod
    def getComponentImage(componentId, grade=0, localized=False):
        ...
    @staticmethod
    def getBottomPlateImage(backgroundId):
        ...
    @classmethod
    def getComponentImageFullPath(cls, size, componentId, grade=0):
        ...
    @staticmethod
    def getDefaultBackgroundImageFullPath(size):
        ...
    @classmethod
    def getComponentTitle(cls, componentId):
        ...
    @staticmethod
    def getComponentTitleRes(componentId):
        ...
    @staticmethod
    def getComponentDescription(componentId):
        ...
    @staticmethod
    def getComponentType(componentId):
        ...
    @staticmethod
    def getPurposeRes(purpose):
        ...
    @staticmethod
    def getPurposeGroupRes(purposeGroup):
        ...
    @staticmethod
    def getPurposeTooltipRes(purposeGroup):
        ...
    @staticmethod
    def getAnimationSrc(animation):
        ...

def getResourceRoot(component):
    ...
def getLocalizePostfix():
    ...
