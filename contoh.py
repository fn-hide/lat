from hashlib import new
from pickle import NEWTRUE
from random import randint
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import cv2 as cv
import numpy as np
from glob import glob
import pandas as pd

ytrue = [randint(0, 1) for i in range(100)]
ypred = [randint(0, 1) for i in range(100)]

confusion_matrix(ytrue, ypred)

accuracy_score(ytrue, ypred)

print(classification_report(ytrue, ypred))

ytrue_filepaths = glob('data/img/segmentation_masked/*png')
ypred_filepaths = glob('data/img/volume_segmented/*png')
spectrue_path = 'data/img/segmentation_masked/segmentation-0_slice-59.png'
specpred_path = 'data/img/volume_segmented/volume-0_slice-59.png'

for truepath, predpath in zip(ytrue_filepaths, ypred_filepaths):
    ytrue = cv.imread(truepath, cv.IMREAD_GRAYSCALE)
    ytrue[ytrue == 255] = 1
    
    ypred = cv.imread(predpath, cv.IMREAD_GRAYSCALE)
    ypred[ypred == 255] = 1
    

ytrue = cv.imread(spectrue_path, cv.IMREAD_GRAYSCALE)
ytrue[ytrue == 255] = 1

ypred = cv.imread(specpred_path, cv.IMREAD_GRAYSCALE)
ypred[ypred == 255] = 1

np.savetxt('true.csv', ytrue, delimiter=',', fmt='%d', )
np.savetxt('pred.csv', ypred, delimiter=',', fmt='%d', )

new_true = np.loadtxt('data/true.csv', delimiter=',').flatten()
new_pred = np.loadtxt('data/pred.csv', delimiter=',').flatten()

new_true.shape
new_true
np.unique(new_true)

confusion_matrix(new_true, new_pred)
print(classification_report(new_true, new_pred))

pd_true = pd.read_csv('data/true.csv').values.flatten()
pd_pred = pd.read_csv('data/pred.csv').values.flatten()

confusion_matrix(pd_true, pd_pred)


