import cv2
from skimage.metrics import structural_similarity as compare_ssim

def image_comapre(imgUP, imgDOWN, imgLEFT, imgRIGHT, imgBLANK,pic):

    imageUP = cv2.imread(imgUP)
    imageDOWN = cv2.imread(imgDOWN)
    imageLEFT = cv2.imread(imgLEFT)
    imageRIGHT = cv2.imread(imgRIGHT)
    imageBLANK = cv2.imread(imgBLANK)

    grayORG = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    grayUP = cv2.cvtColor(imageUP, cv2.COLOR_BGR2GRAY)
    grayDOWN = cv2.cvtColor(imageDOWN, cv2.COLOR_BGR2GRAY)
    grayLEFT = cv2.cvtColor(imageLEFT, cv2.COLOR_BGR2GRAY)
    grayRIGHT = cv2.cvtColor(imageRIGHT, cv2.COLOR_BGR2GRAY)
    grayBLANK = cv2.cvtColor(imageBLANK, cv2.COLOR_BGR2GRAY)

    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (scoreUP, diffUP) = compare_ssim(grayORG, grayUP, full=True)
    # diffUP = (diffUP * 255).astype("uint8")

    (scoreDOWN, diffDOWN) = compare_ssim(grayORG, grayDOWN, full=True)
    # diffDOWN = (diffDOWN * 255).astype("uint8")

    (scoreLEFT, diffLEFT) = compare_ssim(grayORG, grayLEFT, full=True)
    # diffLEFT = (diffLEFT * 255).astype("uint8")

    (scoreRIGHT, diffRIGHT) = compare_ssim(grayORG, grayRIGHT, full=True)
    # diffRIGHT = (diffRIGHT * 255).astype("uint8")

    (scoreBLANK, diffBLANK) = compare_ssim(grayORG, grayBLANK, full=True)
    # diffBLANK = (diffBLANK * 255).astype("uint8")

    scores = [scoreUP, scoreDOWN, scoreLEFT, scoreRIGHT, scoreBLANK]
    score = max(scores)
    imgRead = ["UP", "DOWN", "LEFT", "RIGHT", "BLANK"]

    if score < 0.05:
        print("NO READ")
        return 0


    print("SSIM: {}".format(score), 'At index:', imgRead[scores.index(score)])

    return imgRead[scores.index(score)]