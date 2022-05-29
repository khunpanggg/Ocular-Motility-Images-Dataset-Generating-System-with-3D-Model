import maya.cmds as cmds
import random as rand

from mainUI import MainUI

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

# need fix later, coupling name
lstCollectEyes = ['collectEyes_RSR', 'collectEyes_LIO', 'collectEyes_RIO', 'collectEyes_LSR', 'collectEyes_RLR', 'collectEyes_LMR',
                  'collectEyes_RMR', 'collectEyes_LLR', 'collectEyes_RIR', 'collectEyes_LSO', 'collectEyes_RSO', 'collectEyes_LIR']

# ----------------- action_checkBox -----------------

lstcheckBox = ['RSR', 'LIO', 'RIO', 'LSR', 'RLR', 'LMR',
               'RMR', 'LLR', 'RIR', 'LSO', 'RSO', 'LIR']


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

    # IR
    gaze_IR_lst_R = []
    checkGaze_IR_R = []
    gaze_IR_lst_L = []
    checkGaze_IR_L = []

    sixGaze_lst_R = []
    sixGaze_lst_L = []

    # set Gaze Position
    lst_Nine = [('Right Up', [-0.8, 0.5]), ('Upgaze middle', [0, 0.8]), ('Left Up', [0.8, 0.5]),
                ('Right', [-1, 0]), ('Primary middle',
                                     [0, 0]), ('Left', [1, 0]),
                ('Right Down', [-1, -1]), ('Downgaze middle', [0, -0.8]), ('Left Down', [1, -1])]

    # should calculate which time that show each gaze
    # Right Up = 1
    # Upgaze middle = 2
    # Left Up = 3
    # Right = 4
    # Primary middle = 5
    # Left = 6
    # Right Down = 7
    # Downgaze middle = 8
    # Left Down = 9
    #
    # ex. if amount = 2, let i to be each round of "amount"
    # the gaze list should be ...
    #  - sixGaze_lst_R = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17]
    #    (i*9+1, i*9+2, i*9+4, i*9+5, i*9+7, i*9+8)
    #  - sixGaze_lst_L = [2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18]
    #    (i*9+2, i*9+3, i*9+5, i*9+6, i*9+8, i*9+9)
    #  - Gaze_up_lst_R = [1, 2, 5, 10, 11, 14]
    #    (i*9+1, i*9+2, i*9+5)
    for i in range(amount):

        sixGaze_lst_R.append(i*9+1, i*9+2, i*9+4, i*9+5, i*9+7, i*9+8)
        sixGaze_lst_L.append(i*9+2, i*9+3, i*9+5, i*9+6, i*9+8, i*9+9)
        # SR Case
        Gaze_up_lst_R.append(i*9+1, i*9+2, i*9+5)
        Gaze_up_lst_L.append(i*9+1, i*9+2, i*9+5)
        # IR Case
        gaze_IR_lst_R.append(i*9+1, i*9+2, i*9+3, i*9+5, i*9+7, i*9+8)
        gaze_IR_lst_L.append(i*9+1, i*9+2, i*9+3, i*9+5, i*9+8, i*9+9)

        # checkGaze_middle
        checkGaze_middle.append(i*9+2, i*9+5, i*8)

        # checkGaze_left
        checkGaze_left_R.append(i*9+3, i*9+6, i*9+9)
        checkGaze_left_L.append(i*9+1, i*9+4, i*9+7)

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
    MainUI('Ocular motility test images generating system')
