from rdkit import Chem
from rdkit.Chem import Descriptors
import numpy as np
import pandas as pd

def getAromaticProportion(m) :
  aromatic_list = [m.GetAtomWithIdx(i).GetIsAromatic() for i in range(m.GetNumAtoms())]
  aromatic_count = aromatic_list.count(True)
  heavy_atom_count = Descriptors.HeavyAtomCount(m)
  return aromatic_count/heavy_atom_count

def mol_to_descriptors(mol) -> list:
  return [
    Descriptors.MolLogP(mol),
    Descriptors.MolWt(mol),
    Descriptors.NumRotatableBonds(mol),
    getAromaticProportion(mol)
  ]

def descriptors_from_smiles(smiles) -> pd.DataFrame:
  mols= [Chem.MolFromSmiles(smile) for smile in smiles]
  descriptor_array = [mol_to_descriptors(mol) for mol in mols]
  columnNames=["MolLogP","MolWt","NumRotatableBonds","AromaticProportion"]   
  
  return pd.DataFrame(
      data=descriptor_array,
      columns=columnNames
      )