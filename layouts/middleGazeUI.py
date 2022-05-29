import maya.cmds as cmds

class MiddleGazeUI:
    def __init__(self, parentLayout, frameTitle, faceCamera):
        self.mainFrame = cmds.frameLayout(label=frameTitle, parent=parentLayout)
        self.mainLayout = cmds.paneLayout(parent=self.mainFrame, configuration='quad', height=100)
        cmds.modelEditor(
            parent=self.mainLayout,
            da='smoothShaded',
            dtx=True,
            wireframeOnShaded=False, 
            swf=True, 
            displayLights='all', 
            camera=faceCamera
        )
        