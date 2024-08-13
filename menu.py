#---------------------------------------
# menu.py
# Version: 1.0.1
# Last updated: 14/08/2024
# Ruben Mulas
#---------------------------------------


import nuke
import os
import platform
import nukescripts
import KnobScripter


# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:/Users/Ruben/.nuke'
Mac_Dir = '/Users/Ruben/.nuke'
Linux_Dir = '/home/Ruben/.nuke'

# Set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = Mac_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None





#-----------------------------------------------------------------------------------------
# DEFINITIONS ----------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

def closeAllProperties():
	for nodes in nuke.allNodes():
		nodes.hideControlPanel()


#-----------------------------------------------------------------------------------------
# SETTINGS -------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

menuSettings = nuke.menu('Nuke').addMenu('Utilities')

menuSettings.addCommand('Close all properties panels', lambda: closeAllProperties(), 'alt+x')
menuSettings.addCommand('Autocrop', 'nukescripts.autocrop()')


#-----------------------------------------------------------------------------------------
# CUSTOM NODES ---------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

menuNodes = nuke.menu('Nodes')

menuNodes.addCommand('Color/GradeAlpha', "nuke.createNode('Grade', 'white_clamp 1 channels alpha')", 'alt+g', icon="Grade.png", shortcutContext = 2)
menuNodes.addCommand('Color/Math/Multiply', "nuke.createNode('Multiply', '')", 'ctrl+m', icon="ColorMult.png", shortcutContext = 2)
menuNodes.addCommand('Merge/Merges/Merge_Mask', "nuke.createNode('Merge2', 'operation mask')", 'alt+m', icon="MergeOut.png", shortcutContext = 2)
menuNodes.addCommand('Merge/KeyMix', "nuke.createNode('Keymix', '')", 'ctrl+alt+x', icon="Keymix.png", shortcutContext = 2)
menuNodes.addCommand('Channel/ChannelMerge', "nuke.createNode('ChannelMerge', '')", 'alt+c', icon="ChannelMerge.png", shortcutContext = 2)
menuNodes.addCommand('Channel/Shuffle_White', lambda: nuke.createNode('Shuffle2', 'mappings "4 rgba.red 0 0 rgba.red 0 0 rgba.green 0 1 rgba.green 0 1 rgba.blue 0 2 rgba.blue 0 2 white -1 -1 rgba.alpha 0 3"'), 'ctrl+alt+s', icon="Shuffle.png", shortcutContext = 2)
menuNodes.addCommand('Transform/Tracker', "nuke.createNode('Tracker4', '')", 'ctrl+t', icon="Tracker.png", shortcutContext = 2)
menuNodes.addCommand('Time/FrameHold', "nuke.createNode('FrameHold', '')", 'ctrl+f', icon="FrameHold.png", shortcutContext = 2)


myNodesMenu = nuke.menu('Nodes').addMenu('rm nodes', icon=dir+"/icons/rm_icon.png")

myNodesMenu.addCommand("Additive/additivePlus", "nuke.nodePaste(\"" + os.path.join(dir + "/Tools/rm_additivePlus.nk") + "\")", shortcutContext = 2) 

#-----------------------------------------------------------------------------------------
# KNOB DEFAULT ---------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------


#nuke.knobDefault('Copy.bbox', '2')
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')
nuke.addOnUserCreate(lambda:nuke.thisNode()['keyframe_display'].setValue(3), nodeClass='Tracker4')
nuke.knobDefault("OFXuk.co.thefoundry.keylight.keylight_v201.show", "Intermediate Result")
nuke.knobDefault("RotoPaint.toolbox", '''clone {{ clone opc 0.1 }}''')
nuke.knobDefault("Blur.label", "[value size]")
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')

# ----- MOTION BLUR SHUTTER CENTERED ---------------------------
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")

