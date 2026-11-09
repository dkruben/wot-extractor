# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/resources/consts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/resources/consts.py
import typing, enum

class EnumWithValues(enum.Enum):

    @classmethod
    def values(cls):
        return [obj.value for obj in cls.__members__.values()]


@enum.unique
class ImageVfxs(str, EnumWithValues):
    DUST = 'dust'
    FIRE = 'fire'
    FOG = 'fog'
    RAIN = 'rain'
    SNOW = 'snow'
    SUNSHINE = 'sunshine'


@enum.unique
class LoadingTypes(str, EnumWithValues):
    CLIENT = 'client'
    PLAYER = 'player'


@enum.unique
class MilestonesTypes(str, EnumWithValues):
    DEFAULT = 'default'
    STANDARD = 'standard'


@enum.unique
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


@enum.unique
class InfoStyles(str, EnumWithValues):
    DEFAULT = 'default'
    KOREA = 'korea'
    CHINA = 'china'
