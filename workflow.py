import os
import subprocess
import shutil

dirs = ["printhead-pcb", "pi-shield-pcb", "2nd-mainboard-pcb"]

# Make sure output directory gets freshly created
if os.path.exists("export"):
    shutil.rmtree("export")
    print("Deleted existing export directory.")
os.makedirs("export")


def make_input_directory(dir, ending):
    input_filename = dir + ending
    input_directory = os.path.join(dir, input_filename)
    if not os.path.exists(input_directory):
        print(f"Error: The file {input_directory} does not exist.")
        return None
    return input_directory


def make_output_directory(dir, filename):
    dir = os.path.join("export", dir)
    os.makedirs(dir, exist_ok=True)  # Sicherstellen, dass das Verzeichnis existiert
    file_path = os.path.join(dir, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return file_path


pcb_layers = [
    "F.Cu", "B.Cu", "F.Adhes", "B.Adhes", "F.Paste", "B.Paste",
    "F.Mask", "B.Mask", "Edge.Cuts", "Margin", "In1.Cu", "In2.Cu",
    "In3.Cu", "In4.Cu", "In5.Cu", "In6.Cu", "In7.Cu", "In8.Cu",
    "In9.Cu", "In10.Cu", "In11.Cu", "In12.Cu", "In13.Cu", "In14.Cu",
    "In15.Cu", "In16.Cu", "Dwgs.User", "Cmts.User", "Eco1.User",
    "Eco2.User", "B.Fab", "F.Fab", "B.SilkS", "F.SilkS", "B.CrtYd",
    "F.CrtYd"
]


def run_kicad_cli_command(command_type, file_type, input_file, output_file, *args):
    if input_file is None or output_file is None:
        print(f"Skipping {command_type.upper()} for {file_type.upper()} due to missing input/output file.")
        return

    command = ["kicad-cli", file_type, "export", command_type, "-o", output_file] + list(args) + [input_file]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Successfully created {command_type.upper()} for {file_type.upper()} {input_file}")
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to create {command_type.upper()} for {file_type.upper()} {input_file}: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")


def export_sch_to_pdf(dir, filename):
    input_file = make_input_directory(dir, ".kicad_sch")
    output_file = make_output_directory(dir, filename)
    
    if input_file is None:
        return  
    
    run_kicad_cli_command("pdf", "sch", input_file, output_file)


def export_sch_to_bom(dir, filename):
    input_file = make_input_directory(dir, ".kicad_sch")
    output_file = make_output_directory(dir, filename)
    run_kicad_cli_command("bom", "sch", input_file, output_file)


def export_pcb_to_step(dir, filename):
    input_file = make_input_directory(dir, ".kicad_pcb")
    output_file = make_output_directory(dir, filename)
    run_kicad_cli_command("step", "pcb", input_file, output_file, "-f", "--include-zones", "--include-tracks")


def export_pcb_to_dxf(dir, filename):
    input_file = make_input_directory(dir, ".kicad_pcb")
    output_file = make_output_directory(dir, filename)
    run_kicad_cli_command("dxf", "pcb", input_file, output_file, "--layers", ",".join(pcb_layers))


for dir in dirs:
    export_sch_to_pdf(dir, "schematic.pdf")
    export_sch_to_bom(dir, "bom.csv")
    export_pcb_to_step(dir, "pcb.step")
    export_pcb_to_dxf(dir, "pcb.dxf")

print("All .kicad_sch and .kicad_pcb files processed.")
