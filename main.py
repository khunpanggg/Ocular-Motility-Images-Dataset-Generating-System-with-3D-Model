import maya.OpenMaya as om
import maya.cmds as cmds
from functools import partial
import random as rand
from mtoa.cmds.arnoldRender import arnoldRender
import mtoa.core as core
import mtoa.utils as mutils  # skydome
import maya.app.general.createImageFormats as createImageFormats

# def arnoldOpenMtoARenderView():
#     core.createOptions()
#     cmds.arnoldRenderView(mode="open")


# def arnoldMtoARenderView():
#     # core.ACTIVE_CAMERA is not set, anything we could do here ?
#     # if core.ACTIVE_CAMERA != None:
#     #    cmds.arnoldRenderView(cam=core.ACTIVE_CAMERA)
#     # so instead we're calling it without any argument
#     core.createOptions()
#     cmds.arnoldRenderView()


# # execute both functions
# arnoldOpenMtoARenderView()
# arnoldMtoARenderView()

def openFile(self):
    filename = cmds.fileDialog2(fileMode=1, caption="Import File")
    cmds.file(filename[0], i=True)


def createUI(windowTitle):
    window = 'MR_Window'
    size = (400, 400)

    # create new window
    window = cmds.window(window, title=windowTitle,
                         resizeToFitChildren=True, widthHeight=size, sizeable=True)
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
    cmds.paneLayout(configuration='quad', height=300)
    # ------------ Viewport ------------
    cmds.modelEditor(da='smoothShaded', dtx=True,
                     wireframeOnShaded=True, swf=True)
    cmds.frameLayout(label='Preparation')
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 200), (2, 150)], columnOffset=[(1, 'both', 3)])
    cmds.separator(height=30, style=None)
    cmds.button(label='Open Scene', command=openFile)
    cmds.setParent('..')

    cmds.frameLayout(label='Position')
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 200), (2, 200)], columnOffset=[(1, 'right', 3)], rowSpacing=[1, 5])
    cmds.text('Type of Position :')
    collection1 = cmds.radioCollection()
    # Primary Position
    PriPos = cmds.radioButton(
        label='Primary Position (1 pattern)', select=True, changeCommand=lambda x: action_radioButton(PriPos, CarPos, DiaPos, normal_eyes, abnormal_eyes, AmoutImages))
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.separator(height=10, style=None)
    # Cardinal Position
    CarPos = cmds.radioButton(
        label='Cardinal Position (7 patterns)', changeCommand=lambda x: action_radioButton(PriPos, CarPos, DiaPos, normal_eyes, abnormal_eyes, AmoutImages))
    cmds.iconTextButton(
        style='iconOnly', image1='help.xpm', command=buttonhelp)
    cmds.separator(height=10, style=None)
    # 9 Diagnostic  Position
    DiaPos = cmds.radioButton(
        label='9 Diagnostic Position (9 patterns)', changeCommand=lambda x: action_radioButton(PriPos, CarPos, DiaPos, normal_eyes, abnormal_eyes, AmoutImages))
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.radioCollection(collection1, edit=True, select=PriPos)

    # ------------ Classify ------------
    cmds.frameLayout(label='Classify')
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 200), (2, 200)], columnOffset=[(1, 'right', 3)], rowSpacing=[1, 5])

    cmds.text('Type of eyes :')
    collection_eyes = cmds.radioCollection()
    normal_eyes = cmds.radioButton(
        label='normal', select=True, changeCommand=lambda x: action_radioButton(PriPos, CarPos, DiaPos, normal_eyes, abnormal_eyes, AmoutImages))
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.separator(height=10, style=None)
    abnormal_eyes = cmds.radioButton(
        label='abnormal', changeCommand=lambda x: action_radioButton(PriPos, CarPos, DiaPos, normal_eyes, abnormal_eyes, AmoutImages))
    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    # ------------ Setting for Primary  Position ------------
    framePriSetting = cmds.frameLayout('framePriSetting',
                                       label='Setting for Primary  Position', collapsable=False, enable=False)
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[
        (1, 400), (2, 400)], columnOffset=[(1, 'both', 3), (2, 'both', 3)])
    cmds.text('Right eye')
    cmds.text('Left eye')

    Pri_TypeofStrabismus_R = cmds.optionMenuGrp(
        'TypeofStrabismus_R', w=400, label="Type of Strabismus :")
    cmds.menuItem(label="Esotropia")
    cmds.menuItem(label="Exotropia")

    Pri_TypeofStrabismus_L = cmds.optionMenuGrp(
        'TypeofStrabismus_L', w=400, label="Type of Strabismus :")
    cmds.menuItem(label="Esotropia")
    cmds.menuItem(label="Exotropia")

    menuRight_H = cmds.optionMenuGrp('Right_H', w=400, label="Horizontal (X) :",
                                     extraLabel='degree', changeCommand=lambda x: setPreviewDegree(menuRight_H, menuLeft_H,
                                                                                                   Pri_TypeofStrabismus_R, Pri_TypeofStrabismus_L))
    cmds.menuItem(label="0")
    cmds.menuItem(label="15")
    cmds.menuItem(label="30")
    cmds.menuItem(label="45")

    menuLeft_H = cmds.optionMenuGrp('Left_H', w=400, label="Horizontal (X) :",
                                    extraLabel='degree', changeCommand=lambda x: setPreviewDegree(menuRight_H, menuLeft_H,
                                                                                                  Pri_TypeofStrabismus_R, Pri_TypeofStrabismus_L))
    cmds.menuItem(label="0")
    cmds.menuItem(label="15")
    cmds.menuItem(label="30")
    cmds.menuItem(label="45")

    cmds.setParent('..')
    cmds.setParent('..')

    # ------------ Setting for 9 diagnostic positions of gaze ------------

    frameDiaSetting = cmds.frameLayout('frameDiaSetting',
                                       label='Setting for 9 diagnostic positions of gaze', enable=False)
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 400), (2, 400), (3, 400)], columnOffset=[(1, 'both', 3), (2, 'both', 3), (3, 'both', 3)])
    frameCarSetting_r_ug = cmds.frameLayout(
        'frameCarSetting_r_ug', label='Right and up gaze')
    cmds.text('Right eye:')
    RU_R_Scale = cmds.intSliderGrp(field=True, label='RSR:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(RU_R_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_r_ug', RU_R_Scale, 'RU_R_Scale'))
    cmds.text('Left eye:')
    RU_L_Scale = cmds.intSliderGrp(field=True, label='LIO:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(RU_L_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_r_ug', RU_L_Scale, 'RU_L_Scale'))
    cmds.setParent('..')
    # ------------ Up gaze not use in cardinal of gaze ------------
    frameCarSetting_ug = cmds.frameLayout(
        'frameCarSetting_ug', label='Up gaze')
    cmds.text('Right eye:')
    Up_R_Scale = cmds.intSliderGrp(field=True, label='RSR/RIO:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(Up_R_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_ug', Up_R_Scale, 'Up_R_Scale'))
    cmds.text('Left eye:')
    Up_L_Scale = cmds.intSliderGrp(field=True, label='LIO/LSR:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(Up_L_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_ug', Up_L_Scale, 'Up_L_Scale'))
    cmds.setParent('..')

    frameCarSetting_l_ug = cmds.frameLayout(
        'frameCarSetting_l_ug', label='Left and up gaze')
    cmds.text('Right eye:')
    LU_R_Scale = cmds.intSliderGrp(field=True, label='RIO:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(LU_R_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_l_ug', LU_R_Scale, 'LU_R_Scale'))
    cmds.text('Left eye:')
    LU_L_Scale = cmds.intSliderGrp(field=True, label='LSR:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(LU_L_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_l_ug', LU_L_Scale, 'LU_L_Scale'))
    cmds.setParent('..')

    frameCarSetting_rg = cmds.frameLayout(
        'frameCarSetting_rg', label='Right gaze')
    cmds.text('Right eye:')
    RG_R_Scale = cmds.intSliderGrp(field=True, label='RLR:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(RG_R_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_rg', RG_R_Scale, 'RG_R_Scale'))
    cmds.text('Left eye:')
    RG_L_Scale = cmds.intSliderGrp(field=True, label='LMR:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(RG_L_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_rg', RG_L_Scale, 'RG_L_Scale'))
    cmds.setParent('..')

    # ------------ Start Primary not use in cardinal of gaze ------------
    frameCarSetting_pri = cmds.frameLayout(
        'frameCarSetting_pri', label='Primary Position')
    cmds.text('Right eye')
    TypeofStrabismus_R = cmds.optionMenuGrp(
        'TypeofStrabismus_R', w=400, label="Type of Strabismus :")
    cmds.menuItem(label="Esotropia")
    cmds.menuItem(label="Exotropia")

    cmds.optionMenuGrp('Right_H', w=400, label="Horizontal (X) :",
                       extraLabel='degree', changeCommand=lambda x: setPreviewDegree(menuRight_H, menuLeft_H,
                                                                                     Pri_TypeofStrabismus_R, Pri_TypeofStrabismus_L))
    cmds.menuItem(label="0")
    cmds.menuItem(label="15")
    cmds.menuItem(label="30")
    cmds.menuItem(label="45")

    cmds.text('Left eye')
    TypeofStrabismus_L = cmds.optionMenuGrp('TypeofStrabismus_L', w=400,
                                            label="Type of Strabismus :")
    cmds.menuItem(label="Esotropia")
    cmds.menuItem(label="Exotropia")

    cmds.optionMenuGrp('Left_H', w=400, label="Horizontal (X) :",
                       extraLabel='degree', changeCommand=lambda x: setPreviewDegree(menuRight_H, menuLeft_H,
                                                                                     Pri_TypeofStrabismus_R, Pri_TypeofStrabismus_L))
    cmds.menuItem(label="0")
    cmds.menuItem(label="15")
    cmds.menuItem(label="30")
    cmds.menuItem(label="45")
    cmds.setParent('..')
    # ------------ END Primary not use in cardinal of gaze ------------
    frameCarSetting_lg = cmds.frameLayout(
        'frameCarSetting_lg', label='Left gaze')
    cmds.text('Right eye:')
    LG_R_Scale = cmds.intSliderGrp(field=True, label='RMR:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(LG_R_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_lg', LG_R_Scale, 'LG_R_Scale'))
    cmds.text('Left eye:')
    LG_L_Scale = cmds.intSliderGrp(field=True, label='LLR:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(LG_L_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_lg', LG_L_Scale, 'LG_L_Scale'))
    cmds.setParent('..')
    frameCarSetting_r_dg = cmds.frameLayout(
        'frameCarSetting_r_dg', label='Right and down gaze')
    cmds.text('Right eye:')
    RD_R_Scale = cmds.intSliderGrp(field=True, label='RIR:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(RD_R_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_r_dg', RD_R_Scale, 'RD_R_Scale'))
    cmds.text('Left eye:')
    RD_L_Scale = cmds.intSliderGrp(field=True, label='LSO:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(RD_L_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_r_dg', RD_L_Scale, 'RD_L_Scale'))
    cmds.setParent('..')

    # ------------ Downgaze not use in cardinal of gaze ------------
    frameCarSetting_dg = cmds.frameLayout(
        'frameCarSetting_dg', label='Downgaze')
    cmds.text('Right eye:')
    D_R_Scale = cmds.intSliderGrp(field=True, label='IR/SO:', minValue=-4,
                                  maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(D_R_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_dg', D_R_Scale, 'D_R_Scale'))
    cmds.text('Left eye:')
    D_L_Scale = cmds.intSliderGrp(field=True, label='SO/IR:', minValue=-4,
                                  maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(D_L_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_dg', D_L_Scale, 'D_L_Scale'))
    cmds.setParent('..')
    frameCarSetting_l_dg = cmds.frameLayout(
        'frameCarSetting_l_dg', label='Left and down gaze')
    cmds.text('Right eye:')
    LD_R_Scale = cmds.intSliderGrp(field=True, label='RSO:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(LD_R_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_l_dg', LD_R_Scale, 'LD_R_Scale'))
    cmds.text('Left eye:')
    LD_L_Scale = cmds.intSliderGrp(field=True, label='LIR:', minValue=-4,
                                   maxValue=4, fieldMinValue=-4, fieldMaxValue=4, value=0)
    cmds.intSliderGrp(LD_L_Scale, e=True, changeCommand=lambda x: setPreviewSilderPositionOfGaze(
        'frameCarSetting_l_dg', LD_L_Scale, 'LD_L_Scale'))
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')

    # ------- Amount -------
    cmds.paneLayout(configuration='quad')
    cmds.frameLayout(label='Amount of Images')
    cmds.separator(height=5, style=None)
    cmds.rowColumnLayout(numberOfColumns=3, columnAttach=(
        (1, 'right', 3), (2, 'both', 3), (3, 'both', 3)), columnWidth=[(1, 200), (2, 150)])
    cmds.text(label='Amount:')
    AmoutImages = cmds.textField()

    cmds.iconTextButton(style='iconOnly', image1='help.xpm')
    cmds.separator(height=10, style=None)

    cmds.setParent('..')
    cmds.setParent('..')
    cmds.frameLayout(label='Create Lighting')
    cmds.optionMenuGrp('optionLighting', w=400, label="HDRIs :",
                       changeCommand=lambda x: apply_texture())
    cmds.menuItem(label="Outdoor")
    cmds.menuItem(label="Skies")
    cmds.menuItem(label="Indoor")
    cmds.menuItem(label="Studio")
    cmds.menuItem(label="Nature")
    cmds.menuItem(label="Urban")
    cmds.setParent('..')
    cmds.setParent('..')

    def applyButton(*args):
        # Abnormal Eyes
        if cmds.radioButton(abnormal_eyes, query=True, select=True) and cmds.radioButton(PriPos, query=True, select=True):
            setvaluePrimary(AmoutImages, menuRight_H, menuLeft_H,
                            Pri_TypeofStrabismus_R, Pri_TypeofStrabismus_L)
            loadWindowPreview_Abnormal(getAmountValue(AmoutImages))

        elif cmds.radioButton(abnormal_eyes, query=True, select=True) and cmds.radioButton(CarPos, query=True, select=True):
            getAmountFrame = setCardinalPositionOfGaze(setDefaultCardinal(RU_R_Scale, RU_L_Scale, LU_R_Scale, LU_L_Scale, RG_R_Scale,
                                                                          RG_L_Scale, LG_R_Scale, LG_L_Scale, RD_R_Scale, RD_L_Scale, LD_R_Scale, LD_L_Scale), AmoutImages)
            print('getAmountFrame', getAmountFrame[2])
            loadWindowPreview_Abnormal(
                getAmountFrame[0], getAmountFrame[1], getAmountFrame[2], AmoutImages)

        # elif cmds.radioButton(abnormal_eyes, query=True, select=True) and cmds.radioButton(DiaPos, query=True, select=True):
        #     setCardinalPositionOfGaze(collectValueCardinal(RU_R_Scale, RU_L_Scale, LU_R_Scale,
        #                                                    LU_L_Scale, RG_R_Scale, RG_L_Scale, LG_R_Scale, LG_L_Scale, RD_R_Scale, RD_L_Scale, LD_R_Scale, LD_L_Scale), AmoutImages)
        #     loadWindowPreview_Abnormal(getAmountValue(AmoutImages))

        # Normal Eyes
        elif cmds.radioButton(normal_eyes, query=True, select=True) and cmds.radioButton(PriPos, query=True, select=True):
            setNormalPositionOfGaze(AmoutImages)
            # loadWindowPreview_Normal(int(setNormalPositionOfGaze()))

        elif cmds.radioButton(normal_eyes, query=True, select=True) and cmds.radioButton(CarPos, query=True, select=True):
            getValue = setNormalCardinalPositionOfGaze(AmoutImages)
            print('getValue', getValue[2])
            loadWindowPreview_Abnormal(
                getValue[0], getValue[1], getValue[2], AmoutImages)
            # loadWindowPreview_Normal(int(setNormalCardinalPositionOfGaze()))

        elif cmds.radioButton(normal_eyes, query=True, select=True) and cmds.radioButton(DiaPos, query=True, select=True):
            getValueNine = setNinePositionOfGaze(AmoutImages)
            loadWindowPreview(
                getValueNine[0], getValueNine[1], getValueNine[2], AmoutImages)
            # loadWindowPreview_Normal(int(setNinePositionOfGaze()))

    def cancelCallback(*args):
        if cmds.window(window, exists=True):
            cmds.deleteUI(window)

    def render_seq(startframe=1, endframe=10, renderfn=cmds.render, renderfn_args=None):
        '''render out a sequence of frames as per global settings

        defaults to using maya.cmds.render for frames 1-10'''

        # save state
        now = cmds.currentTime(q=True)

        for x in range(startframe, endframe):
            cmds.currentTime(x)
            renderfn(renderfn_args)

        # restore state
        cmds.currentTime(now)

    # ------- Button -------
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[
        (1, 400), (2, 400), (3, 400)], columnOffset=[(1, 'both', 3), (2, 'both', 3), (3, 'both', 3)])
    cmds.button(label='Apply', height=40, command=applyButton)
    cmds.button(label='Render', command=render_seq)
    cmds.button(label='Close', command=cancelCallback)
    cmds.setParent('..')
    # display new window
    createLight()
    cmds.showWindow()


# create Lighting Skydome
def apply_texture():
    selectedMenuItem = cmds.optionMenuGrp('optionLighting', q=True, value=True)
    i = 0
    # create a shader
    shader = cmds.shadingNode("aiSkyDomeLight", asLight=True, n='shaderNode')
    # a file texture node
    file_node = cmds.shadingNode(
        "file", asTexture=True, n="fileTexture_%s" % i)
    # defines location where texture is
    file = ("C:/Users/Khunpang/Documents/GitHub/Ocular-Motility-Images-Dataset-Generating-System-with-3D-Model/" +
            "abandoned_" + selectedMenuItem+".hdr")
    # a shading group
    shading_group = cmds.sets(
        renderable=True, noSurfaceShader=True, empty=True)
    cmds.select('aiSkyDomeLight1')
    cmds.setAttr('%s.fileTextureName' % file_node, file, type="string")
    # connect shader to sg surface shader
    cmds.connectAttr('%s.outColor' %
                     shader, '%s.surfaceShader' % shading_group)
    # connect file texture node to shader's color
    cmds.connectAttr('%s.outColor' % file_node, '%s.color' % shader)
    i += 1


def createLight():
    if cmds.objExists('aiSkyDomeLight1'):
        cmds.select('aiSkyDomeLight1')

    else:
        skydome = mutils.createLocator('aiSkyDomeLight', asLight=True)
        print("Warning: no aiSkyDomeLight exists.")
        apply_texture()

# ------------------- set Preview Degree -------------------


def setPreviewDegree(menuRight_H, menuLeft_H, type_selected_R, type_selected_L):
    lstMenuitemDegree = getMenuitemDegree(menuRight_H, menuLeft_H)
    lstTypeOfStrabismus = getTypeOfStrabismus(type_selected_R, type_selected_L)
    # TypeofStrabismus_Right
    if lstTypeOfStrabismus[0] == 'Esotropia':  # Esotropia_R
        if lstMenuitemDegree[0] == '0':
            cmds.setAttr('ctrlEye_R.translateX', 0)
        elif lstMenuitemDegree[0] == '15':
            cmds.setAttr('ctrlEye_R.translateX', 0.22)
        elif lstMenuitemDegree[0] == '30':
            cmds.setAttr('ctrlEye_R.translateX', 0.59)
        elif lstMenuitemDegree[0] == '45':
            cmds.setAttr('ctrlEye_R.translateX', 1)
    if lstTypeOfStrabismus[0] == 'Exotropia':  # Exotropia_R
        if lstMenuitemDegree[0] == '0':
            cmds.setAttr('ctrlEye_R.translateX', 0)
        elif lstMenuitemDegree[0] == '15':
            cmds.setAttr('ctrlEye_R.translateX', -0.22)
        elif lstMenuitemDegree[0] == '30':
            cmds.setAttr('ctrlEye_R.translateX', -0.59)
        elif lstMenuitemDegree[0] == '45':
            cmds.setAttr('ctrlEye_R.translateX', -1)
    # TypeofStrabismus_Left
    if lstTypeOfStrabismus[1] == 'Esotropia':  # Esotropia_L
        if lstMenuitemDegree[1] == '0':
            cmds.setAttr('ctrlEye_L.translateX', 0)
        elif lstMenuitemDegree[1] == '15':
            cmds.setAttr('ctrlEye_L.translateX', -0.22)
        elif lstMenuitemDegree[1] == '30':
            cmds.setAttr('ctrlEye_L.translateX', -0.59)
        elif lstMenuitemDegree[1] == '45':
            cmds.setAttr('ctrlEye_L.translateX', -1)

    if lstTypeOfStrabismus[1] == 'Exotropia':  # Exotropia_L
        if lstMenuitemDegree[1] == '0':
            cmds.setAttr('ctrlEye_L.translateX', 0)
        elif lstMenuitemDegree[1] == '15':
            cmds.setAttr('ctrlEye_L.translateX', 0.22)
        elif lstMenuitemDegree[1] == '30':
            cmds.setAttr('ctrlEye_L.translateX', 0.59)
        elif lstMenuitemDegree[1] == '45':
            cmds.setAttr('ctrlEye_L.translateX', 1)

# ------------------- set Preview Silder Position Of Gaze -------------------


def setPreviewSilderPositionOfGaze(namesilder, ScaleSelected, nameSelected):
    lst_preview_cardinal = [[-1, 1], [0, 1], [1, 1],
                            [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
    lst_namesilder = ['frameCarSetting_r_ug', 'frameCarSetting_ug', 'frameCarSetting_l_ug', 'frameCarSetting_rg',
                      'frameCarSetting_lg', 'frameCarSetting_r_dg', 'frameCarSetting_dg', 'frameCarSetting_l_dg']
    findindex = lst_namesilder.index(namesilder)
    setGaze = lst_preview_cardinal[findindex]

    if '_R_' in nameSelected:
        cmds.setAttr('ctrlEye_R.translateX', setGaze[0])
        cmds.setAttr('ctrlEye_R.translateY', setGaze[1])
        if setGaze[0] < 0 and setGaze[1] >= 0:
            cmds.setAttr('AimEye_R.translateX',
                         getPreviewSliderValue(ScaleSelected)*(-1))
        elif setGaze[0] >= 0 or setGaze[1] >= 0:
            cmds.setAttr('AimEye_R.translateX',
                         getPreviewSliderValue(ScaleSelected))
        elif setGaze[0] >= 0 or setGaze[1] < 0:
            cmds.setAttr('AimEye_R.translateX',
                         getPreviewSliderValue(ScaleSelected)*(-1))

        print('yes R')
    elif '_L_' in nameSelected:
        cmds.setAttr('ctrlEye_L.translateX', setGaze[0])
        cmds.setAttr('ctrlEye_L.translateY', setGaze[1])
        if setGaze[0] < 0 and setGaze[1] >= 0:
            cmds.setAttr('AimEye_L.translateX',
                         getPreviewSliderValue(ScaleSelected)*(-1))
        elif setGaze[0] >= 0 or setGaze[1] >= 0:
            cmds.setAttr('AimEye_L.translateX',
                         getPreviewSliderValue(ScaleSelected))
        elif setGaze[0] > 0 or setGaze[1] < 0:
            cmds.setAttr('AimEye_L.translateX',
                         getPreviewSliderValue(ScaleSelected)*(-1))

        print('yes L')


def getPreviewSliderValue(ScaleSelected):
    getScale = cmds.intSliderGrp(ScaleSelected, query=True, value=True)
    return getScale

# ------------------- set Position Of Gaze (NORMAL) -------------------


def setNormalPositionOfGaze(textfieldAmount):
    amount = getAmountValue(textfieldAmount)
    value_noise = []

    for i in range(amount):
        cmds.setKeyframe('ctrlEye_R.translateX', at='tx', v=0, t=i+1)
        cmds.setKeyframe('ctrlEye_R.translateY', at='ty', v=0, t=i+1)
        cmds.setKeyframe('ctrlEye_L.translateX', at='tx', v=0, t=i+1)
        cmds.setKeyframe('ctrlEye_L.translateY', at='ty', v=0, t=i+1)

        value_noise.append(round(rand.uniform(-1, 1), 4))

        cmds.setKeyframe('AimEye_R.translateX', at='tx',
                         v=value_noise[i], t=i+1)
        cmds.setKeyframe('AimEye_L.translateX', at='ty',
                         v=value_noise[i], t=i+1)


lst_cardinal = [('Right Up', [-1, 1]), ('Left Up', [1, 1]), ('Right', [-1, 0]),
                ('Left', [1, 0]), ('Right Down', [-1, -1]), ('Left Down', [1, -1])]

lst_Nine = [('Right Up', [-1, 1]), ('Up gaze', [0, 1]), ('Left Up', [1, 1]), ('Right', [-1, 0]),
            ('Primary', [0, 0]), ('Left', [1, 0]), ('Right Down', [-1, -1]), ('Downgaze', [0, -1]), ('Left Down', [1, -1])]


def setNormalCardinalPositionOfGaze(textfieldAmount):
    amount = getAmountValue(textfieldAmount)
    value_noise = []
    lst_namegaze = []
    lst_scalegaze = []
    time_value = 0
    time_scale = 0
    for x, scale in lst_cardinal:
        for _ in range(amount):
            time_value += 1
            cmds.playbackOptions(edit=True, maxTime=time_value)
            cmds.setKeyframe('ctrlEye_R.translateX', at='tx',
                             v=scale[0], t=time_value)
            cmds.setKeyframe('ctrlEye_R.translateY', at='ty',
                             v=scale[1], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateX', at='tx',
                             v=scale[0], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateY', at='ty',
                             v=scale[1], t=time_value)

    for x, scale in lst_cardinal:
        # print(scale)
        for i in range(amount):
            lst_namegaze.append(x)
            time_scale += 1
            cmds.playbackOptions(edit=True, maxTime=time_value)
            value_noise.append(round(rand.uniform(-1, 1), 4))
            if 'Right' in x:
                scale_R_r = round(scale[0]*(-1)+value_noise[i], 4)
                scale_L_r = round(scale[1]*(-1)+value_noise[i], 4)
                all_scale_R_r = [scale, [scale_R_r, scale_L_r]]
                cmds.setKeyframe('AimEye_R.translateX',
                                 at='tx', v=scale_R_r, t=time_scale)
                cmds.setKeyframe('AimEye_L.translateX',
                                 at='tx', v=scale_L_r, t=time_scale)
                print('R', all_scale_R_r)
                lst_scalegaze.append(all_scale_R_r)
            elif 'Right' not in x:
                scale_R_l = round(scale[0]+value_noise[i], 4)
                scale_L_l = round(scale[1]+value_noise[i], 4)
                all_scale_R_l = [scale, [scale_R_l, scale_L_l]]
                cmds.setKeyframe('AimEye_R.translateX',
                                 at='tx', v=scale_R_l, t=time_scale)
                cmds.setKeyframe('AimEye_L.translateX',
                                 at='tx', v=scale_L_l, t=time_scale)
                print('L', all_scale_R_l)
                lst_scalegaze.append(all_scale_R_l)

    return time_value, lst_namegaze, lst_scalegaze


def setNinePositionOfGaze(textfieldAmount):
    amount = getAmountValue(textfieldAmount)
    value_noise = []
    lst_namegaze = []
    lst_scalegaze = []
    time_value = 0
    time_scale = 0
    all_scale_R_r = []
    all_scale_R_l = []
    for x, scale in lst_Nine:
        for _ in range(amount):
            time_value += 1
            cmds.playbackOptions(edit=True, maxTime=time_value)
            cmds.setKeyframe('ctrlEye_R.translateX', at='tx',
                             v=scale[0], t=time_value)
            cmds.setKeyframe('ctrlEye_R.translateY', at='ty',
                             v=scale[1], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateX', at='tx',
                             v=scale[0], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateY', at='ty',
                             v=scale[1], t=time_value)

    for x, scale in lst_Nine:
        # print(scale)
        for i in range(amount):
            lst_namegaze.append(x)
            time_scale += 1
            cmds.playbackOptions(edit=True, maxTime=time_value)
            value_noise.append(round(rand.uniform(-1, 1), 4))
            if 'Right' in x:
                scale_R_r = round(scale[0]*(-1)+value_noise[i], 4)
                scale_L_r = round(scale[1]*(-1)+value_noise[i], 4)
                all_scale_R_r = [scale, [scale_R_r, scale_L_r]]
                cmds.setKeyframe('AimEye_R.translateX',
                                 at='tx', v=scale_R_r, t=time_scale)
                cmds.setKeyframe('AimEye_L.translateX',
                                 at='tx', v=scale_L_r, t=time_scale)
                print('R', all_scale_R_r)
                lst_scalegaze.append(all_scale_R_r)
            elif 'Right' not in x:
                scale_R_l = round(scale[0]+value_noise[i], 4)
                scale_L_l = round(scale[1]+value_noise[i], 4)
                all_scale_R_l = [scale, [scale_R_l, scale_L_l]]
                cmds.setKeyframe('AimEye_R.translateX',
                                 at='tx', v=scale_R_l, t=time_scale)
                cmds.setKeyframe('AimEye_L.translateX',
                                 at='tx', v=scale_L_l, t=time_scale)
                print('L', all_scale_R_l)
                lst_scalegaze.append(all_scale_R_l)

    return time_value, lst_namegaze, lst_scalegaze

# def setNinePositionOfGaze(textfieldAmount):
#     amount = getAmountValue(textfieldAmount)

#     lst_Nine = [[-1, 1], [0, 1], [1, 1], [-1, 0],
#                 [0, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
#     value_noise = []
#     time_value = 0
#     time_scale = 0

#     for res in lst_Nine:
#         for _ in range(amount):
#             time_value += 1
#             cmds.setKeyframe('ctrlEye_R.translateX', at='tx',
#                              v=res[0], t=time_value)
#             cmds.setKeyframe('ctrlEye_R.translateY', at='ty',
#                              v=res[1], t=time_value)
#             cmds.setKeyframe('ctrlEye_L.translateX', at='tx',
#                              v=res[0], t=time_value)
#             cmds.setKeyframe('ctrlEye_L.translateY', at='ty',
#                              v=res[1], t=time_value)
#     for _ in lst_Nine:
#         for i in range(amount):
#             time_scale += 1
#             value_noise.append(round(rand.uniform(-1, 1), 4))
#             cmds.setKeyframe('AimEye_R.translateX', at='tx',
#                              v=value_noise[i], t=time_scale)
#             cmds.setKeyframe('AimEye_L.translateX', at='ty',
#                              v=value_noise[i], t=time_scale)
#     return str(len(lst_Nine))


# ----------------- set Position Of Gaze (ABNORMAL) -----------------


def getSliderValue(Scale_R, Scale_L):
    lst_scale = []
    getScale_R = cmds.intSliderGrp(Scale_R, query=True, value=True)
    getScale_L = cmds.intSliderGrp(Scale_L, query=True, value=True)
    lst_scale = [getScale_R, getScale_L]
    # print(lst_scale)
    return lst_scale


def setDefaultCardinal(Scale_R_1, Scale_L_1, Scale_R_2, Scale_L_2, Scale_R_3, Scale_L_3, Scale_R_4, Scale_L_4, Scale_R_5, Scale_L_5, Scale_R_6, Scale_L_6):
    value1 = getSliderValue(Scale_R_1, Scale_L_1)
    value2 = getSliderValue(Scale_R_2, Scale_L_2)
    value3 = getSliderValue(Scale_R_3, Scale_L_3)
    value4 = getSliderValue(Scale_R_4, Scale_L_4)
    value5 = getSliderValue(Scale_R_5, Scale_L_5)
    value6 = getSliderValue(Scale_R_6, Scale_L_6)
    thisdict = [
        ('Right Up', value1),
        ('Left Up', value2),
        ('Right', value3),
        ('Left', value4),
        ('Right Down', value5),
        ('Left Down', value6)
    ]
    return thisdict


# def setDefaultNine(Scale_R_1, Scale_L_1, Scale_R_2, Scale_L_2, thisdict):
#     value_up = (getSliderValue(Scale_R_1, Scale_L_1))
#     value_down = getSliderValue(Scale_R_2, Scale_L_2)
#     thisdict.insert(index, num)


def setCardinalPositionOfGaze(lst_ScaleSelected, textfieldAmount):
    amount = getAmountValue(textfieldAmount)
    lst_namegaze = []
    lst_scalegaze = []
    value_noise = []
    time_value = 0
    time_scale = 0
    all_scale_R_r = []
    all_scale_R_l = []

    for x, value in lst_cardinal:
        for _ in range(amount):
            # print(value)
            time_value += 1
            cmds.setKeyframe('ctrlEye_R.translateX', at='tx',
                             v=value[0], t=time_value)
            cmds.setKeyframe('ctrlEye_R.translateY', at='ty',
                             v=value[1], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateX', at='tx',
                             v=value[0], t=time_value)
            cmds.setKeyframe('ctrlEye_L.translateY', at='ty',
                             v=value[1], t=time_value)
            # set Scale Selected
    for x, scale in lst_ScaleSelected:

        for i in range(amount):
            lst_namegaze.append(x)
            # print(len(lst_namegaze))
            # print(x, scale[1])
            time_scale += 1
            cmds.playbackOptions(edit=True, maxTime=time_value)
            value_noise.append(round(rand.uniform(-1, 1), 4))
            # print(value_noise)
            if 'Right' in x:
                scale_R_r = round(scale[0]*(-1)+value_noise[i], 4)
                scale_L_r = round(scale[1]*(-1)+value_noise[i], 4)
                all_scale_R_r = [scale, [scale_R_r, scale_L_r]]
                print('R', all_scale_R_r)
                cmds.setKeyframe('AimEye_R.translateX',
                                 at='tx', v=scale_R_r, t=time_scale)
                cmds.setKeyframe('AimEye_L.translateX',
                                 at='tx', v=scale_L_r, t=time_scale)
                lst_scalegaze.append(all_scale_R_r)
            elif 'Right' not in x:
                scale_R_l = round(scale[0]+value_noise[i], 4)
                scale_L_l = round(scale[1]+value_noise[i], 4)
                all_scale_R_l = [scale, [scale_R_l, scale_L_l]]
                cmds.setKeyframe('AimEye_R.translateX',
                                 at='tx', v=scale_R_l, t=time_scale)
                cmds.setKeyframe('AimEye_L.translateX',
                                 at='tx', v=scale_L_l, t=time_scale)
                print('L', all_scale_R_l)
                lst_scalegaze.append(all_scale_R_l)

    return time_value, lst_namegaze, lst_scalegaze


# ------------------- get Degree -------------------


def getMenuitemDegree(menuRight_H, menuLeft_H):
    lstMenuitemDegree = []
    getDegree_RH = cmds.optionMenuGrp(menuRight_H, query=True, value=True)
    getDegree_LH = cmds.optionMenuGrp(menuLeft_H, query=True, value=True)
    lstMenuitemDegree = [getDegree_RH, getDegree_LH]
    print(lstMenuitemDegree)
    return lstMenuitemDegree


def getAmountValueNormal(textfieldAmount, positionofgaze):
    currentAmount = cmds.textField(
        textfieldAmount, edit=True, text=positionofgaze, editable=False)
    # print('Amount'+currentAmount)
    return currentAmount


def getAmountValue(textfieldAmount):
    currentAmount = cmds.textField(textfieldAmount, query=True, text=True)
    # print('Amount'+currentAmount)
    return int(currentAmount)


def loopNoiseRandom(textfieldAmount, min_v, max_v):
    amount = getAmountValue(textfieldAmount)
    cmds.playbackOptions(edit=True, maxTime=amount)
    # print(amount)
    lst = []
    for i in range(amount):
        lst.append(round(rand.uniform(min_v, max_v), 4))
        cmds.setKeyframe('AimEye_R.translateX', at='tx', v=lst[i], t=i+1)
        cmds.setKeyframe('AimEye_L.translateX', at='tx', v=lst[i], t=i+1)
    print(lst)


def getTypeOfStrabismus(type_selected_R, type_selected_L):
    TypeofStrabismus_R = cmds.optionMenuGrp(
        type_selected_R, query=True, value=True)
    TypeofStrabismus_L = cmds.optionMenuGrp(
        type_selected_L, query=True, value=True)
    lstTypeOfStrabismus = [TypeofStrabismus_R, TypeofStrabismus_L]
    # print(lstTypeOfStrabismus)
    return lstTypeOfStrabismus


def setvaluePrimary(textfieldAmount, menuRight_H, menuLeft_H, type_selected_R, type_selected_L):
    lstMenuitemDegree = getMenuitemDegree(menuRight_H, menuLeft_H)
    lstTypeOfStrabismus = getTypeOfStrabismus(type_selected_R, type_selected_L)
    # TypeofStrabismus_Right
    if lstTypeOfStrabismus[0] == 'Esotropia':  # Esotropia-ตาเขเข้า
        if lstMenuitemDegree[0] == '0':
            cmds.setAttr('ctrlEye_R.translateX', 0)
        elif lstMenuitemDegree[0] == '15':
            cmds.setAttr('ctrlEye_R.translateX', 0.22)
            loopNoiseRandom(textfieldAmount, 0, 1)
        elif lstMenuitemDegree[0] == '30':
            cmds.setAttr('ctrlEye_R.translateX', 0.59)
            loopNoiseRandom(textfieldAmount, 0, 1)
        elif lstMenuitemDegree[0] == '45':
            cmds.setAttr('ctrlEye_R.translateX', 1)
            loopNoiseRandom(textfieldAmount, 0, 1)
    if lstTypeOfStrabismus[0] == 'Exotropia':  # Exotropia-ตาเขออก
        if lstMenuitemDegree[0] == '0':
            cmds.setAttr('ctrlEye_R.translateX', 0)
        elif lstMenuitemDegree[0] == '15':
            cmds.setAttr('ctrlEye_R.translateX', -0.22)
            loopNoiseRandom(textfieldAmount, 0, -1)
        elif lstMenuitemDegree[0] == '30':
            cmds.setAttr('ctrlEye_R.translateX', -0.59)
            loopNoiseRandom(textfieldAmount, 0, -1)
        elif lstMenuitemDegree[0] == '45':
            cmds.setAttr('ctrlEye_R.translateX', -1)
            loopNoiseRandom(textfieldAmount, 0, -1)
    # TypeofStrabismus_Left
    if lstTypeOfStrabismus[1] == 'Esotropia':  # Esotropia-ตาเขเข้า
        if lstMenuitemDegree[1] == '0':
            cmds.setAttr('ctrlEye_L.translateX', 0)
        elif lstMenuitemDegree[1] == '15':
            cmds.setAttr('ctrlEye_L.translateX', -0.22)
            loopNoiseRandom(textfieldAmount, 0, -1)
        elif lstMenuitemDegree[1] == '30':
            cmds.setAttr('ctrlEye_L.translateX', -0.59)
            loopNoiseRandom(textfieldAmount, 0, -1)
        elif lstMenuitemDegree[1] == '45':
            cmds.setAttr('ctrlEye_L.translateX', -1)
            loopNoiseRandom(textfieldAmount, 0, -1)
    if lstTypeOfStrabismus[1] == 'Exotropia':  # Exotropia-ตาเขออก
        if lstMenuitemDegree[1] == '0':
            cmds.setAttr('ctrlEye_L.translateX', 0)
        elif lstMenuitemDegree[1] == '15':
            cmds.setAttr('ctrlEye_L.translateX', 0.22)
            loopNoiseRandom(textfieldAmount, 0, 1)
        elif lstMenuitemDegree[1] == '30':
            cmds.setAttr('ctrlEye_L.translateX', 0.59)
            loopNoiseRandom(textfieldAmount, 0, 1)
        elif lstMenuitemDegree[1] == '45':
            cmds.setAttr('ctrlEye_L.translateX', 1)
            loopNoiseRandom(textfieldAmount, 0, 1)


def playblastPreview():
    cmds.lookThru('camera1')
    cmds.lookThru(q=True)
    cmds.playblast(filename="C:/Users/Khunpang/Documents/maya/projects/mermaid/movies/mermaid_model_6",
                   format="image",
                   viewer=False,
                   compression="jpg",
                   clearCache=1,
                   fp=4,
                   percent=100,
                   quality=100,
                   widthHeight=[400, 80],
                   showOrnaments=False,
                   offScreen=True)


def loadWindowPreview(endframe, nameGaze, scaleGaze, textfieldAmount):

    def cancelCallback(*args):
        if cmds.window(window, exists=True):
            cmds.deleteUI(window)

    def render_seq(startframe=1, endframe=1, renderfn=cmds.render, renderfn_args=None):
        # save state
        now = cmds.currentTime(q=True)

        for x in range(startframe, endframe):
            cmds.currentTime(x)
            renderfn(renderfn_args)

        # restore state
        editor = 'renderView'
        formatManager = createImageFormats.ImageFormats()
        # formatManager.pushRenderGlobalsForDesc("JPEG")
        arnoldRender(1, 1, True, True, 'camera1', ' -layer defaultRenderLayer')

        cmds.setAttr("defaultArnoldDriver.ai_translator", "jpg", type="string")
        cmds.setAttr("defaultArnoldDriver.pre", "file_name", type="string")

        arnoldRender(400, 80, True, True, 'camera1',
                     ' -layer defaultRenderLayer')

        cmds.renderWindowEditor(
            editor, e=True, writeImage='C:/Users/Khunpang/Documents/maya/projects/mermaid/images/testImage.jpg')
        formatManager.popRenderGlobals()
        cmds.currentTime(now)

    amount = getAmountValue(textfieldAmount)
    size = (810, 400)
    # create new window
    window = cmds.window(title='Preview',
                         resizeToFitChildren=True, widthHeight=size, sizeable=False)

    form = cmds.formLayout()
    tabs = cmds.shelfTabLayout(
        'mainShelfTab', image='help.png', imageVisible=True)
    cmds.formLayout(form, edit=True, attachForm=(
        (tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 50), (tabs, 'right', 0)))

    for i in range(endframe):
        # cmds.shelfLayout('%s' % nameGaze[i], cellWidthHeight=[300, 50])
        if i % amount == 0:
            cmds.shelfLayout(
                '%s' % nameGaze[i], cellWidthHeight=[400, 80])
            for num in range(amount):
                # print(scaleGaze[i], scaleGaze[num])
                cmds.picture(
                    image=('C:/Users/Khunpang/Documents/maya/projects/mermaid/movies/mermaid_model_6.%04d.jpg' % (i+1)))
                cmds.text(('No. %d \n Right: %s Left: %s' % (num+1, scaleGaze[num+i][1][0], scaleGaze[num+i][1][1])),
                          font="boldLabelFont", align='center')
            cmds.setParent('..')

    cmds.setParent('..')
    ButtonRender = cmds.rowColumnLayout(numberOfColumns=2, columnOffset=(
        1, 'both', 5), columnWidth=[(1, 400), (2, 400)])
    cmds.button(label='Render', height=40, command=render_seq)
    cmds.button(label='Close', command=cancelCallback)
    cmds.formLayout(form, edit=True, attachForm=(
        (ButtonRender, 'top', 0), (ButtonRender, 'left', 0), (ButtonRender, 'bottom', 0), (ButtonRender, 'right', 0)), attachControl=(ButtonRender, 'top', 2, tabs))

    cmds.showWindow(window)


def loadWindowPreview_Normal(endframe, nameGaze, scaleGaze, amount):
    playblastPreview()
    loadWindowPreview(endframe, nameGaze, scaleGaze, amount)


def loadWindowPreview_Abnormal(endframe, nameGaze, scaleGaze, amount):
    playblastPreview()
    loadWindowPreview(endframe, nameGaze, scaleGaze, amount)


def buttonhelp():
    size = (400, 400)
    # create new window
    window = cmds.window(title='Help',
                         resizeToFitChildren=True, widthHeight=size, sizeable=False)
    cmds.columnLayout(adjustableColumn=True)
    cmds.picture(
        image=('C:/Users/Khunpang/Documents/maya/projects/mermaid/images/help/Cardinal Position.jpg'))
    cmds.showWindow(window)


def action_radioButton(PriPos, CarPos, DiaPos, normal_eyes, abnormal_eyes, textfieldAmount):
    # normal_eyes
    if cmds.radioButton(normal_eyes, query=True, select=True):
        if cmds.radioButton(PriPos, query=True, select=True):
            framePriSetting = cmds.frameLayout(
                'framePriSetting', edit=True, enable=False)
            frameDiaSetting = cmds.frameLayout(
                'frameDiaSetting', edit=True, enable=False)
            print("PriPos / normal_eyes")
        elif cmds.radioButton(CarPos, query=True, select=True):
            framePriSetting = cmds.frameLayout(
                'framePriSetting', edit=True, enable=False)
            frameDiaSetting = cmds.frameLayout(
                'frameDiaSetting', edit=True, enable=False)
            print("CarPos / normal_eyes")
        elif cmds.radioButton(DiaPos, query=True, select=True):
            framePriSetting = cmds.frameLayout(
                'framePriSetting', edit=True, enable=False)
            frameDiaSetting = cmds.frameLayout(
                'frameDiaSetting', edit=True, enable=False)
            print("DiaPos / normal_eyes")
    # abnormal_eyes
    elif cmds.radioButton(abnormal_eyes, query=True, select=True):
        # cmds.textField(
        #     textfieldAmount, editable=True, edit=True, text='')
        if cmds.radioButton(PriPos, query=True, select=True):
            framePriSetting = cmds.frameLayout(
                'framePriSetting', edit=True, enable=True)
            frameDiaSetting = cmds.frameLayout(
                'frameDiaSetting', edit=True, enable=False)
            print("PriPos / abnormal_eyes")
        elif cmds.radioButton(CarPos, query=True, select=True):
            framePriSetting = cmds.frameLayout(
                'framePriSetting', edit=True, enable=False)
            frameDiaSetting = cmds.frameLayout(
                'frameDiaSetting', edit=True, enable=True)
            frameCarSetting_r_ug = cmds.frameLayout(
                'frameCarSetting_r_ug', edit=True, enable=True)
            frameCarSetting_l_ug = cmds.frameLayout(
                'frameCarSetting_l_ug', edit=True, enable=True)
            frameCarSetting_rg = cmds.frameLayout(
                'frameCarSetting_rg', edit=True, enable=True)
            frameCarSetting_lg = cmds.frameLayout(
                'frameCarSetting_lg', edit=True, enable=True)
            frameCarSetting_r_dg = cmds.frameLayout(
                'frameCarSetting_r_dg', edit=True, enable=True)
            frameCarSetting_l_dg = cmds.frameLayout(
                'frameCarSetting_l_dg', edit=True, enable=True)
            frameCarSetting_ug = cmds.frameLayout(
                'frameCarSetting_ug', edit=True, enable=False)
            frameCarSetting_pri = cmds.frameLayout(
                'frameCarSetting_pri', edit=True, enable=False)
            frameCarSetting_dg = cmds.frameLayout(
                'frameCarSetting_dg', edit=True, enable=False)
            print("CarPos / abnormal_eyes")
        elif cmds.radioButton(DiaPos, query=True, select=True):
            framePriSetting = cmds.frameLayout(
                'framePriSetting', edit=True, enable=False)
            frameDiaSetting = cmds.frameLayout(
                'frameDiaSetting', edit=True, enable=True)
            frameCarSetting_r_ug = cmds.frameLayout(
                'frameCarSetting_r_ug', edit=True, enable=True)
            frameCarSetting_l_ug = cmds.frameLayout(
                'frameCarSetting_l_ug', edit=True, enable=True)
            frameCarSetting_rg = cmds.frameLayout(
                'frameCarSetting_rg', edit=True, enable=True)
            frameCarSetting_lg = cmds.frameLayout(
                'frameCarSetting_lg', edit=True, enable=True)
            frameCarSetting_r_dg = cmds.frameLayout(
                'frameCarSetting_r_dg', edit=True, enable=True)
            frameCarSetting_l_dg = cmds.frameLayout(
                'frameCarSetting_l_dg', edit=True, enable=True)
            frameCarSetting_ug = cmds.frameLayout(
                'frameCarSetting_ug', edit=True, enable=True)
            frameCarSetting_pri = cmds.frameLayout(
                'frameCarSetting_pri', edit=True, enable=True)
            frameCarSetting_dg = cmds.frameLayout(
                'frameCarSetting_dg', edit=True, enable=True)
            print("DiaPos / abnormal_eyes")
    else:
        print("No function")


if __name__ == "__main__":
    createUI('Ocular motility test images generating system')
