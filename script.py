import os
import subprocess
from PyPDF2 import PdfMerger

# Define the directory containing the .kicad_sch files and the output directory for PDFs
input_directory = './printhead-pcb/'  # Change this to the directory where your .kicad_sch files are located
output_directory = './export/'  # Change this to your desired output directory

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

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
    command = ["kicad-cli", "pcb", "export", "pdf", "-o", output_file, input_file]
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
        # Export PCB to PDF
        export_pcb_to_pdf(input_file, output_file)
        # Collect the PDF files for merging
        pdf_files.append(output_file)
        # Export PCB to STEP
        # export_pcb_to_step(input_file, output_file)

# Merge all PDF files into a single PDF
merger = PdfMerger()
for pdf_file in pdf_files:
    merger.append(pdf_file)

# Write the merged PDF to the output directory
merged_pdf_file = os.path.join(output_directory, "merged.pdf")
merger.write(merged_pdf_file)
merger.close()

print(f"Successfully merged all PDF files into {merged_pdf_file}")

print("All .kicad_sch and .kicad_pcb files processed.")

