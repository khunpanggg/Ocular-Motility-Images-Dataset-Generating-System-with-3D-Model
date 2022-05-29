import collections
import maya.cmds as cmds

class CardinalGazeUI:
    def __init__(self, parentLayout, gazeTitle, muscleRightName, muscleLeftName, faceCamera):
        self.mainLayout = cmds.frameLayout(label=gazeTitle, parent=parentLayout)
        # ----------------------------------------
        # Name Muscle Layout
        # ----------------------------------------
        self.nameMuscleLayout = cmds.rowColumnLayout(
            parent=self.mainLayout,
            numberOfColumns=2, 
            columnWidth=[(1, 150), (2, 150)], 
            columnOffset=[(1, 'both', 2)]
        )
        cmds.text(muscleRightName, parent=self.nameMuscleLayout, bgc=[0.1, 0.1, 0.1])
        cmds.text(muscleLeftName, parent=self.nameMuscleLayout, bgc=[0.1, 0.1, 0.1])

        # ----------------------------------------
        # Viewport Layout
        # ----------------------------------------
        self.viewportLayout = cmds.paneLayout(
            parent=self.mainLayout,
            configuration='quad', 
            height=100
        )
        cmds.modelEditor(
            parent=self.viewportLayout,
            da='smoothShaded', 
            dtx=True,
            # wireframeOnShaded=False, 
            # swf=True,
            displayLights='all', 
            camera=faceCamera
        )

        # ----------------------------------------
        # Eye Gaze Selector Layout
        # ----------------------------------------
        self.eyeGazeSelectorLayout = cmds.rowColumnLayout(
            parent=self.mainLayout,
            numberOfColumns=2, 
            columnWidth=[(1, 150), (2, 150)], 
            columnOffset=[(1, 'both', 2)]
        )

        # ----------------------------------------
        # Right Gaze Layout
        # ----------------------------------------
        self.rightGazeLayout = cmds.rowColumnLayout(
            parent=self.eyeGazeSelectorLayout,
            numberOfColumns=1, 
            columnWidth=[(1, 150), (2, 150)], 
            columnOffset=[(1, 'both', 2)]
        )
        # self.radioCollectionRightName = 'collectEyes_' + muscleRightName
        self.radioCollectionRight = cmds.radioCollection(parent=self.rightGazeLayout)
        radioNormalRight = cmds.radioButton(muscleRightName, label='normal', collection=self.radioCollectionRight)
        radioOverRight = cmds.radioButton('radioOver_' + muscleRightName + '_R', label='overaction', collection=self.radioCollectionRight)
        radioUnderRight = cmds.radioButton('radioUnder_' + muscleRightName + '_R', label='underaction', collection=self.radioCollectionRight)

        # ----------------------------------------
        # Left Gaze Layout
        # ----------------------------------------
        self.leftGazeLayout = cmds.rowColumnLayout(
            parent=self.eyeGazeSelectorLayout,
            numberOfColumns=1, 
            columnWidth=[(1, 150), (2, 150)], 
            columnOffset=[(1, 'both', 2)]
        )
        # self.radioCollectionLeftName = 'collectEyes_' + muscleLeftName
        self.radioCollectionLeft = cmds.radioCollection(parent=self.leftGazeLayout)
        radioNormalLeft = cmds.radioButton(muscleLeftName, label='normal', collection=self.radioCollectionLeft)
        radioOverLeft = cmds.radioButton('radioOver_' + muscleLeftName + '_R', label='overaction', collection=self.radioCollectionLeft)
        radioUnderLeft = cmds.radioButton('radioUnder_' + muscleLeftName + '_R', label='underaction', collection=self.radioCollectionLeft)


    def isBothNormal(self):
        selectedRight = cmds.radioCollection(self.radioCollectionRight, query=True, select=True)
        selectedLeft = cmds.radioCollection(self.radioCollectionLeft, query=True, select=True)
        resultRight = cmds.radioButton(selectedRight, query=True, label=True)
        resultLeft = cmds.radioButton(selectedLeft, query=True, label=True)
        return resultRight == 'normal' and resultLeft == 'normal'
