# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/customization/slots.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import Math as Math
from shared_utils import first as first
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from items.components.c11n_constants import ProjectionDecalFormTags as ProjectionDecalFormTags, SLOT_DEFAULT_ALLOWED_MODEL as SLOT_DEFAULT_ALLOWED_MODEL, ProjectionDecalMatchingTags as ProjectionDecalMatchingTags
from gui.shared.gui_items.customization import directionByTag as directionByTag
_logger: Any
SLOT_ASPECT_RATIO: dict
FORMFACTOR_ASPECT_RATIO: dict

class BaseSlot(object):
    __slots__: tuple
    _areaId: Any
    _regionIdx: Any
    _descriptor: Any
    def __init__(self, descriptor, areaId, regionIdx):
        ...
    @property
    def type(self):
        ...
    @property
    def areaId(self):
        ...
    @property
    def regionIdx(self):
        ...
    @property
    def descriptor(self):
        ...
    @property
    def hiddenForUser(self):
        ...
    @property
    def compatibleModels(self):
        ...

class EmblemSlot(BaseSlot):
    @property
    def rayStart(self):
        ...
    @property
    def rayEnd(self):
        ...
    @property
    def rayUp(self):
        ...
    @property
    def size(self):
        ...
    @property
    def hideIfDamaged(self):
        ...
    @property
    def isMirrored(self):
        ...
    @property
    def isUVProportional(self):
        ...
    @property
    def emblemId(self):
        ...
    @property
    def slotId(self):
        ...
    @property
    def applyToFabric(self):
        ...

class BaseCustomizationSlot(BaseSlot):
    @property
    def slotId(self):
        ...
    @property
    def anchorPosition(self):
        ...
    @property
    def anchorDirection(self):
        ...
    @property
    def areaId(self):
        ...
    @property
    def regionIdx(self):
        ...
    @property
    def descriptor(self):
        ...

class ProjectionDecalSlot(BaseCustomizationSlot):
    @property
    def applyTo(self):
        ...
    @property
    def tags(self):
        ...
    @property
    def hiddenForUser(self):
        ...
    @property
    def position(self):
        ...
    @property
    def rotation(self):
        ...
    @property
    def scale(self):
        ...
    @property
    def scaleFactors(self):
        ...
    @property
    def doubleSided(self):
        ...
    @property
    def showOn(self):
        ...
    @property
    def direction(self):
        ...
    @property
    def canBeMirroredVertically(self):
        ...
    @property
    def formfactors(self):
        ...
    @property
    def matchingTag(self):
        ...
    def isFitForFormfactor(self, formfactor):
        ...
    @property
    def compatibleModels(self):
        ...

class AttachmentSlot(BaseCustomizationSlot):
    @property
    def position(self):
        ...
    @property
    def rotation(self):
        ...
    @property
    def hiddenForUser(self):
        ...
    @property
    def enableVisTunnel(self):
        ...
    @property
    def tags(self):
        ...
    @property
    def applyType(self):
        ...
    @property
    def size(self):
        ...
    @property
    def hangerId(self):
        ...
    @property
    def scaleFactorId(self):
        ...
    @property
    def hangerRotation(self):
        ...
    @property
    def compatibleModels(self):
        ...

def getProgectionDecalAspect(slotDescriptor):
    ...
