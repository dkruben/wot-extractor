# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_post_progression/vo_builders/cfg_page_vos.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.gui_items.Vehicle import getTypeBigIconPath as getTypeBigIconPath
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import resolveStateTooltip as resolveStateTooltip
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.veh_post_progression.vo_builders.base_page_vos import getBaseButtonsVO as getBaseButtonsVO, getBaseDataVO as getBaseDataVO, getBaseTitleVO as getBaseTitleVO
from helpers import int2roman as int2roman, dependency as dependency
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_DEMOUNT_VISIBILITY_COUNT = 2

# decorador original: @dependency.replace_none_kwargs(...)
def _getButtonsVO(vehicle, goToVehicleAllowed, cmpBasket=None):
    ...
def getDataVO(vehicle, freeExp, goToVehicleAllowed):
    ...
def getTitleVO(vehicle):
    ...
