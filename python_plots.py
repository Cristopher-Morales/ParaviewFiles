# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# set active view
SetActiveView(renderView1)

# split cell
layout1.SplitHorizontal(1, 0.5)

# set active view
SetActiveView(None)

# split cell
layout1.SplitHorizontal(2, 0.5)

# set active view
SetActiveView(renderView1)

# split cell
layout1.SplitVertical(3, 0.5)

# set active view
SetActiveView(None)

# split cell
layout1.SplitVertical(4, 0.5)

# split cell
layout1.SplitVertical(5, 0.5)

# split cell
layout1.SplitVertical(6, 0.5)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraFocalDisk = 1.0

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView2, layout=layout1, hint=9)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraFocalDisk = 1.0

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView3, layout=layout1, hint=11)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraFocalDisk = 1.0

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView4, layout=layout1, hint=13)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView5 = CreateView('RenderView')
renderView5.AxesGrid = 'GridAxes3DActor'
renderView5.StereoType = 'Crystal Eyes'
renderView5.CameraFocalDisk = 1.0

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView5, layout=layout1, hint=8)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView6 = CreateView('RenderView')
renderView6.AxesGrid = 'GridAxes3DActor'
renderView6.StereoType = 'Crystal Eyes'
renderView6.CameraFocalDisk = 1.0

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView6, layout=layout1, hint=10)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView7 = CreateView('RenderView')
renderView7.AxesGrid = 'GridAxes3DActor'
renderView7.StereoType = 'Crystal Eyes'
renderView7.CameraFocalDisk = 1.0

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView7, layout=layout1, hint=12)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView8 = CreateView('RenderView')
renderView8.AxesGrid = 'GridAxes3DActor'
renderView8.StereoType = 'Crystal Eyes'
renderView8.CameraFocalDisk = 1.0

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView8, layout=layout1, hint=14)

# set active view
SetActiveView(renderView1)

# create a new 'XML MultiBlock Data Reader'
kenics_mixer_tutorialvtm = XMLMultiBlockDataReader(registrationName='kenics_mixer_tutorial.vtm', FileName=['/home/cristopher/Desktop/Documentation/Simulations/SU2_TUTORIAL_TRANSPORT_PROPERTIES/CASE_TWISTED/TURBULENT/RESULTS_2/TURBULENT/kenics_mixer_tutorial.vtm'])

#array of slice

position = [0.04, 0.09, 0.106667, 0.113333, 0.126667, 0.133333, 0.18, 0.24]

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=kenics_mixer_tutorialvtm)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, position[0]]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False)

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.050000000745]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.15000000074505806]

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, False)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'Species_0'))

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# update the view to ensure updated data information
renderView1.Update()
# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=kenics_mixer_tutorialvtm)

# Properties modified on slice1.SliceType
slice2.SliceType.Origin = [0.0, 0.0, position[1]]
slice2.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice2Display = Show(slice2, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'

# reset view to fit data
renderView2.ResetCamera(False)

#changing interaction mode based on data extents
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [0.0, 0.0, 10000.050000000745]
renderView2.CameraFocalPoint = [0.0, 0.0, 0.15000000074505806]

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView2, True)

# set scalar coloring
ColorBy(slice2Display, ('POINTS', 'Species_0'))

# Hide orientation axes
renderView2.OrientationAxesVisibility = 0
# update the view to ensure updated data information
renderView2.Update()

# create a new 'Slice'
slice3 = Slice(registrationName='Slice3', Input=kenics_mixer_tutorialvtm)

# Properties modified on slice1.SliceType
slice3.SliceType.Origin = [0.0, 0.0, position[2]]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice3Display = Show(slice3, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
slice3Display.Representation = 'Surface'

# reset view to fit data
renderView3.ResetCamera(False)

#changing interaction mode based on data extents
renderView3.InteractionMode = '2D'
renderView3.CameraPosition = [0.0, 0.0, 10000.050000000745]
renderView3.CameraFocalPoint = [0.0, 0.0, 0.15000000074505806]

# show color bar/color legend
slice3Display.SetScalarBarVisibility(renderView3, True)

# set scalar coloring
ColorBy(slice3Display, ('POINTS', 'Species_0'))

# Hide orientation axes
renderView3.OrientationAxesVisibility = 0
# update the view to ensure updated data information
renderView3.Update()

# create a new 'Slice'
slice4 = Slice(registrationName='Slice4', Input=kenics_mixer_tutorialvtm)

# Properties modified on slice1.SliceType
slice4.SliceType.Origin = [0.0, 0.0, position[3]]
slice4.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice4Display = Show(slice4, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
slice4Display.Representation = 'Surface'

# reset view to fit data
renderView4.ResetCamera(False)

#changing interaction mode based on data extents
renderView4.InteractionMode = '2D'
renderView4.CameraPosition = [0.0, 0.0, 10000.050000000745]
renderView4.CameraFocalPoint = [0.0, 0.0, 0.15000000074505806]

# show color bar/color legend
slice4Display.SetScalarBarVisibility(renderView4, True)

# set scalar coloring
ColorBy(slice4Display, ('POINTS', 'Species_0'))

# Hide orientation axes
renderView4.OrientationAxesVisibility = 0
# update the view to ensure updated data information
renderView4.Update()

# create a new 'Slice'
slice5 = Slice(registrationName='Slice5', Input=kenics_mixer_tutorialvtm)

# Properties modified on slice1.SliceType
slice5.SliceType.Origin = [0.0, 0.0, position[4]]
slice5.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice5Display = Show(slice5, renderView5, 'GeometryRepresentation')

# trace defaults for the display properties.
slice5Display.Representation = 'Surface'

# reset view to fit data
renderView5.ResetCamera(False)

#changing interaction mode based on data extents
renderView5.InteractionMode = '2D'
renderView5.CameraPosition = [0.0, 0.0, 10000.050000000745]
renderView5.CameraFocalPoint = [0.0, 0.0, 0.15000000074505806]

# show color bar/color legend
slice5Display.SetScalarBarVisibility(renderView5, True)

# set scalar coloring
ColorBy(slice5Display, ('POINTS', 'Species_0'))

# Hide orientation axes
renderView5.OrientationAxesVisibility = 1
# update the view to ensure updated data information
renderView5.Update()

# create a new 'Slice'
slice6 = Slice(registrationName='Slice6', Input=kenics_mixer_tutorialvtm)

# Properties modified on slice1.SliceType
slice6.SliceType.Origin = [0.0, 0.0, position[5]]
slice6.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice6Display = Show(slice6, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
slice6Display.Representation = 'Surface'

# reset view to fit data
renderView6.ResetCamera(False)

#changing interaction mode based on data extents
renderView6.InteractionMode = '2D'
renderView6.CameraPosition = [0.0, 0.0, 10000.050000000745]
renderView6.CameraFocalPoint = [0.0, 0.0, 0.15000000074505806]

# show color bar/color legend
slice6Display.SetScalarBarVisibility(renderView6, True)

# set scalar coloring
ColorBy(slice6Display, ('POINTS', 'Species_0'))

# Hide orientation axes
renderView6.OrientationAxesVisibility = 0
# update the view to ensure updated data information
renderView6.Update()

# create a new 'Slice'
slice7 = Slice(registrationName='Slice7', Input=kenics_mixer_tutorialvtm)

# Properties modified on slice1.SliceType
slice7.SliceType.Origin = [0.0, 0.0, position[6]]
slice7.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice7Display = Show(slice7, renderView7, 'GeometryRepresentation')

# trace defaults for the display properties.
slice7Display.Representation = 'Surface'

# reset view to fit data
renderView7.ResetCamera(False)

#changing interaction mode based on data extents
renderView7.InteractionMode = '2D'
renderView7.CameraPosition = [0.0, 0.0, 10000.050000000745]
renderView7.CameraFocalPoint = [0.0, 0.0, 0.15000000074505806]

# show color bar/color legend
slice7Display.SetScalarBarVisibility(renderView7, True)

# set scalar coloring
ColorBy(slice7Display, ('POINTS', 'Species_0'))

# Hide orientation axes
renderView7.OrientationAxesVisibility = 0
# update the view to ensure updated data information
renderView7.Update()

# create a new 'Slice'
slice8 = Slice(registrationName='Slice8', Input=kenics_mixer_tutorialvtm)

# Properties modified on slice1.SliceType
slice8.SliceType.Origin = [0.0, 0.0, position[7]]
slice8.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice8Display = Show(slice8, renderView8, 'GeometryRepresentation')

# trace defaults for the display properties.
slice8Display.Representation = 'Surface'

# reset view to fit data
renderView8.ResetCamera(False)

#changing interaction mode based on data extents
renderView8.InteractionMode = '2D'
renderView8.CameraPosition = [0.0, 0.0, 10000.050000000745]
renderView8.CameraFocalPoint = [0.0, 0.0, 0.15000000074505806]

# show color bar/color legend
slice8Display.SetScalarBarVisibility(renderView8, True)

# set scalar coloring
ColorBy(slice8Display, ('POINTS', 'Species_0'))

# Hide orientation axes
renderView8.OrientationAxesVisibility = 0

# show color bar/color legend
slice8Display.SetScalarBarVisibility(renderView8, True)

# get color transfer function/color map for 'Species_0'
species_0LUT = GetColorTransferFunction('Species_0')

# get opacity transfer function/opacity map for 'Species_0'
species_0PWF = GetOpacityTransferFunction('Species_0')

# get color legend/bar for species_0LUT in view renderView8
species_0LUTColorBar = GetScalarBar(species_0LUT, renderView8)

# change scalar bar placement
species_0LUTColorBar.Orientation = 'Horizontal'
species_0LUTColorBar.WindowLocation = 'Any Location'
species_0LUTColorBar.Position = [0.1377914110429446, 0.03145631067961169]
species_0LUTColorBar.ScalarBarLength = 0.7410429447852764

# Properties modified on species_0LUTColorBar
species_0LUTColorBar.Title = 'Mass Fraction CH4'

# update the view to ensure updated data information
renderView8.Update()

# link cameras in two views
AddCameraLink(renderView2, renderView1, 'CameraLink0')

# link cameras in two views
AddCameraLink(renderView3, renderView1, 'CameraLink1')

# link cameras in two views
AddCameraLink(renderView4, renderView1, 'CameraLink2')

# link cameras in two views
AddCameraLink(renderView5, renderView1, 'CameraLink3')

# link cameras in two views
AddCameraLink(renderView6, renderView1, 'CameraLink4')

# link cameras in two views
AddCameraLink(renderView7, renderView1, 'CameraLink5')

# link cameras in two views
AddCameraLink(renderView8, renderView1, 'CameraLink6')

# set active view
SetActiveView(renderView1)

# rescale color and/or opacity maps used to exactly fit the current data range
slice1Display.RescaleTransferFunctionToDataRange(False, True)

# rescale color and/or opacity maps used to exactly fit the current data range
slice1Display.RescaleTransferFunctionToDataRange(False, True)

# Rescale transfer function
species_0LUT.RescaleTransferFunction(0.0, 1.0)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1310, 654)

#--------------------------------------------
# uncomment the following to render all views
#RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
# save screenshot
