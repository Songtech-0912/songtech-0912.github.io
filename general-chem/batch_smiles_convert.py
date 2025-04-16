# This is to extract the linked SMILES images
# that were renderered using RxnFinder
# (http://hulab.rxnfinder.org/smi2img/)
# into local images for faster + offline loads
# it saves generated SMILES to a smiles/ subfolder

import sys
from rdkit import Chem
from rdkit.Chem import Draw
import subprocess
import re
from urllib import parse as urlparse
from os import getcwd, path, mkdir

"""
These are the forbidden characters
in file paths:
< (less than)
> (greater than)
: (colon - sometimes works, but is actually NTFS Alternate Data Streams)
" (double quote)
/ (forward slash)
\ (backslash)
| (vertical bar or pipe)
? (question mark)
* (asterisk)
"""
forbidden_chars = ("<", ">", ":", "'", "\\", "/", "|", "?", "*")

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

def savesvg(svgpath, svgcode):
    with open(svgpath, "w") as svgfile:
        svgfile.write(svgcode)
    print("Complete")

# Script start

# create output folder to write PNGs to
if not path.exists("smiles/"):
    mkdir("smiles/")

if len(sys.argv) < 2:
    print("Usage: python batch_smiles_convert [yourfile.md]")
    sys.exit(1)

input_md_file = sys.argv[1]

# read markdown file contents
with open(input_md_file, "r") as f:
    input_md = f.read()

rxnfinder_regex = r"\(.+?smi2img\/(.+?)\?.+?\)"
matches = re.findall(rxnfinder_regex, input_md, re.IGNORECASE | re.MULTILINE | re.DOTALL)

total_matches = len(matches)

for idx, smiles_code in enumerate(matches):
    print(f"Processing {idx+1}/{total_matches} SMILES chunks")
    # Generate the image
    img = generate_image(smiles_code)
    if img is None:
        print(f"Failed to parse SMILES {smiles_code}")
        continue
    # as SMILES contains characters that
    # are invalid as file paths we URL-encode
    # the filenames
    fname = f"{smiles_code}.svg"
    if any(special_char in smiles_code for special_char in forbidden_chars):
        fname = urlparse.quote_plus(fname)
    fpath = "smiles/" + fname
    savesvg(fpath, img)

"""
# now do the replacement on the markdown file too
replacements_md = re.sub(
        rxnfinder_regex,
        lambda match: 
    )
"""