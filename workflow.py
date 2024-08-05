import os
import subprocess
import shutil

dirs = ["printhead-pcb", "pi-shield-pcb"]

# Make sure output directory gets freshly created
if os.path.exists("export"):
    shutil.rmtree("export")
    print("Deleted existing export directory.")
os.makedirs("export")

# Make sure the input directory exists
def make_input_directory(dir, ending):
    input_filename = dir + ending
    input_directory = os.path.join(dir, input_filename)
    if not os.path.exists(input_directory):
        print(f"Error: The directory {input_directory} does not exist.")
    return input_directory

# Make sure the output directory is freshly created
def make_output_directory(dir, filename):
    dir = os.path.join("export", dir)
    if not os.path.exists(dir):
        os.makedirs(dir)
    dir = os.path.join(dir, filename)
    if os.path.exists(dir):
        os.remove(dir)
    return dir

pcb_layers = [
    "F.Cu", "B.Cu", "F.Adhes", "B.Adhes", "F.Paste", "B.Paste",
    "F.Mask", "B.Mask", "Edge.Cuts", "Margin", "In1.Cu", "In2.Cu",
    "In3.Cu", "In4.Cu", "In5.Cu", "In6.Cu", "In7.Cu", "In8.Cu",
    "In9.Cu", "In10.Cu", "In11.Cu", "In12.Cu", "In13.Cu", "In14.Cu",
    "In15.Cu", "In16.Cu", "Dwgs.User", "Cmts.User", "Eco1.User",
    "Eco2.User", "B.Fab", "F.Fab", "B.SilkS", "F.SilkS", "B.CrtYd",
    "F.CrtYd"
]

# Generic function to run kicad-cli command
def run_kicad_cli_command(command_type, file_type, input_file, output_file, *args):
    command = ["kicad-cli", file_type, "export", command_type, "-o", output_file] + list(args) + [input_file]
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created {command_type.upper()} for {file_type.upper()} {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create {command_type.upper()} for {file_type.upper()} {input_file}: {e}")

# Function to run kicad-cli command for schematic files
def export_sch_to_pdf(dir, filename):
    input_file = make_input_directory(dir, ".kicad_sch")
    output_file = make_output_directory(dir, filename)
    print(input_file + " -> " + output_file)
    run_kicad_cli_command("pdf", "sch", input_file, output_file)

# Function to run kicad-cli command for BOM files
def export_sch_to_bom(dir, filename):
    input_file = make_input_directory(dir, ".kicad_sch")
    output_file = make_output_directory(dir, filename)
    run_kicad_cli_command("bom", "sch", input_file, output_file)

# Function to run kicad-cli command for PCB files
def export_pcb_to_pdf(dir, filename):
    # Define configurations for different PDF exports
    configs = [
        {"suffix": "pcb-", "exclude_layers": []},
        {"suffix": "front-", "exclude_layers": ["B."]},
        {"suffix": "back-", "exclude_layers": ["F."]},
        {"suffix": "back-mirrored-", "exclude_layers": ["F."], "mirror": True},
        {"suffix": "front-noCrtYd-", "exclude_layers": ["CrtYd"]},
        {"suffix": "front-noCrtYd-noSilkS-", "exclude_layers": ["CrtYd", "SilkS"]},
        {"suffix": "front-noCrtYd-noSilkS-noFab-", "exclude_layers": ["CrtYd", "SilkS", "Fab"]},
    ]

    for config in configs:
        # Prepare output file name and filter pcb_layers
        output_file_suffix = config["suffix"] + filename
        output_file = make_output_directory(dir, output_file_suffix)
        filtered_layers = [layer for layer in pcb_layers if all(sub not in layer for sub in config["exclude_layers"])]

        # Construct command arguments
        command_args = ["pdf", "pcb", make_input_directory(dir, ".kicad_pcb"), output_file, "--layers", ",".join(filtered_layers), "--exclude-value", "--exclude-refdes", "--include-border-title"]
        if config.get("mirror"):
            command_args.append("--mirror")

        # Execute the command
        run_kicad_cli_command(*command_args)

# Function to run kicad-cli command for PCB files to STEP
def export_pcb_to_step(dir, filename):
    input_file = make_input_directory(dir, ".kicad_pcb")
    output_file = make_output_directory(dir, filename)
    run_kicad_cli_command("step", "pcb", input_file, output_file, "-f", "--include-zones", "--include-tracks")

# Function to run kicad-cli command for PCB files to DXF
def export_pcb_to_dxf(dir, filename):
    input_file = make_input_directory(dir, ".kicad_pcb")
    output_file = make_output_directory(dir, filename)
    run_kicad_cli_command("dxf", "pcb", input_file, output_file, "--layers", ",".join(pcb_layers))

for dir in dirs:
    export_sch_to_pdf(dir, "schematic.pdf")
    export_sch_to_bom(dir, "bom.csv")
    export_pcb_to_pdf(dir, "pcb.pdf")
    export_pcb_to_step(dir, "pcb.step")
    export_pcb_to_dxf(dir, "pcb.dxf")

print("All .kicad_sch and .kicad_pcb files processed.")

