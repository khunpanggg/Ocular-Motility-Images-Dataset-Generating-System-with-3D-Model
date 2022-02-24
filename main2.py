import maya.cmds as cmds


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
    cmds.button(label='Blend Shape', command=openFile, bgc=[0.4, 0.4, 0.4])
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.button(label='Set Gaze', command=openFile, bgc=[0.4, 0.4, 0.4])
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
        (1, 300), (2, 300), (3, 300)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])

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
                                 changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    collectEyes_RSR = cmds.radioCollection()
    radioOver_RSR = cmds.radioButton('radioOver_RSR', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    radioUnder_RSR = cmds.radioButton('radioUnder_RSR', label='underaction', changeCommand=lambda x: action_checkBox_Right(
        checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LIO
    checkBox_LIO = cmds.checkBox('checkBox_LIO', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    collectEyes_LIO = cmds.radioCollection()
    radioOver_LIO = cmds.radioButton('radioOver_LIO', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    radioUnder_LIO = cmds.radioButton('radioUnder_LIO', label='underaction',
                                      changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
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
                                   changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    collectEyes_RSRIO = cmds.radioCollection()
    radioOver_RSRIO = cmds.radioButton('radioOver_RSRIO', label='overaction', select=True,
                                       changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    radioUnder_RSRIO = cmds.radioButton('radioUnder_RSRIO', label='underaction', changeCommand=lambda x: action_checkBox_Right(
        checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LIO
    checkBox_LSRIO = cmds.checkBox('checkBox_LSRIO', label='normal', value=False,
                                   changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    collectEyes_LSRIO = cmds.radioCollection()
    radioOver_LSRIO = cmds.radioButton('radioOver_LSRIO', label='overaction', select=True,
                                       changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    radioUnder_LSRIO = cmds.radioButton('radioUnder_LSRIO', label='underaction',
                                        changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
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
                                 changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    collectEyes_RIO = cmds.radioCollection()
    radioOver_RIO = cmds.radioButton('radioOver_RIO', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    radioUnder_RIO = cmds.radioButton('radioUnder_RIO', label='underaction', changeCommand=lambda x: action_checkBox_Right(
        checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LSR
    checkBox_LSR = cmds.checkBox('checkBox_LSR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    collectEyes_LSR = cmds.radioCollection()
    radioOver_LSR = cmds.radioButton('radioOver_LSR', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    radioUnder_LSR = cmds.radioButton('radioUnder_LSR', label='underaction',
                                      changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
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
                                 changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    collectEyes_RLR = cmds.radioCollection()
    radioOver_RLR = cmds.radioButton('radioOver_RLR', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    radioUnder_RLR = cmds.radioButton('radioUnder_RLR', label='underaction', changeCommand=lambda x: action_checkBox_Right(
        checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LMR
    checkBox_LMR = cmds.checkBox('checkBox_LMR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    collectEyes_LMR = cmds.radioCollection()
    radioOver_LMR = cmds.radioButton('radioOver_LMR', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    radioUnder_LMR = cmds.radioButton('radioUnder_LMR', label='underaction',
                                      changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
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
                                 changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    collectEyes_RMR = cmds.radioCollection()
    radioOver_RMR = cmds.radioButton('radioOver_RMR', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    radioUnder_RMR = cmds.radioButton('radioUnder_RMR', label='underaction', changeCommand=lambda x: action_checkBox_Right(
        checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LLR
    checkBox_LLR = cmds.checkBox('checkBox_LLR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    collectEyes_LLR = cmds.radioCollection()
    radioOver_LLR = cmds.radioButton('radioOver_LLR', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    radioUnder_LLR = cmds.radioButton('radioUnder_LLR', label='underaction',
                                      changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
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
                                 changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    collectEyes_RIR = cmds.radioCollection()
    radioOver_RIR = cmds.radioButton('radioOver_RIR', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    radioUnder_RIR = cmds.radioButton('radioUnder_RIR', label='underaction', changeCommand=lambda x: action_checkBox_Right(
        checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LSO
    checkBox_LSO = cmds.checkBox('checkBox_LSO', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    collectEyes_LSO = cmds.radioCollection()
    radioOver_LSO = cmds.radioButton('radioOver_LSO', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    radioUnder_LSO = cmds.radioButton('radioUnder_LSO', label='underaction',
                                      changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
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
                                   changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    collectEyes_RIRSO = cmds.radioCollection()
    radioOver_RIRSO = cmds.radioButton('radioOver_RIRSO', label='overaction', select=True,
                                       changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    radioUnder_RIRSO = cmds.radioButton('radioUnder_RIRSO', label='underaction', changeCommand=lambda x: action_checkBox_Right(
        checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LSO
    checkBox_LIRSO = cmds.checkBox('checkBox_LSO', label='normal', value=False,
                                   changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    collectEyes_LIRSO = cmds.radioCollection()
    radioOver_LIRSO = cmds.radioButton('radioOver_LIRSO', label='overaction', select=True,
                                       changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    radioUnder_LIRSO = cmds.radioButton('radioUnder_LIRSO', label='underaction',
                                        changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
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
                                 changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    collectEyes_RSO = cmds.radioCollection()
    radioOver_RSO = cmds.radioButton('radioOver_RSO', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO))
    radioUnder_RSO = cmds.radioButton('radioUnder_RSO', label='underaction', changeCommand=lambda x: action_checkBox_Right(
        checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO))
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LIR
    checkBox_LIR = cmds.checkBox('checkBox_LIR', label='normal', value=False,
                                 changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    collectEyes_LIR = cmds.radioCollection()
    radioOver_LIR = cmds.radioButton('radioOver_LIR', label='overaction', select=True,
                                     changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
    radioUnder_LIR = cmds.radioButton('radioUnder_LIR', label='underaction',
                                      changeCommand=lambda x: action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO))
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

    def cancelCallback(*args):
        if cmds.window(window, exists=True):
            cmds.deleteUI(window)

    def applyButton(*args):
        loadWindowPreview()

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


def loadWindowPreview():

    def cancelCallback(*args):
        if cmds.window(window, exists=True):
            cmds.deleteUI(window)

    # create new window
    window = cmds.window(title='9 Diagnostic Positions of Gaze Preview',
                         resizeToFitChildren=True, sizeable=True)

    form = cmds.formLayout()
    sl = cmds.scrollLayout(childResizable=True)
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 250), (2, 250), (3, 250)], columnOffset=[(1, 'both', 2), (2, 'both', 3), (3, 'both', 3)])

    # mock up images
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_1.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/mermaid_model_up_gaze.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_7.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_17.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/mermaid_model_primary.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_19.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_25.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/mermaid_model_down_gaze.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_36.jpg'))
    cmds.separator(height=10, style=None)
    cmds.separator(height=10, style=None)
    cmds.separator(height=10, style=None)
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_1.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/mermaid_model_up_gaze.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_7.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_17.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/mermaid_model_primary.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_19.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_25.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/mermaid_model_down_gaze.jpg'))
    cmds.picture(image=(
        'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_36.jpg'))

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

# ----------------- set Position Of Gaze (ABNORMAL) -----------------

# ----------------- action_radioButton -----------------


def action_checkBox_Right(checkBox_RSR, checkBox_RIO, checkBox_RLR, checkBox_RMR, checkBox_RIR, checkBox_RSO, checkBox_RSRIO, checkBox_RIRSO):
    # chackbox values
    if cmds.checkBox(checkBox_RSR, query=True, value=True):
        cmds.radioButton('radioOver_RSR', edit=True, enable=False)
        cmds.radioButton('radioUnder_RSR', edit=True, enable=False)
        print("checkBox_RSR")

    if cmds.checkBox(checkBox_RIO, query=True, value=True):
        cmds.radioButton('radioOver_RIO', edit=True, enable=False)
        cmds.radioButton('radioUnder_RIO', edit=True, enable=False)
        print("checkBox_RIO")
    if cmds.checkBox(checkBox_RLR, query=True, value=True):
        cmds.radioButton('radioOver_RLR', edit=True, enable=False)
        cmds.radioButton('radioUnder_RLR', edit=True, enable=False)
        print("checkBox_RLR")
    if cmds.checkBox(checkBox_RMR, query=True, value=True):
        cmds.radioButton('radioOver_RMR', edit=True, enable=False)
        cmds.radioButton('radioUnder_RMR', edit=True, enable=False)
        print("checkBox_RMR")
    if cmds.checkBox(checkBox_RIR, query=True, value=True):
        cmds.radioButton('radioOver_RIR', edit=True, enable=False)
        cmds.radioButton('radioUnder_RIR', edit=True, enable=False)
        print("checkBox_RIR")
    if cmds.checkBox(checkBox_RSO, query=True, value=True):
        cmds.radioButton('radioOver_RSO', edit=True, enable=False)
        cmds.radioButton('radioUnder_RSO', edit=True, enable=False)
        print("checkBox_RSO")
    if cmds.checkBox(checkBox_RSRIO, query=True, value=True):
        cmds.radioButton('radioOver_RSRIO', edit=True, enable=False)
        cmds.radioButton('radioUnder_RSRIO', edit=True, enable=False)
        print("checkBox_RSRIO")
    if cmds.checkBox(checkBox_RIRSO, query=True, value=True):
        cmds.radioButton('radioOver_RIRSO', edit=True, enable=False)
        cmds.radioButton('radioUnder_RIRSO', edit=True, enable=False)
        print("checkBox_RIRSO")


def action_checkBox_Left(checkBox_LSR, checkBox_LIO, checkBox_LLR, checkBox_LMR, checkBox_LIR, checkBox_LSO, checkBox_LSRIO, checkBox_LIRSO):
    # chackbox values
    if cmds.checkBox(checkBox_LSR, query=True, value=True):
        cmds.radioButton('radioOver_LSR', edit=True, enable=False)
        cmds.radioButton('radioUnder_LSR', edit=True, enable=False)
        print("checkBox_LSR")
    if cmds.checkBox(checkBox_LIO, query=True, value=True):
        cmds.radioButton('radioOver_LIO', edit=True, enable=False)
        cmds.radioButton('radioUnder_LIO', edit=True, enable=False)
        print("checkBox_LIO")
    if cmds.checkBox(checkBox_LLR, query=True, value=True):
        cmds.radioButton('radioOver_LLR', edit=True, enable=False)
        cmds.radioButton('radioUnder_LLR', edit=True, enable=False)
        print("checkBox_LLR")
    if cmds.checkBox(checkBox_LMR, query=True, value=True):
        cmds.radioButton('radioOver_LMR', edit=True, enable=False)
        cmds.radioButton('radioUnder_LMR', edit=True, enable=False)
        print("checkBox_LMR")
    if cmds.checkBox(checkBox_LIR, query=True, value=True):
        cmds.radioButton('radioOver_LIR', edit=True, enable=False)
        cmds.radioButton('radioUnder_LIR', edit=True, enable=False)
        print("checkBox_LIR")
    if cmds.checkBox(checkBox_LSO, query=True, value=True):
        cmds.radioButton('radioOver_LSO', edit=True, enable=False)
        cmds.radioButton('radioUnder_LSO', edit=True, enable=False)
        print("checkBox_LSO")
    if cmds.checkBox(checkBox_LSRIO, query=True, value=True):
        cmds.radioButton('radioOver_LSRIO', edit=True, enable=False)
        cmds.radioButton('radioUnder_LSRIO', edit=True, enable=False)
        print("checkBox_LSRIO")
    if cmds.checkBox(checkBox_LIRSO, query=True, value=True):
        cmds.radioButton('radioOver_LIRSO', edit=True, enable=False)
        cmds.radioButton('radioUnder_LIRSO', edit=True, enable=False)
        print("checkBox_LIRSO")


if __name__ == "__main__":
    createUI('Ocular motility test images generating system')
