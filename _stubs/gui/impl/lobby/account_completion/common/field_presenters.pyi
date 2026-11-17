# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/common/field_presenters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
from abc import ABCMeta as ABCMeta, abstractmethod as abstractmethod
import typing as typing
from Event import Event as Event
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.account_completion.common.field_email_model import FieldEmailModel as FieldEmailModel
from gui.impl.lobby.account_completion.common import errors as errors
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_field_model import BaseFieldModel as BaseFieldModel
_EMAIL_PATTERN: Any

class BaseFieldPresenter(object, metaclass=ABCMeta):
    __slots__: tuple
    _value: Any
    _viewModel: Any
    onValueChanged: Any
    onFocusLost: Any
    def __init__(self, viewModel):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def value(self):
        ...
    @property
    def isValid(self):
        ...
    def clear(self):
        ...
    def setValue(self, value):
        ...
    def dispose(self):
        ...
    def validate(self):
        ...
    @abstractmethod
    def _validateChangedValue(self):
        ...
    @abstractmethod
    def _validateValueWhenFocusChanged(self):
        ...
    def __valueChangeHandler(self, args):
        ...
    def __lostFocusChangeHandler(self):
        ...

class EmailPresenter(BaseFieldPresenter):
    __slots__: tuple
    def __init__(self, viewModel):
        ...
    @property
    def viewModel(self):
        ...
    def _validateChangedValue(self):
        ...
    def _validateValueWhenFocusChanged(self):
        ...

class CodePresenter(BaseFieldPresenter):
    __slots__: tuple
    def _validateChangedValue(self):
        ...
    def _validateValueWhenFocusChanged(self):
        ...
