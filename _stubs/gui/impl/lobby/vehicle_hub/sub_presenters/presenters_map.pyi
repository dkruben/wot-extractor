# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/presenters_map.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from functools import partial as partial
from future.utils import itervalues as itervalues
from gui.impl.lobby.vehicle_hub.sub_presenters.sub_presenter_base import SubPresenterBase as SubPresenterBase
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.vehicle_hub_view_model import VehicleHubViewModel as VehicleHubViewModel
SubModelInfo: Any

class PresentersMap(object):
    __presentersCache: Any
    __mainView: Any
    __loadersMap: Any
    def __init__(self, mainView):
        ...
    def itervalues(self):
        ...
    def clear(self):
        ...
    def __getitem__(self, item):
        ...
    def __tryToLoadPresenter(self, key):
        ...
    def __loadOverview(self):
        ...
    def __loadModules(self):
        ...
    def __loadStats(self):
        ...
    def __loadVehSkillTree(self):
        ...
    def __loadArmor(self):
        ...
    @staticmethod
    def __makeSubModel(viewAlias, loader):
        ...
