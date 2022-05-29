import maya.cmds as cmds

class PreparationUI:
    def __init__(self, parentLayout):
        # ------------ 1. Preparation ------------
        self.mainLayout = cmds.frameLayout(label='Preparation', parent=parentLayout, collapsable=True, marginWidth=5)

        # ----------------------------------------
        # 1.1 import file section
        importFileSection = cmds.frameLayout(label='Import Flie', parent=self.mainLayout, collapsable=True)
        importFileLayout = cmds.rowColumnLayout(
            parent=importFileSection,
            numberOfColumns=2, 
            columnWidth=[(1, 100), (2, 80)], 
            columnOffset=[(1, 'both', 5), (2, 'left', 10)], 
            bgc=[0.2, 0.2, 0.2], 
            rowAttach=[(1, "top", 2), (2, "top", 2)]
        )
        # button set project: in import file section
        cmds.button(label='Set Project', parent=importFileLayout, command=self.openFile, bgc=[0.4, 0.4, 0.4])
        cmds.iconTextButton(style='iconOnly', image1='help.xpm')
        # button open scene: in import file section
        cmds.button(label='Open Scene', parent=importFileLayout, command=self.openFile, bgc=[0.4, 0.4, 0.4])
        cmds.iconTextButton(style='iconOnly', image1='help.xpm')
        
        # ----------------------------------------
        # 1.2 setting viewport section
        # ----------------------------------------
        viewportSection = cmds.frameLayout(label='Setting Viewport', parent=self.mainLayout, collapsable=True)
        viewportLayout = cmds.rowColumnLayout(
            parent=viewportSection,
            numberOfColumns=2,
            columnWidth=[(1, 100), (2, 80)], 
            columnOffset=[(1, 'both', 5), (2, 'left', 10)], 
            bgc=[0.2, 0.2, 0.2], 
            rowAttach=[(1, "top", 2), (2, "top", 2)]
        )
        # button set gaze: in viewport section
        cmds.button(label='Set Gaze', parent=viewportLayout, command=self.setMovementGaze, bgc=[0.4, 0.4, 0.4])
        cmds.iconTextButton(style='iconOnly', image1='help.xpm')
        # button set camera: in viewport section
        cmds.button(label='Set Camera', parent=viewportLayout, command=self.setCamaraGaze, bgc=[0.4, 0.4, 0.4])
        cmds.iconTextButton(style='iconOnly', image1='help.xpm')
        
        # ----------------------------------------
        # 1.3 tool section
        # ----------------------------------------
        toolSection = cmds.frameLayout(label='Tool', parent=self.mainLayout, collapsable=True)
        toolLayout = cmds.rowColumnLayout(
            parent=toolSection,
            numberOfColumns=2, 
            columnWidth=[(1, 100), (2, 80)], 
            columnOffset=[(1, 'both', 5), (2, 'left', 10)], 
            bgc=[0.2, 0.2, 0.2], 
            rowAttach=[(1, "top", 2), (2, "top", 2)]
        )
        # button bake simulation: in tool section
        cmds.button(label='Bake Simulation', parent=toolLayout, command=self.bakeSimulation, bgc=[0.4, 0.4, 0.4])
        cmds.iconTextButton(style='iconOnly', image1='help.xpm')
        # button reset: in tool section
        cmds.button(label='Reset', parent=toolLayout, command=self.openFile, bgc=[0.4, 0.4, 0.4])
        cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    
    def openFile(self):
        pass

    def setMovementGaze(self):
        pass

    def setCamaraGaze(self):
        pass

    def bakeSimulation(self):
        pass

