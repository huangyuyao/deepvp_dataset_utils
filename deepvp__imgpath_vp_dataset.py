import sys
from pathlib import Path
from tqdm import tqdm

class DeepVPLabelParser:
    SUBSETS = ("AL2MI australia boston BZ2CL CZ2ET indonesia japan LA2NY la_city " +
    "la_mountain lasvegas london_city mexico MT2NC newzealand norway paris PT2IT " +
    "russia SouthAfrica stockholm tailand TX2ND WA2FL").split(' ')

    def __init__(self, root):
        self.rootstr = root
        self.rootpath = Path(root).resolve()
        self.dataitems = []
        for subset in tqdm(self.SUBSETS):
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
                labellines = labelfile.readlines()
                _dataitems = []
                for labelline in tqdm(labellines):
                    tokens = labelline.split(',')
                    _s = tokens[-1]
                    imgfilename = _s[_s.rfind('/')+1:-1]
                    tokens2 = imgfilename.split('_')
                    vpgt = int(tokens2[3]), int(tokens2[4])
                    imgpath = imgroot / imgfilename
                    if not imgpath.exists():
                        self.FileNotExistsWarning(imgpath)
                        continue
                    dataitem = (str(imgpath), vpgt)
                    _dataitems.append(dataitem)
                self.dataitems += _dataitems
    def FileNotExistsWarning(self, filepath):
        print("FileNotExists: %s \n Warning: skipping file or directory recursively because of not existing files!" % str(filepath))
        __import__('pdb').set_trace()
    def __getitem__(self, idx):
        return self.dataitems[idx]
    def __len__(self):
        return len(self.dataitems)


if __name__ == "__main__":
    import dill
    parser = DeepVPLabelParser(sys.argv[1] if len(sys.argv) > 1 else '.')
    with open('deepvp.index', 'wb') as f:
        dill.dump(parser, f, dill.HIGHEST_PROTOCOL)
    print(len(parser))
    print(parser[0])
