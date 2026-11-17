# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/presenters/settings_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from inspect import getmembers as getmembers
from past.builtins import long as long
import logging as logging
import typing as typing
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.common.settings_model import SettingsModel as SettingsModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from typing import Type as Type, Dict as Dict, Any as Any, Callable as Callable, TypedDict as TypedDict
Accessor: _Any
_logger: _Any

# base nao representavel no stub: ViewComponent[...]
class SettingsPresenter:
    __Any: _Any
    __settingsKey: _Any
    __readOnly: _Any
    __settingsMap: _Any
    def __init__(self, modelCls, accountSettingsKey, readOnly=False):
        ...
    @property
    def viewModel(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __fillModel(self):
        ...
    # decorador original: @args2params(...)
    def __onUpdateSetting(self, section, key, value):
        ...
    def __onAccountSettingsUpdated(self, settingsKey, _):
        ...
