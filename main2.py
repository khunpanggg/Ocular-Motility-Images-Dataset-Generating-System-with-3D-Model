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

    # ------------ Preparation ------------
    cmds.frameLayout(label='Preparation', collapsable=True)
    cmds.rowColumnLayout(numberOfColumns=3, columnAttach=(
        (1, 'right', 2), (2, 'both', 3), (3, 'both', 3)), columnWidth=[(1, 200), (2, 150)])
    cmds.separator(height=30, style=None)
    cmds.button(label='Open Scene', command=openFile)
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.setParent('..')

    frameDiaSetting = cmds.frameLayout('frameDiaSetting',
                                       label='Setting for 9 diagnostic positions of gaze', enable=True, borderVisible=False, collapsable=True)
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 300), (2, 300), (3, 300)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    cmds.frameLayout(label='Right & Up Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('SR', bgc=[0.1, 0.1, 0.1])
    cmds.text('IO', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')
    # cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[(1, 300)])
    # cmds.picture(image=(
    #     'C:/Users/Khunpang/Documents/maya/projects/mermaid/images/abnormal/1/scale_(2)/mermaid_model_use_3_normal_1_1.jpg'))
    # cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.frameLayout(label='Up Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 100)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    cmds.text('left eye of all muscles : ')
    cmds.checkBox(label='normal')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.frameLayout(label='Left & Up Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('IO', bgc=[0.1, 0.1, 0.1])
    cmds.text('SR', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')

    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.frameLayout(label='Right Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('LR', bgc=[0.1, 0.1, 0.1])
    cmds.text('MR', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')

    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.frameLayout(label='Primary Position')
    cmds.paneLayout(configuration='quad', height=200)
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=False, swf=True, displayLights='all')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.frameLayout(label='Left Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('MR', bgc=[0.1, 0.1, 0.1])
    cmds.text('LR', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')

    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.frameLayout(label='Right & Down Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('IR', bgc=[0.1, 0.1, 0.1])
    cmds.text('SO', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')

    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.frameLayout(label='Down Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 100)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    cmds.text('left eye of all muscles : ')
    cmds.checkBox(label='normal')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.frameLayout(label='Left & Down Gaze')
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.text('IR', bgc=[0.1, 0.1, 0.1])
    cmds.text('SO', bgc=[0.1, 0.1, 0.1])
    cmds.setParent('..')

    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=[
        (1, 150), (2, 150)], columnOffset=[(1, 'both', 2)])
    cmds.checkBox(label='normal')
    collectEyes_SR = cmds.radioCollection()
    normal_eyes = cmds.radioButton(label='overaction', select=True)
    abnormal_eyes = cmds.radioButton(label='underaction')
    cmds.setParent('..')
    cmds.setParent('..')
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
        (1, 300), (2, 300), (3, 300)], columnOffset=[(1, 'both', 3), (2, 'both', 3), (3, 'both', 3)])
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
