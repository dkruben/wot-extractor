# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from . import ItemsRequester as ItemsRequester
from .ShopRequester import ShopRequester as ShopRequester
from .InventoryRequester import InventoryRequester as InventoryRequester
from .StatsRequester import StatsRequester as StatsRequester
from .DossierRequester import DossierRequester as DossierRequester
from .GoodiesRequester import GoodiesRequester as GoodiesRequester
from .blueprints_requester import BlueprintsRequester as BlueprintsRequester
from .recycle_bin_requester import RecycleBinRequester as RecycleBinRequester
from .vehicle_rotation_requester import VehicleRotationRequester as VehicleRotationRequester
from .tokens_requester import TokensRequester as TokensRequester
from .session_stats_requester import SessionStatsRequester as SessionStatsRequester
from .ItemsRequester import REQ_CRITERIA as REQ_CRITERIA, RequestCriteria as RequestCriteria, getDiffID as getDiffID
from .TokenRequester import TokenRequester as TokenRequester, getTokenRequester as getTokenRequester, fini as _rq_fini
from .TokenResponse import TokenResponse as TokenResponse
from .abstract import RequestCtx as RequestCtx
from .abstract import DataRequestCtx as DataRequestCtx
from .abstract import RequestsByIDProcessor as RequestsByIDProcessor
from .abstract import DataRequestsByIDProcessor as DataRequestsByIDProcessor
__all__: tuple

def fini():
    ...
