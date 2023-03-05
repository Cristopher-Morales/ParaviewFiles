# trace generated using paraview version 5.10.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import os 
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

names =[]
positions =[1e-05, 0.25999]
for folders in os.listdir('/home/cristopher/Desktop/Documentation/Simulations/SU2_TUTORIAL_TRANSPORT_PROPERTIES/kenics_mixer_optimization_two_boxes_without_edges/optimization'):
	x= str(folders)
	if (x.split("_")[0]=='DSN'):
        	names.append(x)
# create a new 'XML Unstructured Grid Reader'
for name in names:
	i = 0;
	for position in positions:
		internalvtu = XMLUnstructuredGridReader(registrationName='Internal.vtu', FileName=['/home/cristopher/Desktop/Documentation/Simulations/SU2_TUTORIAL_TRANSPORT_PROPERTIES/kenics_mixer_optimization_two_boxes_without_edges/optimization/'+name+'/DIRECT/kenics_mixer_tutorial/zone_0/Internal.vtu'])

		# Properties modified on internalvtu
		internalvtu.TimeArray = 'None'

		# get active view
		renderView1 = GetActiveViewOrCreate('RenderView')

		# show data in view
		internalvtuDisplay = Show(internalvtu, renderView1, 'UnstructuredGridRepresentation')

		# trace defaults for the display properties.
		internalvtuDisplay.Representation = 'Surface'

		# reset view to fit data
		renderView1.ResetCamera(False)

		# update the view to ensure updated data information
		renderView1.Update()

		# create a new 'Slice'
		slice1 = Slice(registrationName='Slice1', Input=internalvtu)

		# Properties modified on slice1.SliceType
		slice1.SliceType.Origin = [0.0, 0.0, float(position)]
		slice1.SliceType.Normal = [0.0, 0.0, 1.0]

		# show data in view
		slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

		# trace defaults for the display properties.
		slice1Display.Representation = 'Surface'

		# hide data in view
		Hide(internalvtu, renderView1)

		# update the view to ensure updated data information
		renderView1.Update()

		# create a new 'Generate Surface Normals'
		generateSurfaceNormals1 = GenerateSurfaceNormals(registrationName='GenerateSurfaceNormals1', Input=slice1)

		# show data in view
		generateSurfaceNormals1Display = Show(generateSurfaceNormals1, renderView1, 'GeometryRepresentation')

		# trace defaults for the display properties.
		generateSurfaceNormals1Display.Representation = 'Surface'

		# hide data in view
		Hide(slice1, renderView1)

		# update the view to ensure updated data information
		renderView1.Update()

		# create a new 'Calculator'
		calculator1 = Calculator(registrationName='Calculator1', Input=generateSurfaceNormals1)

		# Properties modified on calculator1
		calculator1.Function = '(Pressure +0.5*Density*((Velocity_X*Velocity_X)+(Velocity_Y*Velocity_Y)+(Velocity_Z*Velocity_Z)))*Normals'

		# show data in view
		calculator1Display = Show(calculator1, renderView1, 'GeometryRepresentation')

		# trace defaults for the display properties.
		calculator1Display.Representation = 'Surface'

		# hide data in view
		Hide(generateSurfaceNormals1, renderView1)

		# update the view to ensure updated data information
		renderView1.Update()

		# create a new 'Integrate Variables'
		integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=calculator1)

		# Create a new 'SpreadSheet View'
		spreadSheetView1 = CreateView('SpreadSheetView')
		spreadSheetView1.ColumnToSort = ''
		spreadSheetView1.BlockSize = 1024

		# show data in view
		integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

		# get layout
		layout1 = GetLayoutByName("Layout #1")

		# add view to a layout so it's visible in UI
		AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

		# Properties modified on integrateVariables1Display
		integrateVariables1Display.Assembly = ''

		# update the view to ensure updated data information
		spreadSheetView1.Update()

		# create a new 'Calculator'
		calculator2 = Calculator(registrationName='Calculator2', Input=integrateVariables1)

		# Properties modified on calculator2
		if (i==0):
			calculator2.ResultArrayName = 'Surface_Total_Pressure_Inlet'
		else:
			calculator2.ResultArrayName = 'Surface_Total_Pressure_Outlet'
		calculator2.Function = 'Result_Z/Normals_Z'

		# show data in view
		calculator2Display = Show(calculator2, spreadSheetView1, 'SpreadSheetRepresentation')

		# hide data in view
		Hide(integrateVariables1, spreadSheetView1)

		# update the view to ensure updated data information
		spreadSheetView1.Update()

		# Properties modified on calculator2Display
		calculator2Display.Assembly = ''

		# get active source.
		calculator2 = GetActiveSource()

		# set active source
		SetActiveSource(calculator2)

		# get active view
		spreadSheetView1 = GetActiveViewOrCreate('SpreadSheetView')

		# export view
		if (i==0):
			ExportView('/home/cristopher/Desktop/Documentation/results_optimization/kenics_mixer_optimization_two_boxes_without_edges/pressure/pressure_inlet_'+str(int(name.split("_")[1]))+'.csv', view=spreadSheetView1)
			i=i+1
		else:
			ExportView('/home/cristopher/Desktop/Documentation/results_optimization/kenics_mixer_optimization_two_boxes_without_edges/pressure/pressure_outlet_'+str(int(name.split("_")[1]))+'.csv', view=spreadSheetView1)
		Delete(spreadSheetView1)
		del spreadSheetView1
		RemoveLayout(layout1)
		Delete(slice1)
		Delete(generateSurfaceNormals1)
		Delete(calculator1)
		Delete(calculator2)
		Delete(integrateVariables1)
		Delete(internalvtu)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1075, 654)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 0.6352446761915185]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.12999999523162842]
renderView1.CameraParallelScale = 0.13076694586916648

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
