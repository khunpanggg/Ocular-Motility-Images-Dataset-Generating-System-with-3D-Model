import maya.cmds as cmds

from layouts.middleGazeUI import MiddleGazeUI
from layouts.cardinalGazeUI import CardinalGazeUI

class DiagonosticUI:
    def __init__(self, parentLayout):
        # ------------------ Setting for 9 diagnostic positions of gaze ------------------
        self.mainFrame = cmds.frameLayout(
            'frameDiaSetting',
            label='Setting for 9 diagnostic positions of gaze', 
            parent=parentLayout,
            enable=True, 
            borderVisible=False, 
            collapsable=True
        )
        self.mainLayout = cmds.rowColumnLayout(
            numberOfColumns=3, 
            columnWidth=[(1, 300), (2, 300), (3, 300)], 
            columnOffset=[(1, 'both', 3), (2, 'both', 3), (3, 'both', 3)]
        )

        # ------------------ Right & Up Gaze ------------------
        self.rightUpGazeUI = CardinalGazeUI(
            parentLayout=self.mainLayout, 
            gazeTitle='Right & Up Gaze', 
            muscleRightName='RSR', 
            muscleLeftName='LIO', 
            faceCamera='faceCam2'
        )

        # ------------------ Up Gaze ------------------
        self.upGazeUI = MiddleGazeUI(
            self.mainLayout,
            'Up Gaze',
            'faceCam3'
        )

        # ------------------ Left & Up Gaze ------------------
        self.leftUpGazeUI = CardinalGazeUI(
            parentLayout=self.mainLayout, 
            gazeTitle='Left & Up Gaze', 
            muscleRightName='RIO', 
            muscleLeftName='LSR', 
            faceCamera='faceCam2'
        )

        # ------------------ Right Gaze ------------------
        self.rightGazeUI = CardinalGazeUI(
            parentLayout=self.mainLayout, 
            gazeTitle='Right Gaze', 
            muscleRightName='RLR', 
            muscleLeftName='LMR', 
            faceCamera='faceCam5'
        )

        # ------------------ Primary Position ------------------
        self.primaryGazeUI = MiddleGazeUI(
            self.mainLayout,
            'Primary Position',
            'faceCam6'
        )

        # ------------------ Left Gaze ------------------
        self.leftGazeUI = CardinalGazeUI(
            parentLayout=self.mainLayout, 
            gazeTitle='Left Gaze', 
            muscleRightName='RMR', 
            muscleLeftName='LLR', 
            faceCamera='faceCam7'
        )

        # ------------------ Right & Down Gaze ------------------
        self.rightDownGazeUI = CardinalGazeUI(
            parentLayout=self.mainLayout, 
            gazeTitle='Right & Down Gaze', 
            muscleRightName='RIR', 
            muscleLeftName='LSO', 
            faceCamera='faceCam8'
        )

        # ------------------ Down Gaze ------------------
        self.downGazeUI = MiddleGazeUI(
            self.mainLayout,
            'Down Gaze',
            'faceCam9'
        )

        # ------------------ Left & Down Gaze ------------------
        self.leftDownGazeUI = CardinalGazeUI(
            parentLayout=self.mainLayout, 
            gazeTitle='Left & Down Gaze', 
            muscleRightName='RSO', 
            muscleLeftName='LIR', 
            faceCamera='faceCam10'
        )

    def isAllNormalEyes(self):
        return self.rightUpGazeUI.isBothNormal() and \
            self.leftUpGazeUI.isBothNormal() and \
            self.rightGazeUI.isBothNormal() and \
            self.leftGazeUI.isBothNormal() and \
            self.rightDownGazeUI.isBothNormal() and \
            self.leftDownGazeUI.isBothNormal()
