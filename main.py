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
    RSR = cmds.checkBox('RSR', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('RSR', 'radioOver_RSR_R', 'radioUnder_RSR_R'))
    collectEyes_RSR = cmds.radioCollection('collectEyes_RSR')
    radioOver_RSR = cmds.radioButton(
        'radioOver_RSR_R', label='overaction', enable=False)
    radioUnder_RSR = cmds.radioButton(
        'radioUnder_RSR_R', label='underaction', enable=False)
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LIO
    LIO = cmds.checkBox('LIO', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('LIO', 'radioOver_LIO_R', 'radioUnder_LIO_R'))
    collectEyes_LIO = cmds.radioCollection('collectEyes_LIO')
    radioOver_LIO = cmds.radioButton(
        'radioOver_LIO_R', label='overaction', enable=False)
    radioUnder_LIO = cmds.radioButton(
        'radioUnder_LIO_R', label='underaction', enable=False)
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
    RIO = cmds.checkBox('RIO', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('RIO', 'radioOver_RIO_L', 'radioUnder_RIO_L'))
    collectEyes_RIO = cmds.radioCollection('collectEyes_RIO')
    radioOver_RIO = cmds.radioButton(
        'radioOver_RIO_L', label='overaction', enable=False)
    radioUnder_RIO = cmds.radioButton(
        'radioUnder_RIO_L', label='underaction', enable=False)
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
                        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LSR
    LSR = cmds.checkBox('LSR', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('LSR', 'radioOver_LSR_L', 'radioUnder_LSR_L'))
    collectEyes_LSR = cmds.radioCollection('collectEyes_LSR')
    radioOver_LSR = cmds.radioButton(
        'radioOver_LSR_L', label='overaction', enable=False)
    radioUnder_LSR = cmds.radioButton(
        'radioUnder_LSR_L', label='underaction', enable=False)
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
    RLR = cmds.checkBox('RLR', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('RLR', 'radioOver_RLR_R', 'radioUnder_RLR_R'))
    collectEyes_RLR = cmds.radioCollection('collectEyes_RLR')
    radioOver_RLR = cmds.radioButton(
        'radioOver_RLR_R', label='overaction', enable=False)
    radioUnder_RLR = cmds.radioButton(
        'radioUnder_RLR_R', label='underaction', enable=False)
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LMR
    LMR = cmds.checkBox('LMR', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('LMR', 'radioOver_LMR_R', 'radioUnder_LMR_R'))
    collectEyes_LMR = cmds.radioCollection('collectEyes_LMR')
    radioOver_LMR = cmds.radioButton(
        'radioOver_LMR_R', label='overaction', enable=False)
    radioUnder_LMR = cmds.radioButton(
        'radioUnder_LMR_R', label='underaction', enable=False)
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
    RMR = cmds.checkBox('RMR', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('RMR', 'radioOver_RMR_L', 'radioUnder_RMR_L'))
    collectEyes_RMR = cmds.radioCollection('collectEyes_RMR')
    radioOver_RMR = cmds.radioButton(
        'radioOver_RMR_L', label='overaction', enable=False)
    radioUnder_RMR = cmds.radioButton(
        'radioUnder_RMR_L', label='underaction', enable=False)
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LLR
    LLR = cmds.checkBox('LLR', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('LLR', 'radioOver_LLR_L', 'radioUnder_LLR_L'))
    collectEyes_LLR = cmds.radioCollection('collectEyes_LLR')
    radioOver_LLR = cmds.radioButton(
        'radioOver_LLR_L', label='overaction', enable=False)
    radioUnder_LLR = cmds.radioButton(
        'radioUnder_LLR_L', label='underaction', enable=False)
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
    RIR = cmds.checkBox('RIR', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('RIR', 'radioOver_RIR_R', 'radioUnder_RIR_R'))
    collectEyes_RIR = cmds.radioCollection('collectEyes_RIR')
    radioOver_RIR = cmds.radioButton(
        'radioOver_RIR_R', label='overaction', enable=False)
    radioUnder_RIR = cmds.radioButton(
        'radioUnder_RIR_R', label='underaction', enable=False)
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LSO
    LSO = cmds.checkBox('LSO', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('LSO', 'radioOver_LSO_R', 'radioUnder_LSO_R'))
    collectEyes_LSO = cmds.radioCollection('collectEyes_LSO')
    radioOver_LSO = cmds.radioButton(
        'radioOver_LSO_R', label='overaction', enable=False)
    radioUnder_LSO = cmds.radioButton(
        'radioUnder_LSO_R', label='underaction', enable=False)
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
    RSO = cmds.checkBox('RSO', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('RSO', 'radioOver_RSO_L', 'radioUnder_RSO_L'))
    collectEyes_RSO = cmds.radioCollection('collectEyes_RSO')
    radioOver_RSO = cmds.radioButton(
        'radioOver_RSO_L', label='overaction', enable=False)
    radioUnder_RSO = cmds.radioButton(
        'radioUnder_RSO_L', label='underaction', enable=False)
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    # LIR
    LIR = cmds.checkBox('LIR', label='normal', value=True,
                        changeCommand=lambda x: action_checkBox('LIR', 'radioOver_LIR_L', 'radioUnder_LIR_L'))
    collectEyes_LIR = cmds.radioCollection('collectEyes_LIR')
    radioOver_LIR_L = cmds.radioButton(
        'radioOver_LIR_L', label='overaction', enable=False)
    radioUnder_LIR_L = cmds.radioButton(
        'radioUnder_LIR_L', label='underaction', enable=False)
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

    def applyButton(*args):
        count_checked = 0
        for i in lstcheckBox:
            if cmds.checkBox(i, query=True, value=True):
                count_checked += 1
                if count_checked == len(lstcheckBox):
                    print('normal eyes')
                    loadWindowPreview(setNormalNinePositionOfGaze(AmoutImages), AmoutImages)
            else:
                print('abnormal eyes')
                loadWindowPreview(setAbNinePositionOfGaze(
                    AmoutImages), AmoutImages)

    def renderButton(*args):
        # normal selected
        setNormalNinePositionOfGaze(AmoutImages)

    def cancelCallback(*args):
        if cmds.window(window, exists=True):
            cmds.deleteUI(window)

    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 300), (2, 300), (3, 300)], columnOffset=[(1, 'both', 3), (2, 'both', 3), (3, 'both', 3)])
    cmds.button(label='Apply', height=30, command=applyButton)
    cmds.button(label='Render', command=renderButton)
    cmds.button(label='Close', command=cancelCallback)
    cmds.setParent('..')
    cmds.showWindow()

# ------------------ openFile ------------------


def openFile(self):
    filename = cmds.fileDialog2(fileMode=1, caption="Import File")
    cmds.file(filename[0], i=True)

# ------------------ loadWindowPreview ------------------


def playblastPreview(*args):
    cmds.lookThru('faceCam1')
    cmds.lookThru(q=True)
    cmds.playblast(filename="C:/Users/Khunpang/Documents/maya/projects/children-girl/movies/boy",
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


def WindowPreview(endframe, textfieldAmount):

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
    pack = 0
    for i in range(endframe):
        cmds.rowColumnLayout(numberOfColumns=4, columnWidth=[
                            (1, 250), (2, 250), (3, 250), (4, 250)])
        cmds.picture(image=(
            'C:/Users/Khunpang/Documents/maya/projects/children-girl/movies/boy.%04d.jpg' % (i+1)))
        count += 1
        if count == 9:
            cmds.separator(height=20, style=None)
            cmds.separator(height=20, style=None)
            cmds.separator(height=20, style=None)
            count = 0
            pack += 1
        cmds.text('No. %d' % pack, font="boldLabelFont", align='center')
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


def loadWindowPreview(endframe, amount):
    playblastPreview()
    WindowPreview(endframe, amount)

# ------------------- getAmountValue -------------------

def getAmountValue(textfieldAmount):
    currentAmount = cmds.textField(textfieldAmount, query=True, text=True)
    # print('Amount'+currentAmount)
    return int(currentAmount)


lst_Nine = [('Right Up', [-0.8, 0.5]), ('Upgaze middle', [0, 0.8]), ('Left Up', [0.8, 0.5]),
            ('Right', [-1, 0]), ('Primary middle', [0, 0]), ('Left', [1, 0]),
            ('Right Down', [-1, -1]), ('Downgaze middle', [0, -0.8]), ('Left Down', [1, -1])]

lstCollectEyes = ['collectEyes_RSR', 'collectEyes_LIO', 'collectEyes_RIO', 'collectEyes_LSR', 'collectEyes_RLR', 'collectEyes_LMR',
                  'collectEyes_RMR', 'collectEyes_LLR', 'collectEyes_RIR', 'collectEyes_LSO', 'collectEyes_RSO', 'collectEyes_LIR']

# ----------------- action_checkBox -----------------
lstcheckBox = ['RSR', 'LIO', 'RIO', 'LSR', 'RLR', 'LMR',
               'RMR', 'LLR', 'RIR', 'LSO', 'RSO', 'LIR']


def action_checkBox(checkBoxValue, radioSelected1, radioSelected2):
    if cmds.checkBox(checkBoxValue, query=True, value=True):
        for _, j in enumerate(lstcheckBox):
            if j == checkBoxValue:
                cmds.radioButton(radioSelected1, edit=True, enable=False)
                cmds.radioButton(radioSelected2, edit=True, enable=False)
                numcheckbox += 1
    else:
        if checkBoxValue[2] == 'R':
            cmds.radioButton(radioSelected1, edit=True, enable=False)
            cmds.radioButton(radioSelected2, edit=True, enable=True)
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


# ----------------- movefaceMuscle -----------------

def movefaceMuscle(name, gaze, time_value):
    # set eyes movement 9 gaze to default
    cmds.setKeyframe('ctrlEye_R.translateX', at='tx', v=gaze[0], t=time_value)
    cmds.setKeyframe('ctrlEye_R.translateY', at='ty', v=gaze[1], t=time_value)
    cmds.setKeyframe('ctrlEye_L.translateX', at='tx', v=gaze[0], t=time_value)
    cmds.setKeyframe('ctrlEye_L.translateY', at='ty', v=gaze[1], t=time_value)
    face_lst = [('upperLid', 0), ('upperLidBase', 0.4),
                ('EyeBrowRegion', 0.4), ('lowerLid', -0.2)]
    if 'Up' in name:
        for i in face_lst:
            cmds.setKeyframe(i[0]+'_R.translateY', at='ty',
                             v=i[1], t=time_value)
            cmds.setKeyframe(i[0]+'_L.translateY', at='ty',
                             v=i[1], t=time_value)
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
        for i in face_lst:
            cmds.setKeyframe(i[0]+'_R.translateY', at='ty',
                             v=0, t=time_value)
            cmds.setKeyframe(i[0]+'_L.translateY', at='ty',
                             v=0, t=time_value)

# ------------------- setMovementGaze Preview -------------------

def setMovementGaze(self):
    time_value = 0
    for name, gaze in lst_Nine:
        time_value += 1
        cmds.playbackOptions(edit=True, minTime='1', maxTime=time_value)
        movefaceMuscle(name, gaze, time_value)
    # set model
    for i in range(time_value):
        no = ""
        cmds.currentTime(i+1)
        cmds.select('geo'+no)
        cmds.duplicate('geo'+no)
        cmds.move(100*(i+1), 0, 0)
        no = str(i)

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

# ------------------ bakeSimulation ------------------

def bakeSimu(self):
    start = cmds.playbackOptions(q=1, min=1)
    end = cmds.playbackOptions(q=1, max=1)
    cmds.select('geo', 'Head_M', hierarchy=True)
    cmds.bakeResults(t=(start, end), simulation=True)

# ------------------- set Position Of Gaze (NORMAL) -------------------

def setNormalNinePositionOfGaze(textfieldAmount):
    amount = getAmountValue(textfieldAmount)
    time_value = 0
    value_noise = []
    for i in range(amount):
        for name, gaze in lst_Nine:
            time_value += 1
            cmds.playbackOptions(edit=True, minTime='1', maxTime=time_value)
            movefaceMuscle(name, gaze, time_value)
            # Add noise
            value_noise.append(round(rand.uniform(0, 0.5), 4))
            cmds.setKeyframe('AimEye_R.translateX', at='tx',
                             v=value_noise[i], t=time_value)
            cmds.setKeyframe('AimEye_L.translateX', at='ty',
                             v=value_noise[i], t=time_value)
    return time_value

# ------------------- set Position Of Gaze (Selected) -------------------

lstActionOU = [  # [value X], [value Y]
    # OVER ACTION
    ('radioOver_LIO_R', [[-4, 2], [1, 5]]),
    ('radioOver_LSO_R', [[-3, 2], [-3, -1]]),
    ('radioOver_RIO_L', [[1, 4], [1, 4]]),
    ('radioOver_RSO_L', [[-4, -1], [-2, -1]]),
    # UNDER ACTION
    ('radioUnder_RSR_R', [[0, 0], [-5, -1]]),
    ('radioUnder_LIO_R', [[-3, 2], [-3, -1]]),
    ('radioUnder_RLR_R', [[2, 8], [0, 0]]),
    ('radioUnder_LMR_R', [[2, 8], [0, 0]]),
    ('radioUnder_RIR_R', [[0, 0], [1, 5]]),
    ('radioUnder_LSO_R', [[-1, 5], [1, 5]]),
    ('radioUnder_RIO_L', [[-4, -1], [-3, -1]]),
    ('radioUnder_LSR_L', [[0, 0], [-5, -1]]),
    ('radioUnder_RMR_L', [[-8, -2], [0, 0]]),
    ('radioUnder_LLR_L', [[-8, -2], [0, 0]]),
    ('radioUnder_RSO_L', [[-3, 2], [1, 3]]),
    ('radioUnder_LIR_L', [[0, 0], [1, 5]])
]

def setGazeleft(AimEye_side, checkGaze_left):
    for _, time_left in enumerate(checkGaze_left):
        cmds.setKeyframe(AimEye_side+'.translateX', v=0, t=time_left)
        cmds.setKeyframe(AimEye_side+'.translateY', v=0, t=time_left)

def setGazeSelected(AimEye_side, AimEye_translate, checkGaze_left, checkGaze_side, checkGaze_middle, xy_value_lst, value_noise_lst, num_part):
    setGazeleft(AimEye_side, checkGaze_left)
    for index_v, time_lst in enumerate(checkGaze_side):
        for time_ in time_lst:
            cmds.setKeyframe(
                AimEye_side+'.'+AimEye_translate, v=xy_value_lst[index_v]+value_noise_lst[index_v], t=time_)
            if time_ in checkGaze_middle:
                cmds.setKeyframe(AimEye_side+'.'+AimEye_translate, v=(
                    xy_value_lst[index_v]+num_part)+value_noise_lst[index_v], t=time_)


def setGazeObSelected(AimEye_side, checkGaze_left, checkGaze_side, checkGaze_middle, x_value_lst, y_value_lst, value_noise_lst, num_part):
    setGazeleft(AimEye_side, checkGaze_left)
    for index_v, time_lst in enumerate(checkGaze_side):
        for time_ in time_lst:
            cmds.setKeyframe(
                AimEye_side+'.translateX', v=x_value_lst[index_v]+value_noise_lst[index_v], t=time_)
            cmds.setKeyframe(
                AimEye_side+'.translateY', v=y_value_lst[index_v]+value_noise_lst[index_v], t=time_)
            if time_ in checkGaze_middle:
                cmds.setKeyframe(AimEye_side+'.translateX', v=(
                    x_value_lst[index_v]+num_part)+value_noise_lst[index_v], t=time_)
                cmds.setKeyframe(AimEye_side+'.translateY', v=(
                    y_value_lst[index_v]+num_part)+value_noise_lst[index_v], t=time_)


def setAbNinePositionOfGaze(textfieldAmount):

    amount = getAmountValue(textfieldAmount)
    radioCol = passValue(lstCollectEyes)

    value_noise = []
    time_value = 0
    time_value_2 = 0

    # value AimEyes
    x_value_lst = []
    y_value_lst = []

    # all checkGaze list
    checkGaze_R = []
    checkGaze_L = []
    checkGaze_middle = []
    checkGaze_left_R = []
    checkGaze_left_L = []

    # SR
    Gaze_up_lst_R = []
    checkGaze_up_R = []
    Gaze_up_lst_L = []
    checkGaze_up_L = []
    upGaze_input_lst = []

    # IR
    gaze_IR_lst_R = []
    checkGaze_IR_R = []
    gaze_IR_lst_L = []
    checkGaze_IR_L = []
    gaze_IR_input_lst = []

    sixGaze_lst_R = []
    sixGaze_lst_L = []
    sixGaze_input_lst = []

    # Set Normal Gaze
    for _ in range(amount):
        for name, gaze in lst_Nine:
            time_value += 1
            if 'Right' in name or 'middle' in name:
                sixGaze_lst_R.append(time_value)
            if 'Left' in name or 'middle' in name:
                sixGaze_lst_L.append(time_value)
            # SR
            if 'Right Up' in name or 'Upgaze middle' in name or 'Primary' in name:
                Gaze_up_lst_R.append(time_value)
            if 'Left Up' in name or 'Upgaze middle' in name or 'Primary' in name:
                Gaze_up_lst_L.append(time_value)
            # IR
            if 'Right Up' in name or 'Right Down' in name or 'middle' in name or 'Left Up' in name:
                gaze_IR_lst_R.append(time_value)
            if 'Left Up' in name or 'Left Down' in name or 'middle' in name or 'Right Up' in name:
                gaze_IR_lst_L.append(time_value)
            # middle
            if 'middle' in name:
                checkGaze_middle.append(time_value)
            # check gaze left
            if 'Right' not in name:
                checkGaze_left_R.append(time_value)
            elif 'Left' not in name:
                checkGaze_left_L.append(time_value)

    for r in sixGaze_lst_R:
        sixGaze_input_lst.append(r)
        if len(sixGaze_input_lst) % 6 == 0:
            checkGaze_R.append(sixGaze_input_lst)
            sixGaze_input_lst = []

    for l in sixGaze_lst_L:
        sixGaze_input_lst.append(l)
        if len(sixGaze_input_lst) % 6 == 0:
            checkGaze_L.append(sixGaze_input_lst)
            sixGaze_input_lst = []
    # SR
    for up_r in Gaze_up_lst_R:
        upGaze_input_lst.append(up_r)
        if len(upGaze_input_lst) % 3 == 0:
            checkGaze_up_R.append(upGaze_input_lst)
            upGaze_input_lst = []

    for up_l in Gaze_up_lst_L:
        upGaze_input_lst.append(up_l)
        if len(upGaze_input_lst) % 3 == 0:
            checkGaze_up_L.append(upGaze_input_lst)
            upGaze_input_lst = []
    # IR
    for gIR_r in gaze_IR_lst_R:
        gaze_IR_input_lst.append(gIR_r)
        if len(gaze_IR_input_lst) % 6 == 0:
            checkGaze_IR_R.append(gaze_IR_input_lst)
            gaze_IR_input_lst = []
    for gIR_l in gaze_IR_lst_L:
        gaze_IR_input_lst.append(gIR_l)
        if len(gaze_IR_input_lst) % 6 == 0:
            checkGaze_IR_L.append(gaze_IR_input_lst)
            gaze_IR_input_lst = []

    print('checkGaze_R', checkGaze_R)
    print('checkGaze_L', checkGaze_L)
    print('checkGaze_middle', checkGaze_middle)
    print('checkGaze_left_R', checkGaze_left_R)
    print('checkGaze_left_L', checkGaze_left_L)

    for _ in range(amount):
        for name, gaze in lst_Nine:
            time_value_2 += 1
            cmds.playbackOptions(edit=True, minTime='1', maxTime=time_value_2)
            movefaceMuscle(name, gaze, time_value_2)
        # Add value selected
        for name_OU, scale in lstActionOU:
            if radioCol in name_OU:
                # print('user selected', name_OU,scale)
                for x_value in range(scale[0][0], scale[0][1]):
                    value_noise.append(round(rand.uniform(0, 0.5), 4))
                    x_value_lst.append(x_value)
                for y_value in range(scale[1][0], scale[1][1]):
                    value_noise.append(round(rand.uniform(0, 0.5), 4))
                    y_value_lst.append(y_value)

    for name_OU, scale in lstActionOU:
        # Check มุมมองทืศทางที่ตาขยับ เช่น มองไปทาง Right gaze
        if radioCol in name_OU:
            print('radioCol', radioCol)
            if 'R' == name_OU[-1:][0]:
                # print("_R",name_OU[-1:][0], name_OU)

                # LR / R gaze
                if 'LR' == name_OU[-4:-2]:
                    print('Yes! LR and R gaze:')
                    setGazeSelected('AimEye_R', 'translateX', checkGaze_left_R,
                                    checkGaze_R,   checkGaze_middle, x_value_lst, value_noise, -3)
                # MR / R gaze
                elif 'MR' == name_OU[-4:-2]:
                    print('Yes! MR and R gaze:')
                    setGazeSelected('AimEye_L', 'translateX', checkGaze_left_R,
                                    checkGaze_R, checkGaze_middle, x_value_lst, value_noise, -2)
                # SR / R gaze
                elif 'SR' == name_OU[-4:-2]:
                    print('Yes! SR and R gaze:')
                    setGazeSelected('AimEye_R', 'translateY', checkGaze_left_R,
                                    checkGaze_up_R, checkGaze_middle, y_value_lst, value_noise, 1)
                # IR / R gaze
                elif 'IR' == name_OU[-4:-2]:
                    print('Yes! IR and R gaze:')
                    setGazeSelected('AimEye_R', 'translateY', checkGaze_left_R,
                                    checkGaze_IR_R, checkGaze_middle, y_value_lst, value_noise, -1)
                # IO / R gaze
                elif 'IO' == name_OU[-4:-2]:
                    if 'Over' in name_OU:
                        print('Yes! IOOA and R gaze:', name_OU)
                        setGazeObSelected('AimEye_L', checkGaze_left_R, checkGaze_R,
                                          checkGaze_middle, x_value_lst, y_value_lst, value_noise, 1)
                    elif 'Under' in name_OU:
                        print('Yes! IOUA and R gaze:', name_OU)
                        setGazeObSelected('AimEye_L', checkGaze_left_R, checkGaze_R,
                                          checkGaze_middle, x_value_lst, y_value_lst, value_noise, -2)

                # SO / R gaze
                elif 'SO' == name_OU[-4:-2]:
                    print('Yes! SO and R gaze:')
                    if 'Over' in name_OU:
                        print('Yes! SOOA and R gaze:', name_OU)
                        setGazeObSelected('AimEye_L', checkGaze_left_R, checkGaze_R,
                                          checkGaze_middle, x_value_lst, y_value_lst, value_noise, 1)
                    elif 'Under' in name_OU:
                        print('Yes! SOUA and R gaze:', name_OU)
                        setGazeObSelected('AimEye_L', checkGaze_left_R, checkGaze_R,
                                          checkGaze_middle, x_value_lst, y_value_lst, value_noise, -1)

            elif 'L' == name_OU[-1:][0]:
                # LR / L gaze
                if 'LR' == name_OU[-4:-2]:
                    print('Yes! LR and L gaze')
                    setGazeSelected('AimEye_L', 'translateX', checkGaze_left_L,
                                    checkGaze_L, checkGaze_middle, x_value_lst, value_noise, 3)

                # MR / L gaze
                elif 'MR' == name_OU[-4:-2]:
                    print('Yes! MR and L gaze')
                    setGazeSelected('AimEye_R', 'translateX', checkGaze_left_L,
                                    checkGaze_L, checkGaze_middle, x_value_lst, value_noise, 2)
                # SR / L gaze
                elif 'SR' == name_OU[-4:-2]:
                    print('Yes! SR and L gaze:')
                    setGazeSelected('AimEye_L', 'translateY', checkGaze_left_L,
                                    checkGaze_up_L, checkGaze_middle, y_value_lst, value_noise, 1)
                #  IR / L gaze
                elif 'IR' == name_OU[-4:-2]:
                    print('Yes! IR and L gaze:')
                    setGazeSelected('AimEye_L', 'translateY', checkGaze_left_L,
                                    checkGaze_IR_L, checkGaze_middle, y_value_lst, value_noise, -1)
                # IO / L gaze
                elif 'IO' == name_OU[-4:-2]:
                    if 'Over' in name_OU:
                        print('Yes! IOOA and R gaze:', name_OU)
                        setGazeObSelected('AimEye_R', checkGaze_left_L, checkGaze_L,
                                          checkGaze_middle, x_value_lst, y_value_lst, value_noise, -2)
                    elif 'Under' in name_OU:
                        print('Yes! IOUA and R gaze:', name_OU)
                        setGazeObSelected('AimEye_R', checkGaze_left_L, checkGaze_L,
                                          checkGaze_middle, x_value_lst, y_value_lst, value_noise, -2)
                # SO / L gaze
                elif 'SO' == name_OU[-4:-2]:
                    print('Yes! SO and R gaze:')
                    if 'Over' in name_OU:
                        print('Yes! SOOA and R gaze:', name_OU)
                        setGazeObSelected('AimEye_R', checkGaze_left_L, checkGaze_L,
                                          checkGaze_middle, x_value_lst, y_value_lst, value_noise, 1)
                    elif 'Under' in name_OU:
                        print('Yes! SOUA and R gaze:', name_OU)
                        setGazeObSelected('AimEye_R', checkGaze_left_L, checkGaze_L,
                                          checkGaze_middle, x_value_lst, y_value_lst, value_noise, -1)

    return time_value

if __name__ == "__main__":
    createUI('Ocular motility test images generating system')
