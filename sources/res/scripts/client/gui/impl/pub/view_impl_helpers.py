# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/pub/view_impl_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/view_impl_helpers.py
from __future__ import absolute_import
import logging, json, typing
from soft_exception import SoftException
from helpers import dependency
from gui.impl.pub.tooltip_window import ToolTipWindow
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewEvent, Window
_logger = logging.getLogger(__name__)

def createBackportContextMenuWindow(event, parentWindow):
    menuId = event.getArgument('menuId')
    menuArgs = event.getArgument('menuArgs', None)
    if not menuId:
        _logger.error('Context menu - menuId is not specified')
        return
    else:
        args = json.loads(menuArgs)
        from gui.impl.backport import createContextMenuData, BackportContextMenuWindow
        contextMenuData = createContextMenuData(menuId, args)
        if contextMenuData is not None:
            window = BackportContextMenuWindow(contextMenuData, parentWindow)
            window.load()
            return window
        raise SoftException('Preparing of BackportContextMenu with json args failed: contextMenuData is None or invalid.')
        return


def createWulfTooltipWindow(event, parentWindow):
    from skeletons.gui.app_loader import IAppLoader
    tooltipId = event.getArgument('tooltipId')
    tooltipArgs = event.getArgument('tooltipArgs', None)
    if not tooltipId:
        _logger.error('WulfTooltipContent. TooltipId is not specified.')
        return
    else:
        args = json.loads(tooltipArgs)
        appLoader = dependency.instance(IAppLoader)
        tooltipMgr = appLoader.getApp().getToolTipMgr()
        tooltipMgr.onCreateWulfTooltip(tooltipId, args, event.mouse.positionX, event.mouse.positionY, ownerViewID=event.targetViewID)
        wulfTooltipWindow = tooltipMgr.tooltipWindow
        if parentWindow is not None:
            wulfTooltipWindow.setParent(parentWindow)
        return wulfTooltipWindow


def createParamTooltipWindow(event, parentWindow):
    from gui.impl.common.param_tooltip_view import ParamTooltipView
    tooltipType = event.getArgument('type')
    params = event.getArgument('params', None)
    resId = event.getArgument('resId', None)
    if not tooltipType:
        _logger.error('Can not create ParamTooltipWindow: tooltip type is not specified')
        return
    else:
        if not resId:
            _logger.error('Can not create ParamTooltipWindow: resId is not specified')
            return
        window = ToolTipWindow(event, ParamTooltipView(tooltipType, params, int(resId)), parentWindow)
        return window
