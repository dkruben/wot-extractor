# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousel_event_entry_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import typing as typing
from future.utils import viewitems as viewitems
from gui.Scaleform.daapi.view.meta.CarouselEventEntryMeta import CarouselEventEntryMeta as CarouselEventEntryMeta
from gui.impl.gen import R as R
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.shared.system_factory import collectCarouselEventEntryPoints as collectCarouselEventEntryPoints
from typing import Dict as Dict, Type as Type
from skeletons.gui.hangar import ICarouselEventEntry as ICarouselEventEntry
_VIEWS: dict

class CarouselEventEntryHolder(CarouselEventEntryMeta, IPrbListener):
    __activeViewID: Any
    def __init__(self):
        ...
    def updateState(self):
        ...
    def _onPopulate(self):
        ...
    def _makeInjectView(self, viewID=None):
        ...

def isAnyEntryVisible():
    ...
def _getActiveCarouselEventEntryID():
    ...
