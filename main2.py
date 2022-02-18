import maya.cmds as cmds


def createUI(windowTitle):
    window = 'OC_Window'
    # create new window
    window = cmds.window(window, title=windowTitle,
                         resizeToFitChildren=True, sizeable=True)
    cmds.columnLayout(adjustableColumn=True)
    menuBarLayout = cmds.menuBarLayout()
    cmds.menu(label='File')
    cmds.menuItem(label='New')
    cmds.menuItem(label='Open')
    cmds.menuItem(label='Close')
    cmds.menu(label='Help', helpMenu=True)
    cmds.menuItem(label='About...')

    # ------------ Position ------------
    infoColumnLayout = cmds.columnLayout(
        'infoColumnLayout', adjustableColumn=True, columnOffset=['both', 5], parent=window)
    cmds.paneLayout(configuration='quad', height=250)
    # ------------ Viewport ------------
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------ Preparation ------------
    cmds.frameLayout(label='Preparation', collapsable=True)
    cmds.rowColumnLayout(numberOfColumns=3, columnAttach=(
        (1, 'right', 2), (2, 'both', 3), (3, 'both', 3)), columnWidth=[(1, 200), (2, 150)])
    cmds.separator(height=30, style=None)
    cmds.button(label='Open Scene', command=openFile)
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.setParent('..')
    # # ------------ Setting for Primary  Position ------------
    # framePriSetting = cmds.frameLayout('framePriSetting',
    #                                    label='Setting for Primary  Position', collapsable=True, enable=True)
    # cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
    #     (1, 300), (2, 300)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    # cmds.frameLayout(label='Right eye')
    # cmds.rowColumnLayout(numberOfColumns=1)
    # Pri_TypeofStrabismus_R = cmds.optionMenuGrp(
    #     'TypeofStrabismus_R_1', w=300, label="Type of Strabismus :")
    # cmds.menuItem(label="esotropia")
    # cmds.menuItem(label="exotropia")
    # cmds.optionMenuGrp('TypeofStrabismus_R_2', w=300, label="")
    # cmds.menuItem(label="hypertropia")
    # cmds.menuItem(label="hypotropia")

    # cmds.setParent('..')
    # cmds.setParent('..')
    # cmds.frameLayout(label='Left eye')
    # cmds.rowColumnLayout(numberOfColumns=1)
    # Pri_TypeofStrabismus_L = cmds.optionMenuGrp(
    #     'TypeofStrabismus_L_1', w=300, label="Type of Strabismus :")
    # cmds.menuItem(label="esotropia")
    # cmds.menuItem(label="exotropia")
    # cmds.optionMenuGrp(
    #     'TypeofStrabismus_L_2', w=300, label="")
    # cmds.menuItem(label="hypertropia")
    # cmds.menuItem(label="hypotropia")
    # cmds.setParent('..')
    # cmds.setParent('..')
    # cmds.setParent('..')

    frameDiaSetting = cmds.frameLayout('frameDiaSetting',
                                       label='Setting for 9 diagnostic positions of gaze', enable=True, borderVisible=False, collapsable=True)
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 300), (2, 300)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    cmds.frameLayout(label='Right eye')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 100)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    cmds.text('right eye of all muscles : ')
    cmds.checkBox(label='normal')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.frameLayout(label='Left eye')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 100)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    cmds.text('left eye of all muscles : ')
    cmds.checkBox(label='normal')
    cmds.setParent('..')
    cmds.setParent('..')

    # Right Eye Muscles
    cmds.rowColumnLayout(numberOfColumns=4, columnWidth=[
        (1, 50), (2, 70), (3, 80), (4, 80)], columnOffset=[(1, 'both', 3), (2, 'both', 3)], bgc=[0.3, 0.3, 0.3])
    collectEyes_SR = cmds.radioCollection()
    cmds.text('SR')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')

    collectEyes_IO = cmds.radioCollection()
    cmds.text('IO')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')

    collectEyes_LR = cmds.radioCollection()
    cmds.text('LR')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')

    collectEyes_MR = cmds.radioCollection()
    cmds.text('MR')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')

    collectEyes_IR = cmds.radioCollection()
    cmds.text('IR')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')

    collectEyes_SO = cmds.radioCollection()
    cmds.text('SO')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')

    cmds.setParent('..')
    # Left Eye Muscles
    cmds.rowColumnLayout(numberOfColumns=4, columnWidth=[
        (1, 50), (2, 70), (3, 80), (4, 80)], columnOffset=[(1, 'both', 3), (2, 'both', 3)], bgc=[0.3, 0.3, 0.3])
    collectEyes_SR = cmds.radioCollection()
    cmds.text('SR')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')

    collectEyes_IO = cmds.radioCollection()
    cmds.text('IO')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')

    collectEyes_LR = cmds.radioCollection()
    cmds.text('LR')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')

    collectEyes_MR = cmds.radioCollection()
    cmds.text('MR')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')

    collectEyes_IR = cmds.radioCollection()
    cmds.text('IR')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')

    collectEyes_SO = cmds.radioCollection()
    cmds.text('SO')
    cmds.checkBox(label='normal')
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------- Amount -------
    cmds.paneLayout(configuration='quad')
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

    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 200), (2, 200), (3, 200)], columnOffset=[(1, 'both', 3), (2, 'both', 3), (3, 'both', 3)])
    cmds.button(label='Apply', height=30, command=applyButton)
    cmds.button(label='Render')
    cmds.button(label='Close', command=cancelCallback)
    cmds.setParent('..')
    cmds.showWindow()


def openFile(self):
    filename = cmds.fileDialog2(fileMode=1, caption="Import File")
    cmds.file(filename[0], i=True)


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

    # cmds.rowColumnLayout(numberOfColumns=2, columnOffset=(
    #     1, 'both', 5), columnWidth=[(1, 380), (2, 380)])
    # cmds.text('total of gaze : 6 ')
    # cmds.text('total of picture : 36 ')

    # cmds.setParent('..')
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


if __name__ == "__main__":
    createUI('Ocular motility test images generating system')
