# saves generated SMILES to a smiles/ subfolder

import sys
from rdkit import Chem
from rdkit.Chem import Draw
from io import BytesIO
from PIL import Image
import subprocess
from os import getcwd, path, mkdir

if len(sys.argv) != 2:
    print("Usage: python smiles_to_png.py 'SMILES'")
    sys.exit(1)

smiles_input = sys.argv[1]

# create output folder to write PNGs to
if not path.exists("smiles/"):
    mkdir("smiles/")
file_output = path.join(getcwd(), f"smiles/{smiles_input}.svg")

def generate_image(smiles_input):
    # Parse as a molecule and convert to SVG
    try:
        mol = Chem.MolFromSmiles(smiles_input)
        if mol:
            d2d = Draw.rdMolDraw2D.MolDraw2DSVG(250, 200)
            d2d.DrawMolecule(mol)
            d2d.FinishDrawing()
            return d2d.GetDrawingText()
    except Exception as e:
        print(f"Molecule parsing failed: {e}", file=sys.stderr)
    return None

# Generate the image
svg = generate_image(smiles_input)

if svg is None:
    print("Failed to parse SMILES", file=sys.stderr)
    sys.exit(1)

# write to disk
with open(file_output, "w") as svgfile:
    svgfile.write(svg)
    print("SVG rendered, see smiles/ folder")