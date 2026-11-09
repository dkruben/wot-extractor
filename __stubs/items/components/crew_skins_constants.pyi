# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/crew_skins_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

CREW_SKINS_XML_FILE = 'crewSkins.xml'
CREW_SKINS_PRICE_GROUPS_XML_FILE = 'priceGroups.xml'
NO_CREW_SKIN_ID = 0
NO_CREW_SKIN_SOUND_SET = '-'

class CREW_SKIN_PROPERTIES_MASKS:
    SEX = 2
    NATION = 4
    EMPTY_MASK = 0

class CrewSkinType:
    CREW_SKIN = 1
    ITEM_GROUP = 2
    RANGE: set

class TANKMAN_SEX:
    NONE = ''
    MALE = 'male'
    FEMALE = 'female'
    ALL: tuple
    AVAILABLE: tuple
    @staticmethod
    def getTankmanSex(tmanDescr):
        ...

class CREW_SKIN_RARITY:
    COMMON = 1
    RARE = 2
    EPIC = 3
    ALL: tuple
