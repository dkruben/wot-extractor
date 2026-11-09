# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/base/hangar_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria
from Event import Event as Event
from gui.shared.gui_items import Vehicle as Vehicle

class IVehicleFilter(object):
    onDiff = None
    @property
    def criteria(self):
        ...
    @property
    def vehicles(self):
        ...
    def initialize(self):
        ...
    def destroy(self):
        ...

class IAccountStyles(object):
    onChanged = None
    @property
    def criteria(self):
        ...
    def initialize(self):
        ...
    def destroy(self):
        ...
