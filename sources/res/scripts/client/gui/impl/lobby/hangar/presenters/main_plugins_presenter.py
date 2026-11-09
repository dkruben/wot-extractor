# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/main_plugins_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/hangar/presenters/main_plugins_presenter.py
from __future__ import absolute_import
import logging
from gui.impl.gen.view_models.views.lobby.hangar.main_plugins_model import MainPluginsModel
from gui.impl.pub.view_component import ViewComponent
_logger = logging.getLogger(__name__)

class MainPluginsPresenter(ViewComponent[MainPluginsModel]):

    def __init__(self):
        super(MainPluginsPresenter, self).__init__(model=MainPluginsModel)

    @property
    def viewModel(self):
        return super(MainPluginsPresenter, self).getViewModel()
