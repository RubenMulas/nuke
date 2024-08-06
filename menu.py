import nuke
import KnobScripter
import os
import platform


# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:/Users/Ruben\.nuke'
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





# DEFINICIONES -----------------------------------------------------------------

def closeAllProperties():
	for nodes in nuke.allNodes():
		nodes.hideControlPanel()

#SETTINGS ------------------------------------------------------------------------
	
nuke.menu('Nuke').addCommand('Ruben/Settings/Close all properties panels', lambda: closeAllProperties(), 'alt+x')
#nuke.menu('Nuke').addCommand("Ruben/Settings/Search Tracker", lambda: searchTracker.searchTracker(), 'alt+t')
#nuke.menu('Nuke').addCommand('Ruben/Settings/backdrop', lambda: GrayAutoBackdrop.GrayAutoBackdrop(), 'alt+b')
#nuke.menu('Nuke').addCommand('Ruben/Settings/Scale tree', lambda: W_scaleTree.scaleTreeFloatingPanel()', 'alt+shift+s`)


# KNOB DEFAULT ---------------------------------------------------------------------------
	
nuke.menu('Nuke').addCommand('Ruben/Nodes/GradeAlpha', lambda : nuke.createNode('Grade', 'white_clamp 1 channels alpha'), 'alt+g', shortcutContext = 2)
nuke.menu('Nuke').addCommand('Ruben/Nodes/Merge_Mask', lambda : nuke.createNode('Merge2', 'operation mask'), 'alt+m', shortcutContext = 2)
nuke.menu('Nuke').addCommand('Ruben/Nodes/Shuffle_White', lambda : nuke.createNode('Shuffle2', 'mappings "4 rgba.red 0 0 rgba.red 0 0 rgba.green 0 1 rgba.green 0 1 rgba.blue 0 2 rgba.blue 0 2 white -1 -1 rgba.alpha 0 3"'), 'ctrl+alt+s', shortcutContext = 2)
nuke.menu('Nuke').addCommand('Ruben/Nodes/Tracker', lambda : nuke.createNode('Tracker4', ''), 'ctrl+t', shortcutContext = 2)
nuke.menu('Nuke').addCommand('Ruben/Nodes/ChannelMerge', lambda : nuke.createNode('ChannelMerge', ''), 'alt+c', shortcutContext = 2)
nuke.menu('Nuke').addCommand('Ruben/Nodes/KeyMix', lambda : nuke.createNode('Keymix', ''), 'ctrl+alt+x', shortcutContext = 2)
nuke.menu('Nuke').addCommand('Ruben/Nodes/Multiply', lambda : nuke.createNode('Multiply', ''), 'ctrl+m', shortcutContext = 2)
nuke.menu('Nuke').addCommand('Ruben/Nodes/FrameHold', lambda : nuke.createNode('FrameHold', ''), 'ctrl+f', shortcutContext = 2)



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

