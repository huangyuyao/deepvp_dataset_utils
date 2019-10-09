import sys
from pathlib import Path

class DeepVPLabelParser:
    SUBSETS = ("AL2MI australia boston BZ2CL CZ2ET indonesia japan LA2NY la_city " +
    "la_mountain lasvegas london_city mexico MT2NC newzealand norway paris PT2IT " +
    "russia SouthAfrica stockholm tailand TX2ND WA2FL").split(' ')

    def __init__(self, root):
        self.rootstr = root
        self.rootpath = Path(root)
        self.dataitems = []
        for subset in self.SUBSETS:
            subsetpath = self.rootpath / subset
            if not subsetpath.exists():
                self.FileNotExistsWarning(subsetpath)
                continue
            # print(subset)
            labeltxt = subsetpath / 'IROS2012_label.txt'
            imgroot = subsetpath / 'img'
            if not labeltxt.exists():
                self.FileNotExistsWarning(labeltxt)
                continue
            if not imgroot.exists():
                self.FileNotExistsWarning(imgroot)
                continue
            with open(str(labeltxt), 'r') as labelfile:
                for labelline in labelfile.readlines():
                    tokens = labelline.split(',')
                    imgfilename = tokens[-1][38:-1]
                    tokens2 = imgfilename.split('_')
                    vpgt = int(tokens2[3]), int(tokens2[4])
                    imgpath = imgroot / imgfilename
                    if not imgpath.exists():
                        self.FileNotExistsWarning(imgpath)
                        continue
                    dataitem = (str(imgpath), vpgt)
                    self.dataitems.append(dataitem)
    def FileNotExistsWarning(self, filepath):
        print("FileNotExists: %s \n Warning: skipping file or directory recursively because of not existing files!" % str(filepath))
    def __getitem__(self, idx):
        return self.dataitems[idx]
    def __len__(self):
        return len(self.dataitems)


if __name__ == "__main__":
    parser = DeepVPLabelParser(sys.argv[1] if len(sys.argv) > 1 else '.')
    print(len(parser))
    print(parser[0])
