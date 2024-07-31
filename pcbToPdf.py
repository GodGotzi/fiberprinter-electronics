import sys
import os
import pcbnew

# Load the board
pcb_file = './printhead-pcb/printhead-pcb.kicad_pcb'
board = pcbnew.LoadBoard(pcb_file)
# input_directory = './printhead-pcb/printhead-pcb.kicad_pcb'  # Change this to the directory where your .kicad_sch files are located
# output_directory = './export/'  # Change this to your desired output directory

# Define output directory
output_dir = './export/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set up the plot controller
pctl = pcbnew.PLOT_CONTROLLER(board)
popt = pctl.GetPlotOptions()
popt.SetOutputDirectory(output_dir)
popt.SetPlotFrameRef(False)
popt.SetPlotValue(False)
popt.SetPlotReference(True)
popt.SetPlotInvisibleText(False)
popt.SetPlotPadsOnSilkLayer(True)
popt.SetExcludeEdgeLayer(True)
popt.SetMirror(False)
popt.SetNegative(False)
popt.SetUseAuxOrigin(False)
popt.SetLineWidth(pcbnew.FromMM(0.1))

# Define layers to plot
layers = [
    (pcbnew.F_Cu, "F_Cu"),
    (pcbnew.B_Cu, "B_Cu"),
    (pcbnew.F_SilkS, "F_SilkS"),
    (pcbnew.B_SilkS, "B_SilkS"),
    (pcbnew.F_Paste, "F_Paste"),
    (pcbnew.B_Paste, "B_Paste"),
    (pcbnew.F_SolderMask, "F_SolderMask"),
    (pcbnew.B_SolderMask, "B_SolderMask"),
    (pcbnew.Edge_Cuts, "Edge_Cuts")
]

for layer_info in layers:
    pctl.SetLayer(layer_info[0])
    pctl.OpenPlotfile(layer_info[1], pcbnew.PLOT_FORMAT_PDF, layer_info[1])
    pctl.PlotLayer()
    pctl.ClosePlot()

print(f"PDF files generated in {output_dir}")
