import cv2
import sys
from pathlib import Path
from deepvp__imgpath_vp_dataset import DeepVPLabelParser


if __name__ == "__main__":
    parser = DeepVPLabelParser(sys.argv[1] if len(sys.argv) > 1 else '.')
    for imgpath, vp in parser:
        cvim = cv2.imread(imgpath)
        cv2.circle(cvim, vp, 5, (0, 0, 255))
        cv2.imshow("imshow", cvim)
        cv2.waitKey(0)
