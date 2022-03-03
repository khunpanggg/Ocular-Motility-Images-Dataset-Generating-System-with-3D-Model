import maya.cmds as cmds
import random as rand


def createUI(windowTitle):
    window = 'OC_Window'
    # create new window
    window = cmds.window(window, title=windowTitle,
                         resizeToFitChildren=True, sizeable=True)
    cmds.columnLayout(adjustableColumn=True)
    cmds.rowColumnLayout(numberOfColumns=2, columnAttach=(
        (1, 'right', 2), (2, 'both', 3)), columnWidth=[(1, 250)], columnOffset=[(1, 'both', 2)])

    # ------------ Preparation ------------
    cmds.frameLayout(label='Preparation', collapsable=True, marginWidth=5)
    cmds.frameLayout(label='Import Flie', collapsable=True)
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
                        (1, 125), (2, 125)], columnOffset=[(1, 'both', 10)], bgc=[0.2, 0.2, 0.2])
    cmds.button(label='Open Scene', command=openFile, bgc=[0.4, 0.4, 0.4])
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.setParent('..')
    cmds.frameLayout(label='Setting Gaze', collapsable=True)
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
                        (1, 125), (2, 125)], columnOffset=[(1, 'both', 10)], bgc=[0.2, 0.2, 0.2])
    cmds.button(label='Set Gaze', command=openFile, bgc=[0.4, 0.4, 0.4])
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.button(label='Blend Shape', command=openFile, bgc=[0.4, 0.4, 0.4])
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.setParent('..')
    cmds.frameLayout(label='Tool', collapsable=True)
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
                        (1, 125), (2, 125)], columnOffset=[(1, 'both', 10)], bgc=[0.2, 0.2, 0.2])
    cmds.button(label='Reset', command=openFile, bgc=[0.4, 0.4, 0.4])
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Setting for 9 diagnostic positions of gaze ------------------
    frameDiaSetting = cmds.frameLayout('frameDiaSetting',
                                       label='Setting for 9 diagnostic positions of gaze', enable=True, borderVisible=False, collapsable=True)
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 300), (2, 300), (3, 300)], columnOffset=[(1, 'both', 3), (2, 'both', 3), (3, 'both', 3)])

    # ------------------ Right & Up Gaze ------------------
    cmds.frameLayout(label='Right & Up Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('SR', bgc=[0.1, 0.1, 0.1])
    cmds.text('IO', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RSR
    checkBox_RSR = cmds.checkBox('checkBox_RSR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_RSR', 'radioOver_RSR', 'radioUnder_RSR'))
    collectEyes_RSR = cmds.radioCollection()
    radioOver_RSR = cmds.radioButton(
        'radioOver_RSR', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_RSR'))
    radioUnder_RSR = cmds.radioButton('radioUnder_RSR', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_RSR'))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LIO
    checkBox_LIO = cmds.checkBox('checkBox_LIO', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_LIO', 'radioOver_LIO', 'radioUnder_LIO'))
    collectEyes_LIO = cmds.radioCollection()
    radioOver_LIO = cmds.radioButton(
        'radioOver_LIO', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_LIO'))
    radioUnder_LIO = cmds.radioButton('radioUnder_LIO', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_LIO'))
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Up Gaze ------------------
    cmds.frameLayout(label='Up Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('SR (IO)', bgc=[0.1, 0.1, 0.1])
    cmds.text('SR (IO)', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RSR
    checkBox_RSRIO = cmds.checkBox('checkBox_RSRIO', label='normal', value=False,
                                   changeCommand=lambda x: action_checkBox('checkBox_RSRIO', 'radioOver_RSRIO', 'radioUnder_RSRIO'))
    collectEyes_RSRIO = cmds.radioCollection()
    radioOver_RSRIO = cmds.radioButton(
        'radioOver_RSRIO', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_RSRIO'))
    radioUnder_RSRIO = cmds.radioButton(
        'radioUnder_RSRIO', label='underaction',
        changeCommand=lambda x: action_checkRadioButton('radioUnder_RSRIO'))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LIO
    checkBox_LSRIO = cmds.checkBox('checkBox_LSRIO', label='normal', value=False,
                                   changeCommand=lambda x: action_checkBox('checkBox_LSRIO', 'radioOver_LSRIO', 'radioUnder_LSRIO'))
    collectEyes_LSRIO = cmds.radioCollection()
    radioOver_LSRIO = cmds.radioButton(
        'radioOver_LSRIO', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_LSRIO'))
    radioUnder_LSRIO = cmds.radioButton(
        'radioUnder_LSRIO', label='underaction',
        changeCommand=lambda x: action_checkRadioButton('radioUnder_LSRIO'))
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Left & Up Gaze ------------------
    cmds.frameLayout(label='Left & Up Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('IO', bgc=[0.1, 0.1, 0.1])
    cmds.text('SR', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RIO
    checkBox_RIO = cmds.checkBox('checkBox_RIO', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_RIO', 'radioOver_RIO', 'radioUnder_RIO'))
    collectEyes_RIO = cmds.radioCollection()
    radioOver_RIO = cmds.radioButton(
        'radioOver_RIO', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_RIO'))
    radioUnder_RIO = cmds.radioButton('radioUnder_RIO', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_RIO'))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
                        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LSR
    checkBox_LSR = cmds.checkBox('checkBox_LSR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_LSR', 'radioOver_LSR', 'radioUnder_LSR'))
    collectEyes_LSR = cmds.radioCollection()
    radioOver_LSR = cmds.radioButton(
        'radioOver_LSR', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_LSR'))
    radioUnder_LSR = cmds.radioButton('radioUnder_LSR', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_LSR'))
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Right Gaze ------------------
    cmds.frameLayout(label='Right Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('LR', bgc=[0.1, 0.1, 0.1])
    cmds.text('MR', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RLR
    checkBox_RLR = cmds.checkBox('checkBox_RLR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_RLR', 'radioOver_RLR', 'radioUnder_RLR'))
    collectEyes_RLR = cmds.radioCollection()
    radioOver_RLR = cmds.radioButton(
        'radioOver_RLR', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_RLR'))
    radioUnder_RLR = cmds.radioButton('radioUnder_RLR', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_RLR'))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LMR
    checkBox_LMR = cmds.checkBox('checkBox_LMR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_LMR', 'radioOver_LMR', 'radioUnder_LMR'))
    collectEyes_LMR = cmds.radioCollection()
    radioOver_LMR = cmds.radioButton(
        'radioOver_LMR', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_LMR'))
    radioUnder_LMR = cmds.radioButton('radioUnder_LMR', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_LMR'))
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Primary Position ------------------
    cmds.frameLayout(label='Primary Position')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Left Gaze ------------------
    cmds.frameLayout(label='Left Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('MR', bgc=[0.1, 0.1, 0.1])
    cmds.text('LR', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RMR
    checkBox_RMR = cmds.checkBox('checkBox_RMR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_RMR', 'radioOver_RMR', 'radioUnder_RMR'))
    collectEyes_RMR = cmds.radioCollection()
    radioOver_RMR = cmds.radioButton(
        'radioOver_RMR', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_RMR'))
    radioUnder_RMR = cmds.radioButton('radioUnder_RMR', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_RMR'))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LLR
    checkBox_LLR = cmds.checkBox('checkBox_LLR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_LLR', 'radioOver_LLR', 'radioUnder_LLR'))
    collectEyes_LLR = cmds.radioCollection()
    radioOver_LLR = cmds.radioButton(
        'radioOver_LLR', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_LLR'))
    radioUnder_LLR = cmds.radioButton('radioUnder_LLR', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_LLR'))
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Right & Down Gaze ------------------
    cmds.frameLayout(label='Right & Down Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('IR', bgc=[0.1, 0.1, 0.1])
    cmds.text('SO', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RIR
    checkBox_RIR = cmds.checkBox('checkBox_RIR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_RIR', 'radioOver_RIR', 'radioUnder_RIR'))
    collectEyes_RIR = cmds.radioCollection()
    radioOver_RIR = cmds.radioButton(
        'radioOver_RIR', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_RIR'))
    radioUnder_RIR = cmds.radioButton('radioUnder_RIR', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_RIR'))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LSO
    checkBox_LSO = cmds.checkBox('checkBox_LSO', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_LSO', 'radioOver_LSO', 'radioUnder_LSO'))
    collectEyes_LSO = cmds.radioCollection()
    radioOver_LSO = cmds.radioButton(
        'radioOver_LSO', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_LSO'))
    radioUnder_LSO = cmds.radioButton('radioUnder_LSO', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_LSO'))
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Down Gaze ------------------
    cmds.frameLayout(label='Up Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('IR (SO)', bgc=[0.1, 0.1, 0.1])
    cmds.text('IR (SO)', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RIR
    checkBox_RIRSO = cmds.checkBox('checkBox_RIRSO', label='normal', value=False,
                                   changeCommand=lambda x: action_checkBox('checkBox_RIRSO', 'radioOver_RIRSO', 'radioUnder_RIRSO'))
    collectEyes_RIRSO = cmds.radioCollection()
    radioOver_RIRSO = cmds.radioButton(
        'radioOver_RIRSO', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_RIRSO'))
    radioUnder_RIRSO = cmds.radioButton('radioUnder_RIRSO', label='underaction',
                                        changeCommand=lambda x: action_checkRadioButton('radioUnder_RIRSO'))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LSO
    checkBox_LIRSO = cmds.checkBox('checkBox_LSO', label='normal', value=False,
                                   changeCommand=lambda x: action_checkBox('checkBox_LSO', 'radioOver_LIRSO', 'radioUnder_LIRSO'))
    collectEyes_LIRSO = cmds.radioCollection()
    radioOver_LIRSO = cmds.radioButton(
        'radioOver_LIRSO', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_LIRSO'))
    radioUnder_LIRSO = cmds.radioButton('radioUnder_LIRSO', label='underaction',
                                        changeCommand=lambda x: action_checkRadioButton('radioUnder_LIRSO'))
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Left & Down Gaze ------------------
    cmds.frameLayout(label='Left & Down Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('SO', bgc=[0.1, 0.1, 0.1])
    cmds.text('IR', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RSO
    checkBox_RSO = cmds.checkBox('checkBox_RSO', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_RSO', 'radioOver_RSO', 'radioUnder_RSO'))
    collectEyes_RSO = cmds.radioCollection()
    radioOver_RSO = cmds.radioButton(
        'radioOver_RSO', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_RSO'))
    radioUnder_RSO = cmds.radioButton('radioUnder_RSO', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_RSO'))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LIR
    checkBox_LIR = cmds.checkBox('checkBox_LIR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox('checkBox_LIR', 'radioOver_LIR', 'radioUnder_LIR'))
    collectEyes_LIR = cmds.radioCollection()
    radioOver_LIR = cmds.radioButton(
        'radioOver_LIR', label='overaction', select=True, changeCommand=lambda x: action_checkRadioButton('radioOver_LIR'))
    radioUnder_LIR = cmds.radioButton('radioUnder_LIR', label='underaction',
                                      changeCommand=lambda x: action_checkRadioButton('radioUnder_LIR'))
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.setParent('..')

    # ------------------ Amount ------------------
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 450), (2, 450)], columnOffset=[(1, 'both', 2)])
    cmds.frameLayout(label='Amount of Images', collapsable=True)
    cmds.separator(height=5, style=None)
    cmds.rowColumnLayout(numberOfColumns=3, columnAttach=(
        (1, 'right', 3), (2, 'both', 3), (3, 'both', 3)), columnWidth=[(1, 100), (2, 150)])
    cmds.text(label='amount :')
    AmoutImages = cmds.textField()
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')

    cmds.separator(height=5, style=None)
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Create Lighting ------------------
    cmds.frameLayout(label='Create Lighting', collapsable=True)
    cmds.separator(height=5, style=None)
    cmds.rowColumnLayout(numberOfColumns=2, columnAttach=((1, 'both', 2)))
    cmds.optionMenuGrp('optionLighting', w=250, label="lightning location :")
    cmds.menuItem(label="Outdoor")
    cmds.menuItem(label="Skies")
    cmds.menuItem(label="Indoor")
    cmds.menuItem(label="Studio")
    cmds.menuItem(label="Nature")
    cmds.menuItem(label="Urban")
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.separator(height=5, style=None)
    cmds.setParent('..')
    cmds.setParent('..')

    def applyButton(*args):

        getValueNine = setNinePositionOfGaze(AmoutImages)
        loadWindowPreview_Abnormal(
            getValueNine[0], getValueNine[1], getValueNine[2], AmoutImages)

    def cancelCallback(*args):
        if cmds.window(window, exists=True):
            cmds.deleteUI(window)

    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 300), (2, 300), (3, 300)], columnOffset=[(1, 'both', 3), (2, 'both', 3), (3, 'both', 3)])
    cmds.button(label='Apply', height=30, command=applyButton)
    cmds.button(label='Render')
    cmds.button(label='Close', command=cancelCallback)
    cmds.setParent('..')
    cmds.showWindow()

# ------------------ openFile ------------------


def openFile(self):
    filename = cmds.fileDialog2(fileMode=1, caption="Import File")
    cmds.file(filename[0], i=True)

# ------------------ loadWindowPreview ------------------


def playblastPreview():
    cmds.lookThru('camera1')
    cmds.lookThru(q=True)
    cmds.playblast(filename="C:/Users/Khunpang/Documents/maya/projects/Matahuman/movies/man",
                   startTime=1,
                   format="image",
                   viewer=False,
                   compression="jpg",
                   clearCache=1,
                   fp=4,
                   percent=100,
                   quality=100,
                   widthHeight=[250, 65],
                   showOrnaments=False,
                   offScreen=True)


def loadWindowPreview(endframe, nameGaze, scaleGaze, textfieldAmount):

    def cancelCallback(*args):
        if cmds.window(window, exists=True):
            cmds.deleteUI(window)

    amount = getAmountValue(textfieldAmount)
    # create new window
    window = cmds.window(title='9 Diagnostic Positions of Gaze Preview',
                         resizeToFitChildren=True, sizeable=True)

    form = cmds.formLayout()
    sl = cmds.scrollLayout(childResizable=True)
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 250), (2, 250), (3, 250)], columnOffset=[(1, 'both', 2), (2, 'both', 3), (3, 'both', 3)])

    count = 0
    for i in range(endframe):
        print(i)
        # cmds.shelfLayout('%s' % nameGaze[i], cellWidthHeight=[300, 50])
        cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
                            (1, 250), (2, 250), (3, 250)])

        # print(scaleGaze[i], scaleGaze[num])
        cmds.picture(image=(
            'C:/Users/Khunpang/Documents/maya/projects/Matahuman/movies/man.%04d.jpg' % (i+1)))
        count += 1
        if count == 9:
            cmds.separator(height=20, style=None)
            cmds.separator(height=20, style=None)
            cmds.separator(height=20, style=None)
            count = 0

            # cmds.text(('No. %d \n Right: %s Left: %s' % (num+1, scaleGaze[num+i][1][0], scaleGaze[num+i][1][1])),
            #               font="boldLabelFont", align='center')

        cmds.setParent('..')

    cmds.setParent('..')
    cmds.setParent('..')

    rc = cmds.rowColumnLayout(numberOfColumns=2, columnOffset=(
        1, 'both', 5), columnWidth=[(1, 380), (2, 380)])
    cmds.text('total 9 diagnostic positions of gaze : 6 ')
    cmds.text('total picture : 36 ')
    cmds.separator(height=5, style=None)
    cmds.separator(height=5, style=None)
    cmds.button(label='Render', height=30)
    cmds.button(label='Back', command=cancelCallback)
    cmds.setParent("..")
    cmds.setParent("..")
    cmds.formLayout(form, edit=True, attachForm=[(sl, 'top', 5), (sl, 'right', 5), (sl, 'left', 5), (
        sl, 'top', 5), (sl, 'bottom', 60), (rc, 'bottom', 5), (rc, 'left', 5), (rc, 'right', 5)])

    cmds.showWindow(window)


def loadWindowPreview_Abnormal(endframe, nameGaze, scaleGaze, amount):
    playblastPreview()
    loadWindowPreview(endframe, nameGaze, scaleGaze, amount)

# ------------------- getAmountValue -------------------


def getAmountValue(textfieldAmount):
    currentAmount = cmds.textField(textfieldAmount, query=True, text=True)
    # print('Amount'+currentAmount)
    return int(currentAmount)

# ------------------- set Position Of Gaze (NORMAL) -------------------


def setNormalPositionOfGaze(textfieldAmount):
    amount = getAmountValue(textfieldAmount)
    value_noise = []

    for i in range(amount):
        cmds.setKeyframe('ctrlEye_R.translateX', at='tx', v=0, t=i+1)
        cmds.setKeyframe('ctrlEye_R.translateY', at='ty', v=0, t=i+1)
        cmds.setKeyframe('ctrlEye_L.translateX', at='tx', v=0, t=i+1)
        cmds.setKeyframe('ctrlEye_L.translateY', at='ty', v=0, t=i+1)

        value_noise.append(round(rand.uniform(-1, 1), 4))

        cmds.setKeyframe('AimEye_R.translateX', at='tx',
                         v=value_noise[i], t=i+1)
        cmds.setKeyframe('AimEye_L.translateX', at='ty',
                         v=value_noise[i], t=i+1)


lst_Nine = [('Right Up', [-1, 1]), ('Up gaze', [0, 1]), ('Left Up', [1, 1]),
            ('Right', [-1, 0]), ('Primary', [0, 0]), ('Left', [1, 0]),
            ('Right Down', [-1, -1]), ('Downgaze', [0, -1]), ('Left Down', [1, -1])]

# ('name gaze', [x,y])
lstActionOU = [  # OVER ACTION
    ('radioOver_RSR', [rand.uniform(-0.5, -1), rand.uniform(0.5, 1)]),
    ('radioOver_RLR', [rand.uniform(-0.8, -0.5), 0]),
    ('radioOver_RIR', [
        rand.uniform(-1.5, -0.5), rand.uniform(-1.5, -0.5)]),
    ('radioOver_LIO', [
        rand.uniform(-1, -0.5), rand.uniform(0.5, 1)]),
    ('radioOver_LMR', [rand.uniform(0, -1), 0]),
    ('radioOver_LSO', [
        rand.uniform(-1.5, -0.5), rand.uniform(-1, -0.5)]),
    ('radioOver_RIO', [rand.uniform(
        0.5, 1), rand.uniform(0.5, 1)]),
    ('radioOver_RMR', [rand.uniform(0.8, 0.5), 0]),
    ('radioOver_RSO', [rand.uniform(
        0.5, 0.3), rand.uniform(-0.5, -0.3)]),
    ('radioOver_LSR', [rand.uniform(
        0.5, 1), rand.uniform(0.5, 1)]),
    ('radioOver_LLR', [rand.uniform(-1, 0), 0]),
    ('radioOver_LIR', [rand.uniform(
        0.5, 0.3), rand.uniform(-0.5, -0.3)]),
    # UNDER ACTION
    ('radioUnder_RSR', [rand.uniform(4, 0.5), rand.uniform(-0.5, -4)]),
    ('radioUnder_RLR', [rand.uniform(15, 0.5), 0]),
    ('radioUnder_RIR', [rand.uniform(
        10, 0.5), rand.uniform(10, 0.5)]),
    ('radioUnder_LIO', [rand.uniform(
        1, 0.5), rand.uniform(-0.5, -1)]),
    ('radioUnder_LMR', [rand.uniform(15, 0.5), 0]),
    ('radioUnder_LSO', [rand.uniform(
        10, 0.5), rand.uniform(10, 0.5)]),
    ('radioUnder_RIO', [
        rand.uniform(-0.5, -1), rand.uniform(-0.5, -1)]),
    ('radioUnder_RMR', [rand.uniform(-15, -0.5), 0]),
    ('radioUnder_RSO', [
        rand.uniform(-15, -0.5), rand.uniform(10, 0.5)]),
    ('radioUnder_LSR', [
        rand.uniform(-4, -0.5), rand.uniform(-4, -0.5)]),
    ('radioUnder_LLR', [rand.uniform(15, 0.5), 0]),
    ('radioUnder_LIR', [rand.uniform(-15, -0.5), rand.uniform(10, 0.5)])]

# ------------------- set Position Of Gaze (NORMAL) -------------------


def setNinePositionOfGaze(textfieldAmount):
    amount = getAmountValue(textfieldAmount)
    value_noise = []
    lst_namegaze = []
    lst_scalegaze = []
    time_value = 0
    time_scale = 0
    all_scale_R_r = []
    all_scale_R_l = []
    for _ in range(amount):
        for x, scale in lst_Nine:
            time_value += 1
            cmds.playbackOptions(edit=True, maxTime=time_value)
            cmds.setKeyframe('ctrlEye_R.translateX', at='tx',
                             v=scale[0], t=time_value)
            cmds.setKeyframe('ctrlEye_R.translateY', at='ty',
                             v=scale[1], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateX', at='tx',
                             v=scale[0], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateY', at='ty',
                             v=scale[1], t=time_value)

    for i in range(amount):
        for x, scale in lst_Nine:
            # print(scale)
            lst_namegaze.append(x)
            time_scale += 1
            cmds.playbackOptions(edit=True, maxTime=time_value)
            value_noise.append(round(rand.uniform(-1, 0.5), 4))
            if 'Right' in x:
                scale_R_r = round(scale[0]*(-1)+value_noise[i], 4)
                scale_L_r = round(scale[1]*(-1)+value_noise[i], 4)
                all_scale_R_r = [scale, [scale_R_r, scale_L_r]]
                cmds.setKeyframe('AimEye_R.translateX',
                                 at='tx', v=scale_R_r, t=time_scale)
                cmds.setKeyframe('AimEye_L.translateX',
                                 at='tx', v=scale_L_r, t=time_scale)
                print('R', all_scale_R_r)
                lst_scalegaze.append(all_scale_R_r)
            elif 'Right' not in x:
                scale_R_l = round(scale[0]+value_noise[i], 4)
                scale_L_l = round(scale[1]+value_noise[i], 4)
                all_scale_R_l = [scale, [scale_R_l, scale_L_l]]
                cmds.setKeyframe('AimEye_R.translateX',
                                 at='tx', v=scale_R_l, t=time_scale)
                cmds.setKeyframe('AimEye_L.translateX',
                                 at='tx', v=scale_L_l, t=time_scale)
                print('L', all_scale_R_l)
                lst_scalegaze.append(all_scale_R_l)

    return time_value, lst_namegaze, lst_scalegaze

# ------------------- set Position Of Gaze (Selected) -------------------


def setNinePositionOfGaze(checkBoxValue, radioSelected, textfieldAmount):
    amount = getAmountValue(textfieldAmount)
    radioSelected = action_checkRadioButton(radioSelected)
    value_noise = []
    lst_namegaze = []
    lst_scalegaze = []
    time_value = 0
    time_scale = 0
    all_scale_R_r = []
    all_scale_R_l = []

    # Set Normal Gaze
    for _ in range(amount):
        for x, scale in lst_Nine:
            time_value += 1
            cmds.playbackOptions(edit=True, maxTime=time_value)
            cmds.setKeyframe('ctrlEye_R.translateX', at='tx',
                             v=scale[0], t=time_value)
            cmds.setKeyframe('ctrlEye_R.translateY', at='ty',
                             v=scale[1], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateX', at='tx',
                             v=scale[0], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateY', at='ty',
                             v=scale[1], t=time_value)
    # Add value selected
    for i in range(amount):
        for x, scale in lst_Nine:
            # print(scale)
            lst_namegaze.append(x)
            time_scale += 1
            cmds.playbackOptions(edit=True, maxTime=time_value)
            value_noise.append(round(rand.uniform(-1, 0.5), 4))
            if 'Right' in x:
                scale_R_r = round(scale[0]*(-1)+value_noise[i], 4)
                scale_L_r = round(scale[1]*(-1)+value_noise[i], 4)
                all_scale_R_r = [scale, [scale_R_r, scale_L_r]]
                cmds.setKeyframe('AimEye_R.translateX',
                                 at='tx', v=scale_R_r, t=time_scale)
                cmds.setKeyframe('AimEye_L.translateX',
                                 at='tx', v=scale_L_r, t=time_scale)
                print('R', all_scale_R_r)
                lst_scalegaze.append(all_scale_R_r)
            elif 'Right' not in x:
                scale_R_l = round(scale[0]+value_noise[i], 4)
                scale_L_l = round(scale[1]+value_noise[i], 4)
                all_scale_R_l = [scale, [scale_R_l, scale_L_l]]
                cmds.setKeyframe('AimEye_R.translateX',
                                 at='tx', v=scale_R_l, t=time_scale)
                cmds.setKeyframe('AimEye_L.translateX',
                                 at='tx', v=scale_L_l, t=time_scale)
                print('L', all_scale_R_l)
                lst_scalegaze.append(all_scale_R_l)

    return time_value, lst_namegaze, lst_scalegaze


# ----------------- action_radioButton -----------------
lstcheckBox = ['checkBox_RSR', 'checkBox_RIO', 'checkBox_RLR', 'checkBox_RMR', 'checkBox_RIR', 'checkBox_RSO', 'checkBox_RSRIO', 'checkBox_RIRSO',
               'checkBox_LSR', 'checkBox_LIO', 'checkBox_LLR', 'checkBox_LMR', 'checkBox_LIR', 'checkBox_LSO', 'checkBox_LSRIO', 'checkBox_LIRSO']


def action_checkBox(checkBoxValue, radioSelected1, radioSelected2):
    if cmds.checkBox(checkBoxValue, query=True, value=True):
        for i, j in enumerate(lstcheckBox):
            if j == checkBoxValue:
                cmds.radioButton(radioSelected1, edit=True, enable=False)
                cmds.radioButton(radioSelected2, edit=True, enable=False)
    else:
        cmds.radioButton(radioSelected1, edit=True, enable=True)
        cmds.radioButton(radioSelected2, edit=True, enable=True)


lstSelectedAction = []
new_lstSelectedAction = []


def action_checkRadioButton(radioSelected):
    # chackbox values
    if cmds.radioButton(radioSelected, query=True, select=True):

        # print(radioSelected)
        for _, j in enumerate(lstActionOU):
            if j[0] == radioSelected:
                # print(lstActionOU[i][0])
                lstSelectedAction.append(j[0])
        # # print(lstSelectedAction)
        # for k in lstSelectedAction:
        #     # print(lstSelectedAction[k].index(lstSelectedAction[k][-3:]))
        #     s = k[-3:]
        #     index_ = lstSelectedAction.index(s)
        #     if lstSelectedAction[index_] not in new_lstSelectedAction:
        #         new_lstSelectedAction.append(lstSelectedAction[index_])
        # print(new_lstSelectedAction)
        #     # new_lstSelectedAction = list(
        #     #     dict.fromkeys(lstSelectedAction[k][-3:]))


if __name__ == "__main__":
    createUI('Ocular motility test images generating system')
