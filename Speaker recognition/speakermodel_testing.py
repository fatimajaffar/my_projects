import os
import pickle
import numpy as np
import librosa
from feature_extraction import extract_features
#from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time


#path to test data
test_source   = "data/Speakers/test/"     

#path where training speakers will be saved
modelpath = "data/Speakers/speakers-model/"

gmm_files = [os.path.join(modelpath,fname) for fname in 
              os.listdir(modelpath) if fname.endswith('.gmm')]

#Load the Gaussian speaker Models
models    = [pickle.load(open(fname,'rb')) for fname in gmm_files]
speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname 
              in gmm_files]

error = 0
total_sample = 0


print ("Do you want to Test a Single Audio: Press '1' or The complete Test Audio Sample: Press '0' ?")
take = int(input().strip())

if take==1:
    print ("Enter the File name from Test Audio Sample Collection :")
    path=input().strip
    print("Testing Audio:",path)
    audio,sr=librosa.load(test_source+path)
    vector=extract_features(audio,sr)
    
    log_likelihood=np.zeros(len(models))
    for i in range(len(models)):
        gmm=models[i]
        scores=np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
        
    winner = np.argmax(log_likelihood)
    print ("\tdetected as - ", speakers[winner])
    time.sleep(1.0)
    
elif take==0:
    test_file='testdata_paths.txt'
    file_paths=open(test_file,'r')
    for path in file_paths:
        total_sample+=1
        path=path.strip()
        print("\nTesting Audio:", path)
        audio,sr=librosa.load(test_source+path)
        vector=extract_features(audio,sr)
        log_likelihood=np.zeros(len(models))
        
        for i in range(len(models)):
            gmm=models[i]
            scores=np.array(gmm.score(vector))
            log_likelihood[i]=scores.sum()
        winner=np.argmax(log_likelihood)
        print('Detected as:',speakers[winner])
        checker_name=path.split('/')[1].split('-')[1].strip()
        if speakers[winner] != checker_name:
            print('Actual Speaker:', checker_name)
            error += 1
        time.sleep(1.0)
    print('\nErrors:',error,'Samples:',total_sample)
    accuracy = ((total_sample - error) / total_sample) * 100
    print ("The Accuracy Percentage for the current testing Performance with MFCC + GMM is : "+"{:.2f}".format(accuracy)+"%")