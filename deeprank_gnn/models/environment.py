import os


class Environment:
    "holds directory paths and device settings"

    def __init__(self, pdb_root=None, pssm_root=None, conservation_root=None, device="cpu"):
        self.pdb_root = pdb_root
        self.pssm_root = pssm_root
        self.conservation_root = conservation_root
        self.device = device

    def get_pdb_path(self, pdb_ac):
        for path in [os.path.join(self.pdb_root, "{}.pdb".format(pdb_ac.lower())),
                     os.path.join(self.pdb_root, "{}.PDB".format(pdb_ac.upper())),
                     os.path.join(self.pdb_root, "{}/{}.pdb".format(pdb_ac.upper(), pdb_ac.upper())),
                     os.path.join(self.pdb_root, "pdb{}.ent".format(pdb_ac.lower()))]:

            if os.path.isfile(path):

                return path

        raise FileNotFoundError("No pdb file found for {} under {}".format(pdb_ac, self.pdb_root))