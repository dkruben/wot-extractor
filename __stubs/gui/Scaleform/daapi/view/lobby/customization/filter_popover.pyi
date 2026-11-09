# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/filter_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import OrderedDict as OrderedDict
from future.utils import iteritems as iteritems
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs as CustomizationTabs
from gui.Scaleform.daapi.view.meta.CustomizationFiltersPopoverMeta import CustomizationFiltersPopoverMeta as CustomizationFiltersPopoverMeta
from gui.customization.shared import PROJECTION_DECAL_TEXT_FORM_TAG as PROJECTION_DECAL_TEXT_FORM_TAG
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency
from items.components.c11n_constants import ProjectionDecalFormTags as ProjectionDecalFormTags, Rarity as Rarity
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from uilogging.customization_3d_objects.logger import CustomizationFilterLogger as CustomizationFilterLogger
from uilogging.customization_3d_objects.logging_constants import CustomizationFilterButtons as CustomizationFilterButtons, CustomizationViewKeys as CustomizationViewKeys
_logger: Any

class FiltersPopoverVO(object):
    __slots__: tuple
    lblTitle: Any
    lblGroups: Any
    lblShowOnlyFilters: Any
    lblAdditional: Any
    additionalCheckBoxData: Any
    btnDefault: Any
    groupType: Any
    btnDefaultTooltip: Any
    groupTypeSelectedIndex: Any
    filterBtns: Any
    additionalEnabled: Any
    formsBtns: Any
    formsBtnsLbl: Any
    raritiesBtns: Any
    raritiesBtnsLbl: Any
    def __init__(self, lblTitle, lblGroups, lblShowOnlyFilters, lblAdditional, additionalCheckBoxData, btnDefault, groupType, btnDefaultTooltip, groupTypeSelectedIndex, filterBtns, additionalEnabled, formsBtns=None, formsBtnsLbl='', raritiesBtns=None, raritiesBtnsLbl=''):
        ...
    def asDict(self):
        ...

class FilterPopover(CustomizationFiltersPopoverMeta):
    PROJECTION_DECAL_IMAGE_FORM_TAG: dict
    service: Any
    __ctx: Any
    __filterChangeHandlers: Any
    _purchasedToggleEnabled: Any
    _historicToggleEnabled: Any
    _nonHistoricToggleEnabled: Any
    _fantasticalToggleEnabled: Any
    _appliedToggleEnabled: Any
    _groups: Any
    _selectedGroup: Any
    _groupCount: Any
    _hideOnAnotherVehEnabled: Any
    _showOnlyProgressionDecalsEnabled: Any
    _showOnlyEditableStylesEnabled: Any
    _showOnlyNonEditableStylesEnabled: Any
    _formfactorTypes: Any
    _raritiesGroup: Any
    __uiLogger: Any
    __updateVO: Any
    _isInit: Any
    def __init__(self, ctx=None):
        ...
    def onFilterChange(self, index, value):
        ...
    def onFormChange(self, index, value):
        ...
    def onRarityChange(self, index, value):
        ...
    def setShowOnlyHistoric(self, value):
        ...
    def setShowOnlyNonHistoric(self, value):
        ...
    def setShowOnlyFantastical(self, value):
        ...
    def setShowOnlyAcquired(self, value):
        ...
    def setHideOnAnotherVeh(self, value):
        ...
    def setShowOnlyProgressionDecals(self, value):
        ...
    def setShowOnlyEditableStyles(self, value):
        ...
    def setShowOnlyNonEditableStyles(self, value):
        ...
    def setShowOnlyApplied(self, value):
        ...
    def changeGroup(self, itemId):
        ...
    def updateDefaultButton(self):
        ...
    def setDefaultFilter(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __createUpdateVO(self):
        ...
