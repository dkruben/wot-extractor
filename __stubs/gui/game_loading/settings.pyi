# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.game_loading import loggers as loggers
from gui.game_loading.resources.cdn.consts import SequenceOrders as SequenceOrders
from gui.game_loading.resources.cdn.models import LocalSlideModel as LocalSlideModel, LocalSequenceModel as LocalSequenceModel, CdnCacheDefaultsModel as CdnCacheDefaultsModel
from gui.game_loading.resources.consts import ImageVfxs as ImageVfxs, MilestonesTypes as MilestonesTypes, LoadingTypes as LoadingTypes, Milestones as Milestones, InfoStyles as InfoStyles
from gui.game_loading.resources.models import StatusTextModel as StatusTextModel, LogoModel as LogoModel
from gui.game_loading.state_machine.models import ImageViewSettingsModel as ImageViewSettingsModel
from gui.game_loading.state_machine.const import DEFAULT_SLIDE_DURATION as DEFAULT_SLIDE_DURATION, DEFAULT_LOGIN_NEXT_SLIDE_DURATION as DEFAULT_LOGIN_NEXT_SLIDE_DURATION, DEFAULT_LOGIN_STATUS_MIN_SHOW_TIME_SEC as DEFAULT_LOGIN_STATUS_MIN_SHOW_TIME_SEC, DEFAULT_SLIDE_TRANSITION_DURATION as DEFAULT_SLIDE_TRANSITION_DURATION, ContentState as ContentState
from gui.game_loading.state_machine.models import LoadingMilestoneModel as LoadingMilestoneModel, ProgressSettingsModel as ProgressSettingsModel
from helpers import getClientLanguage as getClientLanguage
from helpers.i18n import makeString as makeString
from soft_exception import SoftException as SoftException
from ResMgr import DataSection as DataSection
_logger: Any
DEFAULT_TAG = 'default'

class GameLoadingSettings(object):
    __slots__: tuple
    _settings: Any
    _ageRatingPath: Any
    _lang: Any
    def __init__(self, settings):
        ...
    def getLogos(self):
        ...
    def getLoginNextSlideDuration(self):
        ...
    def getCdnCacheDefaults(self):
        ...
    def getProgressSettingsByType(self, loadingType):
        ...
    def getProgressMilestones(self, loadingType):
        ...
    def getClientLoadingStateViewSettings(self):
        ...
    def getLoginStateViewSettings(self):
        ...
    def getPlayerLoadingStateViewSettings(self):
        ...
    def _getStateViewSettings(self, state):
        ...
    def _getAgeRatingPath(self):
        ...
    def _getLoadingTypeSection(self, loadingType):
        ...
