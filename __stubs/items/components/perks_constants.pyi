# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/perks_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from functools import reduce as reduce
PERKS_XML_FILE = 'perks.xml'
PERK_BONUS_VALUE_PRECISION = 5
POINT_BLAST_DISTANCE = 50
SKIP_SE_PERKS: tuple

class PerkState(object):
    INACTIVE = 0
    ACTIVE = 1

class PerkTags(object):
    AUTOPERK = 4
    @classmethod
    def pack(cls, tags):
        ...

class PerkMasks(object):
    PERK_ID_MASK = 1023
    PERK_LEVEL_MASK = 63

class StubPerkIDs(object):
    COMMANDER_TUTOR = 103

class PerkIDs(object):
    LOADER_INTUITION = 403
