# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/qualification_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.qualification_tooltip_view_model import QualificationTooltipViewModel as QualificationTooltipViewModel
from gui.impl.pub import ViewImpl as ViewImpl

class QualificationTooltip(ViewImpl):
    __slots__: tuple
    _roleName: Any
    _isFemale: Any
    _qualificationIndex: Any
    _isBonusQualification: Any
    def __init__(self, qualificationIndex, roleName, isBonusQualification, isFemale):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self):
        ...
