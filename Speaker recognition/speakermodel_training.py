# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:45:22 2020

@author: SOFTAGE
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:46:05 2020

@author: SOFTAGE
"""

import pickle
import numpy as np
import librosa
from sklearn import mixture
from feature_extraction import extract_features
#from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")

#path to training data
source   = "data/Speakers/train/"   

#path where trained model will be saved
dest = "data/Speakers/speakers-model/"

train_file = "trainingdata_Path.txt"        
file_paths = open(train_file,'r')

count = 1
# Extracting features for each speaker (5 files per speakers)
features = np.asarray(())
for path in file_paths:    
    path = path.strip()   
    print(path)
    
    # read the audio
    audio, sr = librosa.load(source + path)
    
    # extract 40 dimensional MFCC & delta MFCC features
    vector   = extract_features(audio,sr)
    
    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))
    # when features of 5 files of speaker are concatenated, then do model training
	# -> if count == 5: --> edited below
    if count == 10:    
        gmm = mixture.GaussianMixture(n_components = 16, max_iter = 200, covariance_type='diag',n_init = 3)
        gmm.fit(features)
        
        # dumping the trained gaussian model
        speaker_name = path.split("/")[1].split('-')[1].strip()
        picklefile=speaker_name+".gmm"
        pickle.dump(gmm,open(dest + picklefile,'wb'))
        print ('Modeling completed for speaker:',speaker_name," with data point = ",features.shape,"\n")    
        features = np.asarray(())
        count = 0
    count = count + 1