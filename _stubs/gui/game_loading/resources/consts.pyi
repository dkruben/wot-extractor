# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/resources/consts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import enum as enum

class EnumWithValues(enum.Enum):
    @classmethod
    def values(cls):
        ...

# decorador original: @enum.unique
class ImageVfxs(str, EnumWithValues):
    DUST = 'dust'
    FIRE = 'fire'
    FOG = 'fog'
    RAIN = 'rain'
    SNOW = 'snow'
    SUNSHINE = 'sunshine'

# decorador original: @enum.unique
class LoadingTypes(str, EnumWithValues):
    CLIENT = 'client'
    PLAYER = 'player'

# decorador original: @enum.unique
class MilestonesTypes(str, EnumWithValues):
    DEFAULT = 'default'
    STANDARD = 'standard'

# decorador original: @enum.unique
class Milestones(str, EnumWithValues):
    CLIENT_LOADING = 'client_loading'
    SAVING_PDC = 'saving_pdc'
    CONNECTION = 'connection'
    ENTER = 'enter'
    INVENTORY = 'inventory'
    SHOP = 'shop'
    DOSSIER = 'dossier'
    DISCOUNTS = 'discounts'
    RECYCLE_BIN = 'recycleBin'
    PLAYER_DATA = 'playerData'
    HANGAR_SPACE = 'loadHangarSpace'
    UPDATE_VEHICLE = 'updateVehicle'
    HANGAR_SPACE_VEHICLE = 'loadHangarSpaceVehicle'
    HANGAR_UI_READY = 'hangarUIReady'
    HANGAR_READY = 'hangarReady'
    LOAD_CONTENT = 'loadContent'
    SYNCHRONIZE = 'synchronize'
    ONBOARDING_ENQUEUED = 'onboardingEnqueued'

# decorador original: @enum.unique
class InfoStyles(str, EnumWithValues):
    DEFAULT = 'default'
    KOREA = 'korea'
    CHINA = 'china'
