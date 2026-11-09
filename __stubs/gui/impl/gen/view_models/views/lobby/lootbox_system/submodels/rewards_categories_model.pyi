# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/submodels/rewards_categories_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class Type(Enum):
    LOOTBOX = 'lootBox'
    VEHICLES = 'vehicles'
    STYLE = 'style'
    STYLE3D = 'style_3d'
    CREWMEMBER = 'tmanToken'
    PREMIUMPLUS = 'premium_plus'
    CREDITS = 'credits'
    GOLD = 'gold'
    CRYSTAL = 'crystal'
    FREEXP = 'freeXP'
    CUSTOMIZATIONS = 'customizations'
    ATTACHMENT = 'attachment'
    EXPERIMENTALEQUIPMENT = 'experimental_equipment'
    COMPONENTS = 'equipCoin'
    IMPROVEDEQUIPMENT = 'improved_equipment'
    BOUNTYEQUIPMENT = 'trophy_equipment'
    STANDARDEQUIPMENT = 'standard_equipment'
    DIRECTIVES = 'battleBooster_gift'
    MENTORINGLICENSE = 'mentoringLicense'
    CREWBOOK = 'crewBook'
    GUIDE = 'guide'
    BROCHURE = 'brochure'
    RECERTIFICATIONFORM = 'recertificationForm'
    BLUEPRINTS = 'blueprints'
    BATTLEBONUSX5 = 'battle_bonus_x5'
    CREWBONUSX3 = 'crew_bonus_x3'
    PERSONALRESERVES = 'personal_reserves'
    CONSUMABLES = 'consumables'
    RATIONS = 'rations'

class RewardsCategoriesModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getCount(self):
        ...
    def setCount(self, value):
        ...
    def _initialize(self):
        ...
