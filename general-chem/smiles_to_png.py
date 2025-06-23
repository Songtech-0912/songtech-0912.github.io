# modified from:
# https://www.reddit.com/r/chemistry/comments/1fgp0t7/script_to_convert_smiles_to_png/
# saves generated SMILES to a smiles/ subfolder

import sys
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import rdChemReactions
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
file_output = path.join(getcwd(), f"smiles/{smiles_input}.png")

def generate_image(smiles_input):
    # Parse as a molecule
    try:
        mol = Chem.MolFromSmiles(smiles_input)
        if mol:
            return Draw.MolToImage(mol)
    except Exception as e:
        print(f"Molecule parsing failed: {e}", file=sys.stderr)

    return None

# Generate the image
img = generate_image(smiles_input)

if img is None:
    print("Failed to parse SMILES", file=sys.stderr)
    sys.exit(1)

# Save the image to an in-memory byte buffer
# buffer = BytesIO()
#img.save(buffer, format="PNG")

# write to disk
img.save(file_output)