# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/battle_results_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from soft_exception import SoftException as SoftException
from typing import Union as Union, Type as Type, Optional as Optional, Any as Any
from frameworks.wulf import View as View, ViewEvent as ViewEvent, Window as Window, ViewModel as ViewModel, Array as Array
BattleResultsComponentModelType: _Any
TooltipModelType: _Any

class UnexpectedViewModelException(SoftException):
    ...

class BattleResultsSubPresenter(SubModelPresenter):
    _battleResults: _Any
    _subPresenters: _Any
    def __init__(self, viewModel, parentView):
        ...
    @classmethod
    def getViewModelType(cls):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def addSubPresenter(self, subPacker):
        ...
    def removeSubPacker(self, subPacker):
        ...
    def getBattleResults(self):
        ...
    def packBattleResults(self, battleResults):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createContextMenu(self, event):
        ...
