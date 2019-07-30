#!/usr/bin/env python

# Script to compute evaluation metrics given a pair of segmentation maps per image

import numpy as np
import os
import imageio

def _computeMetrics(confusion):
    '''
    Compute evaluation metrics given a confusion matrix.
    :param confusion: any confusion matrix
    :return: tuple (miou, fwiou, macc, pacc, ious, maccs)
    '''

    # Init
    labelCount = confusion.shape[0]
    ious = np.zeros((labelCount))
    maccs = np.zeros((labelCount))
    ious[:] = np.NAN
    maccs[:] = np.NAN

    # Get true positives, positive predictions and positive ground-truth
    total = confusion.sum()
    if total <= 0:
        raise Exception('Error: Confusion matrix is empty!')
    tp = np.diagonal(confusion)
    posPred = confusion.sum(axis=0)
    posGt = confusion.sum(axis=1)
    
    # Check which classes have elements
    valid = posGt > 0
    iousValid = np.logical_and(valid, posGt + posPred - tp > 0)

    # Compute per-class results and frequencies
    ious[iousValid] = np.divide(tp[iousValid], posGt[iousValid] + posPred[iousValid] - tp[iousValid])
    maccs[valid] = np.divide(tp[valid], posGt[valid])
    freqs = np.divide(posGt, total)

    # Compute evaluation metrics
    miou = np.mean(ious[iousValid])
    fwiou = np.sum(np.multiply(ious[iousValid], freqs[iousValid]))
    macc = np.mean(maccs[valid])
    pacc = tp.sum() / total
    acc = np.trace(confusion)/total

    return miou, fwiou, macc, pacc, ious, maccs, acc

if __name__ == "__main__":

    # Path to dir containing ground truth seg maps
    ground_truth_seg_dir_path = "test_results_0629"

    # Path dir containing spade seg maps
    spade_seg_dir_path  = "test_results"
    
    # Number of classes
    num_classes = 19

    confusion_matrix = np.zeros((num_classes, num_classes)).astype(int)

    for image in os.listdir(ground_truth_seg_dir_path):
        gt_image_path = os.path.join(ground_truth_seg_dir_path, image)
        spade_image_path = os.path.join(spade_seg_dir_path, image)
        gti = imageio.imread(gt_image_path)
        
        if os.path.exists(spade_image_path):
            si = imageio.imread(spade_image_path)
        else:
            print("Corresponding image for {} not found in spade dir.".format(image))
            continue
        
        if gti.shape != si.shape:
            print("{} does not have matching dimensions.".format(image))
            continue
            
        for i in range(gti.shape[0]):
            for j in range(gti.shape[1]):
                true_label = gti[i,j]
                pred_label = si[i,j]
                confusion_matrix[true_label,pred_label]+=1


    miou, fwiou, macc, pacc, ious, maccs, acc= _computeMetrics(confusion_matrix)

    print("MIOU: ", miou)
    print("FWIOU: ", fwiou)
    print("MACC: ", macc)
    print("PACC: ", pacc)
    print("IOUS: ", ious)
    print("MACCS: ", maccs)
    print("Accuracy: ", acc)

