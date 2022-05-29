
import maya.cmds as cmds

from layouts.preparationUI import PreparationUI
from layouts.diagonosticUI import DiagonosticUI
from layouts.settingUI import SettingUI


class MainUI:
    def __init__(self, windowTitle):
        self.windowName = 'OC_Window'  # must unique per runtime

        if cmds.window(self.windowName, query=True, exists=True):
            # use same window
            pass
        else:
            # create new window
            self.windowFrame = cmds.window(self.windowName, title=windowTitle,
                                           resizeToFitChildren=True, sizeable=True)
        self.mainLayout = cmds.rowColumnLayout(
            parent=self.windowFrame,
            adjustableColumn=True,
            numberOfColumns=2,
            columnAttach=((1, 'left', 2), (2, 'both', 2)),
            columnWidth=[(1, 200)],
            columnOffset=[(1, 'both', 1)]
        )

        self.sectionRight = cmds.flowLayout(self.mainLayout)
        self.prepartionUI = PreparationUI(self.mainLayout)
        self.diagonosticUI = DiagonosticUI(self.sectionRight)
        self.settingsUI = SettingUI(self.sectionRight)
        self.commandUI = cmds.rowColumnLayout(
            numberOfColumns=3,
            columnWidth=[(1, 300), (2, 300), (3, 300)],
            columnOffset=[(1, 'both', 3), (2, 'both', 3), (3, 'both', 3)]
        )
        cmds.button(label='Apply', height=30,
                    command=self.applyButton, parent=self.commandUI)
        cmds.button(label='Render', command=self.renderButton,
                    parent=self.commandUI)
        cmds.button(label='Close', command=self.cancelCallback,
                    parent=self.commandUI)

        # Set window visible
        cmds.showWindow(self.windowFrame)

    def applyButton(self, *args):
        if self.diagonosticUI.isAllNormalEyes():
            print('normal eyes')
            # to-do
            loadWindowPreview(setNormalNinePositionOfGaze(
                AmoutImages), AmoutImages)
        else:
            print('abnormal eyes')
            # to-do
            loadWindowPreview(setAbNinePositionOfGaze(
                AmoutImages), AmoutImages)

    def renderButton(self, *args):
        # normal selected
        setNormalNinePositionOfGaze(AmoutImages)

    def cancelCallback(self, *args):
        if cmds.window(window, exists=True):
            cmds.deleteUI(window)
