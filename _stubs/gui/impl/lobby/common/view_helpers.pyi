# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/view_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.server_events.bonuses import processAttachmentsSetTokens as processAttachmentsSetTokens
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from typing import TypeVar as TypeVar, Optional as Optional, Dict as Dict, List as List
from frameworks.wulf import Array as Array
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
BonusModelType: Any
_logger: Any

def packBonusModelAndTooltipData(bonuses, bonusModelsList, tooltipData=None, packer=None, showAttachmentsSets=False):
    ...
def _packBonusTooltip(bonusModel, bonusIndex, bonusTooltipList, bonusContentIdList, tooltipData, tooltipIndex):
    ...
