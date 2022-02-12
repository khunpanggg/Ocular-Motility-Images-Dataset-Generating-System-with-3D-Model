from tracemalloc import Trace
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
                     wireframeOnShaded=True, swf=True)
    cmds.setParent('..')
    cmds.setParent('..')

    # ------------ Preparation ------------
    cmds.frameLayout(label='Preparation')
    cmds.rowColumnLayout(numberOfColumns=3, columnAttach=(
        (1, 'right', 3), (2, 'both', 3), (3, 'both', 3)), columnWidth=[(1, 200), (2, 150)])
    cmds.separator(height=30, style=None)
    cmds.button(label='Open Scene', command=openFile)
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.setParent('..')
    # ------------ Setting for Primary  Position ------------
    framePriSetting = cmds.frameLayout('framePriSetting',
                                       label='Setting for Primary  Position', collapsable=False, enable=True)
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 300), (2, 300)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    cmds.text('Right eye')
    cmds.text('Left eye')

    Pri_TypeofStrabismus_R = cmds.optionMenuGrp(
        'TypeofStrabismus_R', w=100, label="Type of Strabismus :")
    cmds.menuItem(label="Esotropia")
    cmds.menuItem(label="Exotropia")

    Pri_TypeofStrabismus_L = cmds.optionMenuGrp(
        'TypeofStrabismus_L', w=100, label="Type of Strabismus :")
    cmds.menuItem(label="Esotropia")
    cmds.menuItem(label="Exotropia")
    cmds.setParent('..')
    cmds.setParent('..')

    frameDiaSetting = cmds.frameLayout('frameDiaSetting',
                                       label='Setting for 9 diagnostic positions of gaze', enable=True)
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 300), (2, 300)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    cmds.text('Right eye')
    cmds.text('Left eye')
    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=4, columnWidth=[
        (1, 150), (2, 100), (3, 150), (4, 100)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    cmds.text('right eye of all muscles : ')
    cmds.checkBox(label='normal')
    cmds.text('left eye of all muscles : ')
    cmds.checkBox(label='normal')
    cmds.setParent('..')

    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 300), (2, 300)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 50), (2, 100), (3, 100)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])

    collectEyes_SR = cmds.radioCollection()
    cmds.text('SR')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')

    collectEyes_IO = cmds.radioCollection()
    cmds.text('IO')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')

    collectEyes_LR = cmds.radioCollection()
    cmds.text('LR')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')

    collectEyes_MR = cmds.radioCollection()
    cmds.text('MR')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')

    collectEyes_IR = cmds.radioCollection()
    cmds.text('IR')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')

    collectEyes_SO = cmds.radioCollection()
    cmds.text('SO')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')

    cmds.setParent('..')
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 50), (2, 100), (3, 100)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    collectEyes_SR = cmds.radioCollection()
    cmds.text('SR')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')

    collectEyes_IO = cmds.radioCollection()
    cmds.text('IO')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')

    collectEyes_LR = cmds.radioCollection()
    cmds.text('LR')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')

    collectEyes_MR = cmds.radioCollection()
    cmds.text('MR')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')

    collectEyes_IR = cmds.radioCollection()
    cmds.text('IR')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')

    collectEyes_SO = cmds.radioCollection()
    cmds.text('SO')
    normal_eyes = cmds.radioButton(label='normal')
    abnormal_eyes = cmds.radioButton(label='abnormal')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------- Amount -------
    cmds.paneLayout(configuration='quad')
    cmds.frameLayout(label='Amount of Images')
    cmds.separator(height=5, style=None)
    cmds.rowColumnLayout(numberOfColumns=3, columnAttach=(
        (1, 'right', 3), (2, 'both', 3), (3, 'both', 3)), columnWidth=[(1, 100), (2, 150)])
    cmds.text(label='Amount:')
    AmoutImages = cmds.textField()

    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.separator(height=10, style=None)

    cmds.setParent('..')
    cmds.setParent('..')
    cmds.frameLayout(label='Create Lighting')
    cmds.optionMenuGrp('optionLighting', w=200, label="HDRIs :",
                       changeCommand=lambda x: apply_texture())
    cmds.menuItem(label="Outdoor")
    cmds.menuItem(label="Skies")
    cmds.menuItem(label="Indoor")
    cmds.menuItem(label="Studio")
    cmds.menuItem(label="Nature")
    cmds.menuItem(label="Urban")
    cmds.setParent('..')
    cmds.setParent('..')

    def cancelCallback(*args):
        if cmds.window(window, exists=True):
            cmds.deleteUI(window)

    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 200), (2, 200), (3, 200)], columnOffset=[(1, 'both', 3), (2, 'both', 3), (3, 'both', 3)])
    cmds.button(label='Apply', height=30)
    cmds.button(label='Render')
    cmds.button(label='Close', command=cancelCallback)
    cmds.setParent('..')
    cmds.showWindow()


def openFile(self):
    filename = cmds.fileDialog2(fileMode=1, caption="Import File")
    cmds.file(filename[0], i=True)


if __name__ == "__main__":
    createUI('Ocular motility test images generating system')
