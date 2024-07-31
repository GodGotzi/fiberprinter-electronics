import os
import subprocess
from PyPDF2 import PdfMerger

# Define the directory containing the .kicad_sch files and the output directory for PDFs
input_directory = './pi-shield-pcb/'  # Change this to the directory where your .kicad_sch files are located
output_directory = './pi-shield-pcb-export/'  # Change this to your desired output directory

# Check if the directory exists
if not os.path.exists(output_directory):
    # Create the directory
    os.makedirs(output_directory)

# Function to delete file if it exists
def delete_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List of layers to include in the PDF export for PCB files
pcb_layers_V2 = [
    "F.Cu", "B.Cu", "F.Adhes", "B.Adhes", "F.Paste", "B.Paste",  
    "F.Mask", "B.Mask", "Edge.Cuts", "Margin", "In1.Cu", "In2.Cu", 
]
pcb_layers_V3 = [
    "F.Cu", "B.Cu", "F.Adhes", "B.Adhes", "F.Paste", "B.Paste", "F.SilkS", "B.SilkS",
    "F.Mask", "B.Mask", "Edge.Cuts", "Margin", "In1.Cu", "In2.Cu", 
]

# Function to run kicad-cli command for schematic files
def export_sch_to_pdf(input_file, output_file):
    command = ["kicad-cli", "sch", "export", "pdf", "-o", output_file, input_file]
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created PDF for schematic {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create PDF for schematic {input_file}: {e}")

# Function to run kicad-cli command for PCB files
def export_pcb_to_pdf(input_file, output_file):
    command = ["kicad-cli", "pcb", "export", "pdf", "-o", output_file, "--layers", ",".join(pcb_layers_V2), input_file]
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created PDF for PCB {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create PDF for PCB {input_file}: {e}")

def export_pcb_to_pdf_detailed(input_file, output_file):
    command = ["kicad-cli", "pcb", "export", "pdf", "-o", output_file, "--layers", ",".join(pcb_layers_V3), input_file]
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created PDF for PCB {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create PDF for PCB {input_file}: {e}")

# Function to run kicad-cli command for PCB files
def export_pcb_to_step(input_file, output_file):
    command = ["kicad-cli", "pcb", "export", "step", "-f", "--include-zones", "--include-tracks", "-o", output_file, input_file]
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created STEP for PCB {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create STEP for PCB {input_file}: {e}")

# Function to run kicad-cli command for BOM files
def export_bom(input_file, output_file):
    command = ["kicad-cli", "pcb", "export", "bom", "-o", output_file, input_file]
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created BOM for PCB {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create BOM for PCB {input_file}: {e}")

# Function to run kicad-cli command for DXF files
def export_pcb_to_dxf(input_file, output_file):
    command = ["kicad-cli", "pcb", "export", "dxf", "-o", output_file, "--layers", ",".join(pcb_layers_V3), input_file]
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created DXF for PCB {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create DXF for PCB {input_file}: {e}")

# Iterate over all files in the input directory
pdf_files = []
for filename in os.listdir(input_directory):
    if filename.endswith(".kicad_sch"):
        # Construct the input file path
        input_file = os.path.join(input_directory, filename)
        # Construct the output file path
        output_file = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.pdf")
        # Export schematic to PDF
        export_sch_to_pdf(input_file, output_file)
        # Collect the PDF files for merging
        pdf_files.append(output_file)
    
    elif filename.endswith(".kicad_pcb"):
        # Construct the input file path
        input_file = os.path.join(input_directory, filename)
        # Construct the output file path
        output_file = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.pdf")
        # Delete old file if it exists
        delete_if_exists(output_file)
        # Export PCB to PDF
        export_pcb_to_pdf(input_file, output_file)
        # Collect the PDF file for merging
        pdf_files.append(output_file)
        
        # Export detailed PDF Version
        # Construct the output file path
        output_file_detailed = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_detailed.pdf")
        # Delete old file if it exists
        delete_if_exists(output_file_detailed)
        # Export PCB to PDF
        export_pcb_to_pdf_detailed(input_file, output_file_detailed)
        # Collect the detailed PDF file for merging
        pdf_files.append(output_file_detailed)
        
        # Export STEP file
        # Construct the output file path
        output_file_step = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_step.step")
        # Delete old file if it exists
        delete_if_exists(output_file_step)
        # Export PCB to STEP
        export_pcb_to_step(input_file, output_file_step)

        # Export BOM file as CSV
        # Construct the output file path
        output_file_bom = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_bom.csv")
        # Delete old file if it exists
        delete_if_exists(output_file_bom)
        # Export BOM
        export_bom(input_file, output_file_bom)

        # Export to dxf
        # Construct the output file path
        output_file_dxf = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.dxf")
        # Delete old file if it exists
        delete_if_exists(output_file_dxf)
        # Export PCB to DXF



# Merge all PDF files into a single PDF
merger = PdfMerger()
for pdf_file in pdf_files:
    merger.append(pdf_file)

# Write the merged PDF to the output directory
merged_pdf_file = os.path.join(output_directory, "merged.pdf")
delete_if_exists(merged_pdf_file)
merger.write(merged_pdf_file)
merger.close()

print(f"Successfully merged all PDF files into {merged_pdf_file}")

print("All .kicad_sch and .kicad_pcb files processed.")

