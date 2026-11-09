# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/awards/items_collection_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from copy import deepcopy as deepcopy
import typing as typing
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.battle_pass.battle_pass_award import awardsFactory as awardsFactory
from gui.impl.lobby.awards.packers import getMultipleProductAwardsBonusPacker as getMultipleProductAwardsBonusPacker
from gui.impl.lobby.awards.prefetch import PREFETCHERS as PREFETCHERS
from gui.server_events.bonuses import mergeBonuses as mergeBonuses
from helpers import dependency as dependency
from items.components.component_constants import EMPTY_TUPLE as EMPTY_TUPLE
from skeletons.gui.platform.catalog_service_controller import IPurchaseCache as IPurchaseCache
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
from gui.impl.backport import TooltipData as TooltipData
from gui.platform.catalog_service.controller import _PurchaseDescriptor as _PurchaseDescriptor
from gui.platform.catalog_service.controller import _ProductExtraData as _ProductExtraData
_logger: Any

class _OrderHelper(object):
    @classmethod
    def buildSortedBonusList(cls, validData, order, entitlements):
        ...
    @classmethod
    def _getItemByDictKey(cls, key, validSection):
        ...
    @classmethod
    def _getItemByID(cls, itemID, validSection):
        ...

class MultipleProductAwardRewardsMainPacker(object):
    __purchaseCache: Any
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getWholeBonusesData(self, invoiceData, productCode, callback=None):
        ...
    def __extendSortedBonusList(self, sortedBList, extraData):
        ...
    def __prefetchEssentialData(self, bonuses, productCode):
        ...

def _addCompensation(compensation, toUpdate):
    ...
# decorador original: @adisp_async
# decorador original: @adisp_process
def packProductBonusModelAndTooltipData(bonuses, productCode, callback=None):
    ...
