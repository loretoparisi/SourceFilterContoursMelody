'''
Created on Aug 31, 2016

@author: georgid
'''
import json
import os

subset = 'v'


class   Parameters(object):
    
    with_MATPLOTLIB = True
    datasetIKala  = True
    medleyDb = False
    for_makam = False
        
    iKala_URI = '/home/georgid/Documents/iKala/'
    medleyDbURI =  '/home/georgid/Documents/medleyDB/'
    iKala_annotation_URI = iKala_URI + "/PitchLabel/"

    @staticmethod
    def set_paths():
        pass
    
    OLAP_THRESH = 0.5 
    
    dim_timbre = 6 # 5 vocal var + 1 fluctogram
    dim_vv = 5
    
    useMFCC_for_classification = False
    useVV_for_classification = False
    use_SAL_for_classification = True
    use_fluct_for_classification = True

    read_features_from_MATLAB = False # load .arff files per contour extracted with Lehner's code matlab
    

    
#     if useMFCC_for_classification and not useVV_for_classification:
#         features_MATLAB_URI = 'SVD2015/MFCC_29_30_0_0.5_0t/300_200_300/'
#     
#     if useMFCC_for_classification and useVV_for_classification:
#         features_MATLAB_URI = 'SVD2015/'
#     
#     if not useMFCC_for_classification and useVV_for_classification:
    features_MATLAB_URI = '/SVD2015/varMFCC_29_30_0_0.5_0t/300_100_300/5_1_5/'

    

    extract_timbre = 1
    
    to_audio = False
    
    
    if datasetIKala:
        
        contour_URI = iKala_URI + '/Conv_mu-1_G-0_LHSF-0_pC-27.56_pDTh-1.3_pFTh-0.7_tC-100_mD-100_vxTol-0.2_LEH/'
#         contour_URI = iKala_URI + '/Conv_mu-1_G-0_LHSF-0_pC-27.56_pDTh-0.9_pFTh-0.9_tC-100_mD-100_vxTol-0.2/'
        contour_URI = iKala_URI + '/Conv_mu-1_G-0_LHSF-0_pC-27.56_pDTh-0.9_pFTh-0.9_tC-100_mD-300_vxTol-0.2_LEH/'

#         contour_URI = iKala_URI + '/Conv_mu-1_G-0_LHSF-0_pC-27.56_pDTh-1.3_pFTh-0.9_tC-50_mD-100_vxTol-0.2/'
#         contour_URI = iKala_URI + '/Conv_mu-1_G-0_LHSF-0_pC-27.56_pDTh-1.3_pFTh-0.7_tC-100_mD-100_vxTol-0.2_LEH/'
        
        dir_tracks = os.path.join( os.path.dirname(os.path.realpath(__file__)) , 'contour_classification/melody_trackids_iKala.json' )
#         dir_tracks = os.path.join( os.path.dirname(os.path.realpath(__file__)) , 'contour_classification/melody_trackids_iKala_subset.json' )
#         dir_tracks = os.path.join( os.path.dirname(os.path.realpath(__file__)) , 'contour_classification/melody_trackids_iKala_subset_small.json' )

        with open(dir_tracks, 'r') as fhandle:
            track_list = json.load(fhandle)
        tracks = track_list['tracks']
    elif for_makam:
        tracks = ['ba1dc923-9b0e-4b6b-a306-346bd5438d35']
    elif medleyDb: # medley DB
        
        contour_URI = medleyDbURI + '/Conv_mu-1_G-0_LHSF-0_pC-27.56_pDTh-0.9_pFTh-0.9_tC-50_mD-100_vxTol-0.2/'
        contour_URI = medleyDbURI + '/Conv_mu-1_G-0_LHSF-0_pC-27.56_pDTh-1.3_pFTh-0.9_tC-50_mD-100_vxTol-0.2/'
        contour_URI = medleyDbURI + '/Conv_mu-1_G-0_LHSF-0_pC-27.56_pDTh-0.9_pFTh-0.9_tC-50_mD-100_vxTol-0.2/'
        
        dir_tracks = os.path.join( os.path.dirname(os.path.realpath(__file__)) , 'contour_classification/melody_trackids.json' )
        dir_splits = os.path.join( os.path.dirname(os.path.realpath(__file__)) , 'contour_classification/v_i_splits.json' )

        if subset == 'all':
            with open(dir_tracks, 'r') as fhandle:
                track_dict = json.load(fhandle)
                tracks = track_dict['tracks'] 
        else:
            with open(dir_splits, 'r') as fhandle:
                vi_dict = json.load(fhandle)
            if subset == 'i':
                tracks = [k for k in vi_dict.keys() if vi_dict[k] == "i"]
            if subset == 'v':
                tracks = [k for k in vi_dict.keys() if vi_dict[k] == "v"]
        
        print len(tracks)
        tracks_in_dir = os.listdir('/home/georgid/Documents/medleyDB/audio/mono_22050/')
##        remove all which are not in list of vocal
#         for track in tracks_in_dir:
#             if track[:-8] not in tracks:
#                 os.remove('/home/georgid/Documents/medleyDB/audio/mono_22050/' + track )
    
    test_track = '10161_chorus'
    
    CONTOUR_EXTENSION = '.pitch.ctr'
    
    with_plotting = False
    
    ###### not used, just to satisfy 
    harmonicTreshold = -70
    wSize = 2048
    nHarmonics = 30
    