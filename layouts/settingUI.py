import maya.cmds as cmds

class SettingUI:
    def __init__(self, parentLayout):
        self.mainLayout = cmds.rowColumnLayout(
            numberOfColumns=2, 
            columnWidth=[(1, 450), (2, 450)], 
            columnOffset=[(1, 'both', 2)]
        )

        # ------------------ Amount ------------------
        self.amountUI = cmds.frameLayout(label='Amount of Images', parent=self.mainLayout, collapsable=True)
        cmds.separator(height=5, style=None, parent=self.amountUI)

        self.amountLayout = cmds.rowColumnLayout(
            parent=self.amountUI,
            numberOfColumns=3, 
            columnAttach=((1, 'right', 3), (2, 'both', 3), (3, 'both', 3)), 
            columnWidth=[(1, 100), (2, 150)]
        )

        cmds.text(label='amount :', parent=self.amountLayout)
        AmountImages = cmds.textField(parent=self.amountLayout)
        cmds.iconTextButton(style='iconOnly', image1='help.xpm', parent=self.amountLayout)
        cmds.separator(height=5, style=None)

        # ------------------ Create Lighting ------------------
        self.lightningUI = cmds.frameLayout(label='Create Lighting', parent=self.mainLayout, collapsable=True)
        cmds.separator(height=5, style=None, parent=self.mainLayout)
        
        self.lightningLayout = cmds.rowColumnLayout(
            parent=self.lightningUI,
            numberOfColumns=2, 
            columnAttach=((1, 'both', 2)),
        )
        lightningOptionGroup = cmds.optionMenuGrp(
            'optionLighting', 
            label="lightning location :", 
            parent=self.lightningLayout,
            w=250)
        cmds.menuItem(label="Outdoor", parent=lightningOptionGroup)
        cmds.menuItem(label="Indoor", parent=lightningOptionGroup)
        cmds.iconTextButton(style='iconOnly', image1='help.xpm', parent=self.lightningLayout)