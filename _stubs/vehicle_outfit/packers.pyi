# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/vehicle_outfit/packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from itertools import product as product
from past.builtins import long as long
from debug_utils import LOG_WARNING as LOG_WARNING
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from items.components.c11n_constants import CustomizationType as CustomizationType
from items.customizations import PaintComponent as PaintComponent, CamouflageComponent as CamouflageComponent, DecalComponent as DecalComponent, ProjectionDecalComponent as ProjectionDecalComponent, InsigniaComponent as InsigniaComponent, PersonalNumberComponent as PersonalNumberComponent, SequenceComponent as SequenceComponent, AttachmentComponent as AttachmentComponent, StatTrackerComponent as StatTrackerComponent
from items.vehicles import makeIntCompactDescrByID as makeIntCompactDescrByID, getItemByCompactDescr as getItemByCompactDescr
from soft_exception import SoftException as SoftException
from constants import IS_EDITOR as IS_EDITOR

class CustomizationPacker(object):
    @staticmethod
    def pack(slot, component):
        ...
    @classmethod
    def unpack(cls, slot, component):
        ...
    @classmethod
    def invalidate(cls, slot):
        ...
    @staticmethod
    def create(component, cType):
        ...
    @staticmethod
    def getRawComponent():
        ...
    @classmethod
    def removePreview(cls, slot):
        ...

class PaintPacker(CustomizationPacker):
    @staticmethod
    def pack(slot, component):
        ...
    @classmethod
    def unpack(cls, slot, component):
        ...
    @classmethod
    def invalidate(cls, slot):
        ...
    @staticmethod
    def getRawComponent():
        ...

class CamouflagePacker(CustomizationPacker):
    @staticmethod
    def pack(slot, component):
        ...
    @classmethod
    def unpack(cls, slot, component):
        ...
    @classmethod
    def invalidate(cls, slot):
        ...
    @staticmethod
    def getRawComponent():
        ...

class DecalPacker(CustomizationPacker):
    _LOCK_SUBCOMP_ID = 0
    @staticmethod
    def pack(slot, component):
        ...
    @classmethod
    def unpack(cls, slot, component):
        ...
    @classmethod
    def invalidate(cls, slot):
        ...
    @staticmethod
    def getRawComponent():
        ...

class ModificationPacker(CustomizationPacker):
    @staticmethod
    def pack(slot, component):
        ...
    @classmethod
    def unpack(cls, slot, component):
        ...
    @classmethod
    def invalidate(cls, slot):
        ...
    @staticmethod
    def getRawComponent():
        ...

class ProjectionDecalPacker(CustomizationPacker):
    STYLED_SLOT_ID = 0
    @staticmethod
    def pack(slot, component):
        ...
    @classmethod
    def unpack(cls, slot, component):
        ...
    @classmethod
    def invalidate(cls, slot):
        ...
    @staticmethod
    def getRawComponent():
        ...
    @classmethod
    def removePreview(cls, slot):
        ...

class InsigniaPacker(CustomizationPacker):
    @staticmethod
    def pack(slot, component):
        ...
    @classmethod
    def unpack(cls, slot, component):
        ...
    @classmethod
    def invalidate(cls, slot):
        ...
    @staticmethod
    def getRawComponent():
        ...

class PersonalNumberPacker(CustomizationPacker):
    @staticmethod
    def pack(slot, component):
        ...
    @classmethod
    def unpack(cls, slot, component):
        ...
    @classmethod
    def invalidate(cls, slot):
        ...
    @staticmethod
    def getRawComponent():
        ...

class SequencePacker(CustomizationPacker):
    @staticmethod
    def pack(slot, component):
        ...
    @classmethod
    def unpack(cls, slot, component):
        ...
    @classmethod
    def invalidate(cls, slot):
        ...
    @staticmethod
    def getRawComponent():
        ...

class AttachmentPacker(CustomizationPacker):
    @staticmethod
    def pack(slot, component):
        ...
    @classmethod
    def unpack(cls, slot, component):
        ...
    @classmethod
    def invalidate(cls, slot):
        ...
    @staticmethod
    def getRawComponent():
        ...

class StatTrackerPacker(CustomizationPacker):
    @staticmethod
    def pack(slot, component):
        ...
    @classmethod
    def unpack(cls, slot, component):
        ...
    @classmethod
    def invalidate(cls, slot):
        ...
    @staticmethod
    def getRawComponent():
        ...

def pickPacker(itemTypeID):
    ...
def pickPackers(itemTypes):
    ...
def isComponentComplex(component):
    ...
