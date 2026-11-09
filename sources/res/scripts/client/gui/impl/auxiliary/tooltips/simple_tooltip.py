# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/auxiliary/tooltips/simple_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/auxiliary/tooltips/simple_tooltip.py
from __future__ import absolute_import
import typing
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.tooltips.simple_icon_tooltip_model import HeaderType
from gui.impl.lobby.common.tooltips.simple_icon_tooltip_view import SimpleIconTooltipView
from gui.impl.pub.tooltip_window import SimpleTooltipContent
if typing.TYPE_CHECKING:
    from frameworks.wulf import View, ViewEvent

def createSimpleTooltip(parent, event, header='', body=''):
    window = DecoratedTooltipWindow(parent=parent, content=SimpleTooltipContent(R.views.common.tooltip_window.simple_tooltip_content.SimpleTooltipContent(), body=body, header=header))
    window.load()
    window.move(event.mouse.positionX, event.mouse.positionY)
    return window


def createSimpleIconTooltip(event):
    return SimpleIconTooltipView(event.getArgument('header', ''), event.getArgument('body', ''), event.getArgument('icon', ''), event.getArgument('headerType', HeaderType.NORMAL))
