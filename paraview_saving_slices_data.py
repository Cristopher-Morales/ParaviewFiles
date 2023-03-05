# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML MultiBlock Data Reader'
kenics_mixer_tutorialvtm = XMLMultiBlockDataReader(registrationName='kenics_mixer_tutorial.vtm', FileName=['/home/cristopher/Desktop/Documentation/Simulations/SU2_TUTORIAL_TRANSPORT_PROPERTIES/kenics_mixer_tutorial_SU2_website/TURBULENT/kenics_mixer_tutorial.vtm'])

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraFocalDisk = 1.0

# show data in view
kenics_mixer_tutorialvtmDisplay = Show(kenics_mixer_tutorialvtm, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
kenics_mixer_tutorialvtmDisplay.Representation = 'Surface'

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=renderView1, layout=layout1, hint=0)

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(kenics_mixer_tutorialvtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
kenics_mixer_tutorialvtmDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

Hide(kenics_mixer_tutorialvtm, renderView1)

# update the view to ensure updated data information
renderView1.Update()

position =[0.04, 0.09, 0.106667, 0.113333, 0.126667, 0.133333, 0.18, 0.24]

for x in position:
	# create a new 'Slice'
	slice1 = Slice(registrationName='Slice1', Input=kenics_mixer_tutorialvtm)
	# Properties modified on slice1.SliceType
	slice1.SliceType.Origin = [0.0, 0.0, x]
	slice1.SliceType.Normal = [0.0, 0.0, 1.0]
	# show data in view
	#slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')
	# trace defaults for the display properties.
	#slice1Display.Representation = 'Surface'
	# hide data in view
	# set scalar coloring
	#ColorBy(slice1Display, ('FIELD', 'vtkBlockColors'))
	# show color bar/color legend
	#slice1Display.SetScalarBarVisibility(renderView1, True)
	# create new layout object 'Layout #2'
	layout2 = CreateLayout(name='Layout #2')
	# set active view
	SetActiveView(None)
	# Create a new 'SpreadSheet View'
	spreadSheetView1 = CreateView('SpreadSheetView')
	spreadSheetView1.ColumnToSort = ''
	spreadSheetView1.BlockSize = 1024
	# show data in view
	slice1Display = Show(slice1, spreadSheetView1, 'SpreadSheetRepresentation')
	# assign view to a particular cell in the layout
	AssignViewToLayout(view=spreadSheetView1, layout=layout2, hint=0)
	# export view
	ExportView('/home/cristopher/x_'+str(x).split('.')[1]+'.csv', view=spreadSheetView1)
	# destroy spreadSheetView8
	Delete(spreadSheetView1)
	del spreadSheetView1
	RemoveLayout(layout2)
	Delete(slice1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
# layout1.SetSize(1337, 654)

# layout/tab size in pixels
# layout2.SetSize(400, 400)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
# renderView1.CameraPosition = [0.0, 0.0, 0.6352446761915185]
# renderView1.CameraFocalPoint = [0.0, 0.0, 0.12999999523162842]
# renderView1.CameraParallelScale = 0.13076694586916648

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
