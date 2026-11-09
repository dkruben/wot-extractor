# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/Scaleform/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/Scaleform/__init__.py
from __future__ import absolute_import, print_function
AVAILABLE = False
try:
    from _Scaleform import *
    AVAILABLE = True
except ImportError:
    print('There is no module named _Scaleform.  The most likely cause of this     is the client was built without Scaleform support.  Please check the     documentation for further details on enabling Scaleform support.')

def showCursor():
    import GUI, BigWorld
    c = GUI.mcursor()
    c.visible = 1
    BigWorld.setCursor(c)


def exampleFSCommandHandler(cmd, s2):
    print('FSCommand - ', cmd, s2)


def exampleExternalInterfaceHandler(cmd, *args):
    print('External Interface command - ', cmd, args)


def createMovieInstance(file='scaleform/d3d9guide.swf'):
    mv = None
    mvDef = MovieDef(file)
    mv = mvDef.createInstance()
    mv.backgroundAlpha = 0.0
    mv.setFSCommandCallback(exampleFSCommandHandler)
    mv.setExternalInterfaceCallback(exampleExternalInterfaceHandler)
    mv.setFocussed()
    return (mv, mvDef)


def create3DDemo():
    file = 'scaleform/dogfight.swf'
    return createMovieInstance(file)


def createMovieGUI(file='scaleform/d3d9guide.swf'):
    m, _ = createMovieInstance(file)
    import GUI
    for i in GUI.roots():
        i.position[2] = max(i.position[2], 0.1)

    f = GUI.Flash(m)
    f.position = (0, 0, 0)
    f.focus = True
    f.moveFocus = True
    GUI.addRoot(f)
    showCursor()
    return f


def createIMEFontsMovie():
    print('Fonts loading from Python is not supported anymore.')


def createIME():
    print('Fonts mapping from Python is not supported anymore.')
    showCursor()


def createIMEMovie():
    file = 'scaleform/IMESample.swf'
    return createMovieInstance(file)


def createFontMovie(file='scaleform/drawtext_fonts.swf'):
    print('Fonts loading from Python is not supported anymore.')


def createAllFontsMovie():
    print('Fonts loading from Python is not supported anymore.')


def createFlashText(fontName='Slate Mobile'):
    import GUI
    g = GUI.FlashText(u'some label', fontName)
    g.size = (2, 2)
    g.position = (0, 0, 0)
    return g
