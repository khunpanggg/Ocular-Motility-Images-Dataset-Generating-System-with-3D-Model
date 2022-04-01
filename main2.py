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
    cmds.button(label='Set Gaze', command=setMovementGaze, bgc=[0.4, 0.4, 0.4])
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.button(label='Set Camera', command=setCamaraGaze, bgc=[0.4, 0.4, 0.4])
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.setParent('..')
    cmds.frameLayout(label='Tool', collapsable=True)
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
                        (1, 125), (2, 125)], columnOffset=[(1, 'both', 10)], bgc=[0.2, 0.2, 0.2])
    cmds.button(label='Bake Simulation', command=openFile, bgc=[0.4, 0.4, 0.4])
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')

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
    cmds.text('RSR', bgc=[0.1, 0.1, 0.1])
    cmds.text('LIO', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     displayLights='all', camera='faceCam2')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RSR
    RSR = cmds.checkBox('RSR', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('RSR', 'radioOver_RSR', 'radioUnder_RSR'))
    collectEyes_RSR = cmds.radioCollection('collectEyes_RSR')
    radioOver_RSR = cmds.radioButton(
        'radioOver_RSR', label='overaction', select=True)
    radioUnder_RSR = cmds.radioButton('radioUnder_RSR', label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LIO
    LIO = cmds.checkBox('LIO', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('LIO', 'radioOver_LIO', 'radioUnder_LIO'))
    collectEyes_LIO = cmds.radioCollection('collectEyes_LIO')
    radioOver_LIO = cmds.radioButton(
        'radioOver_LIO', label='overaction', select=True)
    radioUnder_LIO = cmds.radioButton('radioUnder_LIO', label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Up Gaze ------------------
    cmds.frameLayout(label='Up Gaze')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all', camera='faceCam3')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Left & Up Gaze ------------------
    cmds.frameLayout(label='Left & Up Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('RIO', bgc=[0.1, 0.1, 0.1])
    cmds.text('LSR', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all', camera='faceCam4')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RIO
    RIO = cmds.checkBox('RIO', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('RIO', 'radioOver_RIO', 'radioUnder_RIO'))
    collectEyes_RIO = cmds.radioCollection('collectEyes_RIO')
    radioOver_RIO = cmds.radioButton(
        'radioOver_RIO', label='overaction', select=True)
    radioUnder_RIO = cmds.radioButton('radioUnder_RIO', label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
                        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LSR
    LSR = cmds.checkBox('LSR', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('LSR', 'radioOver_LSR', 'radioUnder_LSR'))
    collectEyes_LSR = cmds.radioCollection('collectEyes_LSR')
    radioOver_LSR = cmds.radioButton(
        'radioOver_LSR', label='overaction', select=True)
    radioUnder_LSR = cmds.radioButton('radioUnder_LSR', label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Right Gaze ------------------
    cmds.frameLayout(label='Right Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('RLR', bgc=[0.1, 0.1, 0.1])
    cmds.text('LMR', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all', camera='faceCam5')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RLR
    RLR = cmds.checkBox('RLR', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('RLR', 'radioOver_RLR', 'radioUnder_RLR'))
    collectEyes_RLR = cmds.radioCollection('collectEyes_RLR')
    radioOver_RLR = cmds.radioButton(
        'radioOver_RLR', label='overaction', select=True)
    radioUnder_RLR = cmds.radioButton('radioUnder_RLR', label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LMR
    LMR = cmds.checkBox('LMR', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('LMR', 'radioOver_LMR', 'radioUnder_LMR'))
    collectEyes_LMR = cmds.radioCollection('collectEyes_LMR')
    radioOver_LMR = cmds.radioButton(
        'radioOver_LMR', label='overaction', select=True)
    radioUnder_LMR = cmds.radioButton('radioUnder_LMR', label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Primary Position ------------------
    cmds.frameLayout(label='Primary Position')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all', camera='faceCam6')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Left Gaze ------------------
    cmds.frameLayout(label='Left Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('RMR', bgc=[0.1, 0.1, 0.1])
    cmds.text('LLR', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all', camera='faceCam7')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RMR
    RMR = cmds.checkBox('RMR', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('RMR', 'radioOver_RMR', 'radioUnder_RMR'))
    collectEyes_RMR = cmds.radioCollection('collectEyes_RMR')
    radioOver_RMR = cmds.radioButton(
        'radioOver_RMR', label='overaction', select=True)
    radioUnder_RMR = cmds.radioButton('radioUnder_RMR', label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LLR
    LLR = cmds.checkBox('LLR', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('LLR', 'radioOver_LLR', 'radioUnder_LLR'))
    collectEyes_LLR = cmds.radioCollection('collectEyes_LLR')
    radioOver_LLR = cmds.radioButton(
        'radioOver_LLR', label='overaction', select=True)
    radioUnder_LLR = cmds.radioButton('radioUnder_LLR', label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Right & Down Gaze ------------------
    cmds.frameLayout(label='Right & Down Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('RIR', bgc=[0.1, 0.1, 0.1])
    cmds.text('LSO', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all', camera='faceCam8')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RIR
    RIR = cmds.checkBox('RIR', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('RIR', 'radioOver_RIR', 'radioUnder_RIR'))
    collectEyes_RIR = cmds.radioCollection('collectEyes_RIR')
    radioOver_RIR = cmds.radioButton(
        'radioOver_RIR', label='overaction', select=True)
    radioUnder_RIR = cmds.radioButton('radioUnder_RIR', label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LSO
    LSO = cmds.checkBox('LSO', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('LSO', 'radioOver_LSO', 'radioUnder_LSO'))
    collectEyes_LSO = cmds.radioCollection('collectEyes_LSO')
    radioOver_LSO = cmds.radioButton(
        'radioOver_LSO', label='overaction', select=True)
    radioUnder_LSO = cmds.radioButton('radioUnder_LSO', label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Down Gaze ------------------
    cmds.frameLayout(label='Up Gaze')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all', camera='faceCam9')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------------ Left & Down Gaze ------------------
    cmds.frameLayout(label='Left & Down Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('RSO', bgc=[0.1, 0.1, 0.1])
    cmds.text('LIR', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    cmds.paneLayout(configuration='quad', height=100)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all', camera='faceCam10')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # RSO
    RSO = cmds.checkBox('RSO', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('RSO', 'radioOver_RSO', 'radioUnder_RSO'))
    collectEyes_RSO = cmds.radioCollection('collectEyes_RSO')
    radioOver_RSO = cmds.radioButton(
        'radioOver_RSO', label='overaction', select=True)
    radioUnder_RSO = cmds.radioButton('radioUnder_RSO', label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LIR
    LIR = cmds.checkBox('LIR', label='normal', value=False,
                        changeCommand=lambda x: action_checkBox('LIR', 'radioOver_LIR', 'radioUnder_LIR'))
    collectEyes_LIR = cmds.radioCollection('collectEyes_LIR')
    radioOver_LIR = cmds.radioButton(
        'radioOver_LIR', label='overaction', select=True)
    radioUnder_LIR = cmds.radioButton('radioUnder_LIR', label='underaction')
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
    cmds.menuItem(label="Indoor")
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.setParent('..')
    cmds.setParent('..')

    # def setCamara(*args):
    #     setCamaraGaze()
    #     if cmds.window(window, exists=True):
    #         cmds.deleteUI(window)
    #     createUI('Ocular motility test images generating system')
    def applyButton(*args):
        # setNormalPositionOfGaze(AmoutImages)
        loadWindowPreview_Abnormal(
            setNinePositionOfGaze(AmoutImages), AmoutImages)

        # getValueNine = setNinePositionOfGaze(AmoutImages)
        # loadWindowPreview_Abnormal(
        #     getValueNine[0], getValueNine[1], getValueNine[2], AmoutImages)

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
    cmds.lookThru('faceCam1')
    cmds.lookThru(q=True)
    cmds.playblast(filename="C:/Users/Khunpang/Documents/maya/projects/Female Head/movies/female",
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


def loadWindowPreview(endframe, textfieldAmount):

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
        cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
                            (1, 250), (2, 250), (3, 250)])

        # print(scaleGaze[i], scaleGaze[num])
        cmds.picture(image=(
            'C:/Users/Khunpang/Documents/maya/projects/Female Head/movies/female.%04d.jpg' % (i+1)))
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
    cmds.text('total 9 diagnostic positions of gaze : %d ' % (amount))
    cmds.text('total picture : %d ' % (amount*9))
    cmds.separator(height=5, style=None)
    cmds.separator(height=5, style=None)
    cmds.button(label='Render', height=30)
    cmds.button(label='Back', command=cancelCallback)
    cmds.setParent("..")
    cmds.setParent("..")
    cmds.formLayout(form, edit=True, attachForm=[(sl, 'top', 5), (sl, 'right', 5), (sl, 'left', 5), (
        sl, 'top', 5), (sl, 'bottom', 60), (rc, 'bottom', 5), (rc, 'left', 5), (rc, 'right', 5)])

    cmds.showWindow(window)


def loadWindowPreview_Abnormal(endframe, amount):
    playblastPreview()
    loadWindowPreview(endframe, amount)

# ------------------- getAmountValue -------------------


def getAmountValue(textfieldAmount):
    currentAmount = cmds.textField(textfieldAmount, query=True, text=True)
    # print('Amount'+currentAmount)
    return int(currentAmount)


lst_Nine = [('Right Up', [-0.8, 0.5]), ('Up gaze', [0, 0.8]), ('Left Up', [0.8, 0.5]),
            ('Right', [-1, 0]), ('Primary', [0, 0]), ('Left', [1, 0]),
            ('Right Down', [-1, -1]), ('Downgaze', [0, -0.8]), ('Left Down', [1, -1])]

lstCollectEyes = [
    'collectEyes_RSR',
    'collectEyes_LIO',

    'collectEyes_RIO',
    'collectEyes_LSR',

    'collectEyes_RLR',
    'collectEyes_LMR',

    'collectEyes_RMR',
    'collectEyes_LLR',

    'collectEyes_RIR',
    'collectEyes_LSO',

    'collectEyes_RSO',
    'collectEyes_LIR'
]

# ----------------- action_checkBox -----------------
lstcheckBox = ['RSR', 'LIO', 'RIO', 'LSR', 'RLR', 'LMR',
               'RMR', 'LLR', 'RIR', 'LSO', 'RSO', 'LIR']


def action_checkBox(checkBoxValue, radioSelected1, radioSelected2):
    if cmds.checkBox(checkBoxValue, query=True, value=True):
        for _, j in enumerate(lstcheckBox):
            if j == checkBoxValue:
                cmds.radioButton(radioSelected1, edit=True, enable=False)
                cmds.radioButton(radioSelected2, edit=True, enable=False)
    else:
        cmds.radioButton(radioSelected1, edit=True, enable=True)
        cmds.radioButton(radioSelected2, edit=True, enable=True)


# ----------------- action_radioButton -----------------
lstcheckNormal = []
lstcheckDisorder = []


def passValue(DirectionControl, *args):
    for j in lstcheckBox:
        checkboxVal = cmds.checkBox(j, query=True, value=True)
        # print(j, checkbox)
        if checkboxVal == True:
            lstcheckNormal.append(j)
        else:
            lstcheckDisorder.append(j)
    print('Normal', lstcheckNormal)
    print('Disorder', lstcheckDisorder)

    for i in range(len(DirectionControl)):
        for j in lstcheckDisorder:
            if j in DirectionControl[i]:
                print(DirectionControl[i])
                radioCol = cmds.radioCollection(
                    DirectionControl[i], query=True, sl=True)
                print(radioCol)
    return radioCol

# ------------------- setMovementGaze Preview -------------------


def setMovementGaze(self):
    time_value = 0

    for name, gaze in lst_Nine:
        time_value += 1
        cmds.playbackOptions(edit=True, minTime='1', maxTime=time_value)
        cmds.setKeyframe('ctrlEye_R.translateX', at='tx',
                         v=gaze[0], t=time_value)
        cmds.setKeyframe('ctrlEye_R.translateY', at='ty',
                         v=gaze[1], t=time_value)
        cmds.setKeyframe('ctrlEye_L.translateX', at='tx',
                         v=gaze[0], t=time_value)
        cmds.setKeyframe('ctrlEye_L.translateY', at='ty',
                         v=gaze[1], t=time_value)
        if 'Up' in name:
            cmds.setKeyframe('upperLidBase_R.translateY', at='ty',
                             v=0.4, t=time_value)
            cmds.setKeyframe('upperLidBase_L.translateY', at='ty',
                             v=0.4, t=time_value)
            cmds.setKeyframe('EyeBrowRegion_R.translateY', at='ty',
                             v=0.4, t=time_value)
            cmds.setKeyframe('EyeBrowRegion_L.translateY', at='ty',
                             v=0.4, t=time_value)
            cmds.setKeyframe('lowerLid_R.translateY', at='ty',
                             v=-0.2, t=time_value)
            cmds.setKeyframe('lowerLid_L.translateY', at='ty',
                             v=-0.2, t=time_value)
        elif 'Down' in name:
            cmds.setKeyframe('upperLid_R.translateY', at='ty',
                             v=0.6, t=time_value)
            cmds.setKeyframe('upperLid_L.translateY', at='ty',
                             v=0.6, t=time_value)
            cmds.setKeyframe('lowerLid_R.translateY', at='ty',
                             v=0.7, t=time_value)
            cmds.setKeyframe('lowerLid_L.translateY', at='ty',
                             v=0.7, t=time_value)
        else:
            cmds.setKeyframe('upperLidBase_R.translateY', at='ty',
                             v=0, t=time_value)
            cmds.setKeyframe('upperLidBase_L.translateY', at='ty',
                             v=0, t=time_value)
            cmds.setKeyframe('EyeBrowRegion_R.translateY', at='ty',
                             v=0, t=time_value)
            cmds.setKeyframe('EyeBrowRegion_L.translateY', at='ty',
                             v=0, t=time_value)
            cmds.setKeyframe('upperLid_R.translateY', at='ty',
                             v=0, t=time_value)
            cmds.setKeyframe('upperLid_L.translateY', at='ty',
                             v=0, t=time_value)
            cmds.setKeyframe('lowerLid_R.translateY', at='ty',
                             v=0, t=time_value)
            cmds.setKeyframe('lowerLid_L.translateY', at='ty',
                             v=0, t=time_value)
    # set model
    for i in range(time_value):
        no = ""
        cmds.currentTime(i+1)
        cmds.select('Geometry'+no)
        cmds.duplicate('Geometry'+no)
        cmds.move(100*(i+1), 0, 0)
        no = str(i)
    print(time_value)


def setCamaraGaze(self):
    # Create a camera
    cmds.camera(name='faceCam1', focalLength=70)
    cmds.group('faceCam1', n='groupfaceCam1')
    cmds.parent('groupfaceCam1', 'AimEye_M')
    cmds.setAttr('groupfaceCam1.translate', 0, 0, 0)
    cmds.parent('groupfaceCam1', world=True)
    cmds.parent('faceCam1', 'AimEye_M')
    # Move camera
    for i in range(1, 10, 1):
        cmds.select('faceCam'+str(i))
        cmds.duplicate('faceCam'+str(i))
        cmds.move(100*(i), 0, 0, moveX=True)

# ------------------- set Position Of Gaze (NORMAL) -------------------


def setNormalPositionOfGaze(textfieldAmount):
    amount = getAmountValue(textfieldAmount)
    value_noise = []
    time_value = 0
    for i in range(amount):
        for name, gaze in lst_Nine:
            time_value += 1
            cmds.playbackOptions(edit=True, minTime='1', maxTime=time_value)
            cmds.setKeyframe('ctrlEye_R.translateX', at='tx',
                             v=gaze[0], t=time_value)
            cmds.setKeyframe('ctrlEye_R.translateY', at='ty',
                             v=gaze[1], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateX', at='tx',
                             v=gaze[0], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateY', at='ty',
                             v=gaze[1], t=time_value)
            if 'Up' in name:
                cmds.setKeyframe('upperLid_R.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('upperLid_L.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('upperLidBase_R.translateY', at='ty',
                                 v=0.4, t=time_value)
                cmds.setKeyframe('upperLidBase_L.translateY', at='ty',
                                 v=0.4, t=time_value)
                cmds.setKeyframe('EyeBrowRegion_R.translateY', at='ty',
                                 v=0.4, t=time_value)
                cmds.setKeyframe('EyeBrowRegion_L.translateY', at='ty',
                                 v=0.4, t=time_value)
                cmds.setKeyframe('lowerLid_R.translateY', at='ty',
                                 v=-0.2, t=time_value)
                cmds.setKeyframe('lowerLid_L.translateY', at='ty',
                                 v=-0.2, t=time_value)
            elif 'Down' in name:
                cmds.setKeyframe('upperLid_R.translateY', at='ty',
                                 v=0.6, t=time_value)
                cmds.setKeyframe('upperLid_L.translateY', at='ty',
                                 v=0.6, t=time_value)
                cmds.setKeyframe('lowerLid_R.translateY', at='ty',
                                 v=0.7, t=time_value)
                cmds.setKeyframe('lowerLid_L.translateY', at='ty',
                                 v=0.7, t=time_value)
            else:
                cmds.setKeyframe('upperLidBase_R.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('upperLidBase_L.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('EyeBrowRegion_R.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('EyeBrowRegion_L.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('upperLid_R.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('upperLid_L.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('lowerLid_R.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('lowerLid_L.translateY', at='ty',
                                 v=0, t=time_value)

            value_noise.append(round(rand.uniform(0, 1), 4))

            cmds.setKeyframe('AimEye_R.translateX', at='tx',
                             v=value_noise[i], t=time_value)
            cmds.setKeyframe('AimEye_L.translateX', at='ty',
                             v=value_noise[i], t=time_value)


# ------------------- set Position Of Gaze (Selected) -------------------
lstActionOU = [
    # OVER ACTION
    ('radioOver_RSR', [[-1, 5], [1, 5]]),
    ('radioOver_LIO', [[-2, 0], [0, 2]]),
    ('radioOver_RLR', [[-5, 0], [0, 0]]),
    ('radioOver_LMR', [[-5, 0], [0, 0]]),
    ('radioOver_RIR', [[-2, 0], [-2, 0]]),
    ('radioOver_LSO', [[-2, 0], [-2, 0]]),

    ('radioOver_RIO', [[0, 2], [0, 2]]),
    ('radioOver_LSR', [[0, 2], [0, 2]]),
    ('radioOver_RMR', [[0, 5], [0, 0]]),
    ('radioOver_LLR', [[0, 5], [0, 0]]),
    ('radioOver_RSO', [[0, 2], [-2, 0]]),
    ('radioOver_LIR', [[0, 2], [-2, 0]]),

    # UNDER ACTION
    ('radioUnder_RSR', [[0, 2], [0, -2]]),
    ('radioUnder_LIO', [[0, 2], [-2, 0]]),
    ('radioUnder_RLR', [[0, 5], [0, 0]]),
    ('radioUnder_LMR', [[0, 5], [0, 0]]),
    ('radioUnder_RIR', [[0, 5], [0, 5]]),
    ('radioUnder_LSO', [[0, 5], [0, 5]]),

    ('radioUnder_RIO', [[-1, 0], [-4, 0]]),
    ('radioUnder_LSR', [[-4, 0], [-4, 0]]),
    ('radioUnder_RMR', [[-5, 0], [0, 0]]),
    ('radioUnder_LLR', [[-5, 0], [0, 0]]),
    ('radioUnder_RSO', [[-5, 0], [0, 5]]),
    ('radioUnder_LIR', [[-5, 0], [0, 5]])
]


def setNinePositionOfGaze(textfieldAmount):

    amount = getAmountValue(textfieldAmount)
    radioCol = passValue(lstCollectEyes)

    value_noise = []
    time_value = 0

    x_value_lst = []
    y_value_lst = []
    # Set Normal Gaze
    for i in range(amount):
        for name, gaze in lst_Nine:
            time_value += 1
            cmds.playbackOptions(edit=True, maxTime=time_value)
            cmds.setKeyframe('ctrlEye_R.translateX', at='tx',
                             v=gaze[0], t=time_value)
            cmds.setKeyframe('ctrlEye_R.translateY', at='ty',
                             v=gaze[1], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateX', at='tx',
                             v=gaze[0], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateY', at='ty',
                             v=gaze[1], t=time_value)
            if 'Up' in name:
                cmds.setKeyframe('upperLid_R.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('upperLid_L.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('upperLidBase_R.translateY', at='ty',
                                 v=0.4, t=time_value)
                cmds.setKeyframe('upperLidBase_L.translateY', at='ty',
                                 v=0.4, t=time_value)
                cmds.setKeyframe('EyeBrowRegion_R.translateY', at='ty',
                                 v=0.4, t=time_value)
                cmds.setKeyframe('EyeBrowRegion_L.translateY', at='ty',
                                 v=0.4, t=time_value)
                cmds.setKeyframe('lowerLid_R.translateY', at='ty',
                                 v=-0.2, t=time_value)
                cmds.setKeyframe('lowerLid_L.translateY', at='ty',
                                 v=-0.2, t=time_value)
            elif 'Down' in name:
                cmds.setKeyframe('upperLid_R.translateY', at='ty',
                                 v=0.6, t=time_value)
                cmds.setKeyframe('upperLid_L.translateY', at='ty',
                                 v=0.6, t=time_value)
                cmds.setKeyframe('lowerLid_R.translateY', at='ty',
                                 v=0.7, t=time_value)
                cmds.setKeyframe('lowerLid_L.translateY', at='ty',
                                 v=0.7, t=time_value)
            else:
                cmds.setKeyframe('upperLidBase_R.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('upperLidBase_L.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('EyeBrowRegion_R.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('EyeBrowRegion_L.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('upperLid_R.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('upperLid_L.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('lowerLid_R.translateY', at='ty',
                                 v=0, t=time_value)
                cmds.setKeyframe('lowerLid_L.translateY', at='ty',
                                 v=0, t=time_value)

            # Add value selected
            for name_OU, scale in lstActionOU:
                if radioCol in name_OU:
                    print('user selected', name_OU, scale)
                    value_noise.append(round(rand.uniform(0, 0.6), 4))

                    for x_value in range(scale[0][0], scale[0][1]):
                        x_value_lst.append(x_value)
                    for y_value in range(scale[1][0], scale[1][1]):
                        y_value_lst.append(y_value)

                    if 'R' == name_OU[-3:][0]:
                        # print(x[-3:][0])
                        cmds.setKeyframe('AimEye_R.translateX',
                                         at='tx', v=x_value_lst[i]+value_noise[i], t=time_value)
                        cmds.setKeyframe('AimEye_R.translateY',
                                         at='ty', v=y_value_lst[i]+value_noise[i], t=time_value)

                    elif 'L' == name_OU[-3:][0]:
                        cmds.setKeyframe('AimEye_L.translateX',
                                         at='tx', v=x_value_lst[i]+value_noise[i], t=time_value)
                        cmds.setKeyframe('AimEye_L.translateY',
                                         at='ty', v=y_value_lst[i]+value_noise[i], t=time_value)
                        # print(name_OU[-3:][0])

    return time_value

# def bakeSimulation():
#     cmds.select( 'Head_M', visible=True )
#     cmds.select("Geometry", hierarchy=True)


if __name__ == "__main__":
    createUI('Ocular motility test images generating system')
