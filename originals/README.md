# Datasets - Original Malware Datasets

## Description

 CSV files labeled as malware or benign, containing features such as permissions, system calls, hardware access, and API calls.

## Overview

| Dataset                         | Samples | Features | Type Features                   | Size (KB) | Malwares | Benigns | SHA-256                                                          |
| ------------------------------- | ------- | -------- | ------------------------------- | --------- | -------- | ------- | ---------------------------------------------------------------- |
| ADROIT                          | 11476   | 182      | Permission                      | 14911     | 3418     | 8058    | cb264931f9be09f5b9c4dca48ee8737b89ab79589c10f71ada546eea244f043d |
| AndroCrawl                      | 162983  | 221      | Permission                      | 215057    | 10170    | 86574   | a46747ec8c68c021478a1a9038c0467a55e00c2625380d4020ddcacfa728a0d5 |
| Android Permissions             | 29999   | 183      | Permission                      | 53068     | 17787    | 9077    | 2ff6fc1cdd95e61a4247c26cf1bdb710d87c4b8d16feb4222607cd74b6d19256 |
| DefenseDroid APICalls Closeness | 10476   | 21997    | API Calls                       | 529991    | 5254     | 5222    | 349fc0ffb2434980e449cf40e96c64e969e8db3d2980272e5d10e844ecdd0a7c |
| DefenseDroid APICalls Degree    | 10476   | 21997    | API Calls                       | 552263    | 5254     | 5222    | 7e6ebc100b708a9846a9cd93f06552c3b21351c773437114650bb059eb70fca3 |
| DefenseDroid APICalls Katz      | 10476   | 21997    | API Calls                       | 548249    | 5254     | 5222    | 5f5a42386cafa2ea6dfdd47e5eefef9758a0591b9ed9301abcfce3ebcf9a72c2 |
| DefenseDroid PRS1               | 11975   | 2938     | API Calls                       | 68834     | 5975     | 11975   | 083bf4f4a088005e63f5ea3cebe25477a85a14a0d84878b47a48f80ab5139ba9 |
| DREBIN-215                      | 15031   | 215      | Permissions, Intents, API Calls | 6363      | 9476     | 15031   | 710f2c11b0cad04c36f56dd16398127feb697fd99e8efa7f75890b792fba3ad5 |
| KronoDroid Real Device          | 78137   | 483      | Permissions, Intents, API Calls | 70140     | 36755    | 78137   | 4ca8c1c706989d9e2946992b29fc2282d391822d3722e67e2e59d2bf1075b0ad |

## Source

Collected from various public and proprietary repositories.

### AndroCrawl

**Context**

A dataset of benign and malware android application samples of alternative Android marketplaces created by SISTO, A. (2013).

**Acknowledgements**

SISTO, A. (2013). AndroCrawl: studying alternative Android marketplaces. <https://hdl.handle.net/10589/88407>

**Link**
https://github.com/phretor/ransom.mobi/blob/gh-pages/f/filter.7z

### ADROIT

**Context**

A dataset of meta information of benign and malware android samples used by Martín, A., Calleja, A., Menéndez, H. D., Tapiador, J., & Camacho, D. in the paper (2016).

**Acknowledgements**

Martín, Alejandro; Calleja, Alejandro; Menéndez, Héctor D.; Tapiador, Juan; Camacho, David (2017), “ADROIT”, Mendeley Data, V2, doi: 10.17632/yr92xbrvgx.2
ADROIT: Android malware detection using meta-information. In Computational Intelligence (SSCI), 2016 IEEE Symposium Series on (pp. 1-8). IEEE.

**Link**
https://www.kaggle.com/datasets/saurabhshahane/android-malware-dataset>

### Android Permission Dataset
 
**Context**

A dataset of of benign and malware android apps samples with their permissions.

**Acknowledgements**

Mahindru, Arvind (2018), “Android permission dataset, V1, doi: 10.17632/8y543xvnsv.1

**Link**
https://www.kaggle.com/datasets/saurabhshahane/android-permission-dataset>

### DefenseDroid
 
**Context**

A dataset of meta information of benign and malware Android APKs samples focused on Permissions, Receivers, Services and API Calls.
.
**Acknowledgements**

Defensedroid: A modern approach to android malware detection - CW Colaco, MD Bagwe, SA Bose, K Jain - Strad Research, 2021

**Link**
https://www.kaggle.com/datasets/defensedroid/android-malware-detection>

### DREBIN-215

**Context**

Dataset consisting of feature vectors of 215 attributes extracted from 15,036 applications used in the paper 'DroidFusion: A Novel Multilevel Classifier Fusion Approach for Android Malware Detection'. 2019

**Acknowledgements**

S. Y. Yerima and S. Sezer, "DroidFusion: A Novel Multilevel Classifier Fusion Approach for Android Malware Detection," in IEEE Transactions on Cybernetics, vol. 49, no. 2, pp. 453-466, Feb. 2019, doi: 10.1109/TCYB.2017.2777960.

**Link**
https://figshare.com/articles/dataset/Android_malware_dataset_for_machine_learning_2/5854653

### KronoDroid Real Device

**Context**

Android malware dataset designed to study and explore concept drift and cross-device detection issues. Created and maintained by Dr. Alejandro Guerra Manzanares during his Ph.D. studies.

**Acknowledgements**

Alejandro Guerra-Manzanares, Hayretdin Bahsi, Sven Nõmm, KronoDroid: Time-based Hybrid-featured Dataset for Effective Android Malware Detection and Characterization, Computers & Security, Volume 110, 2021,102399,ISSN 0167-4048, <https://doi.org/10.1016/j.cose.2021.102399>.

**Link**
 https://github.com/aleguma/kronodroid/tree/main/real_device
