import FreeCAD
import Part
import TechDraw
import sys

input_file = 'export/printhead-pcb_step.step'
output_file = 'export/step_output_file.pdf'

try:
    doc = FreeCAD.newDocument()
    Part.insert(input_file, doc.Name)
    doc.recompute()

    page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage')
    template = FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate', 'Template')
    template.Template = FreeCAD.getResourceDir() + 'Mod/TechDraw/Templates/A3_Landscape.svg'
    page.Template = template

    view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart', 'View')
    view.Source = [FreeCAD.ActiveDocument.Objects[0]]
    page.addView(view)
    FreeCAD.ActiveDocument.recompute()

    page.ExportPdf(output_file)
    FreeCAD.closeDocument(doc.Name)
    print(f"Successfully converted {input_file} to {output_file}")
except Exception as e:
    print(f"Error during conversion: {str(e)}")
    sys.exit(1)