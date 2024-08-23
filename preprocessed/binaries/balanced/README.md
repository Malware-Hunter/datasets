# Datasets - Binaries - Balanced Datasets

## Overview
This directory contains the binaries version of the preprocessed malware datasets. These datasets focus on binary features extracted from various malware samples, making them suitable for binary classification and related analysis.

## Datasets Balanced by Number of Samples From Minority Class

The datasets are balanced by the number of samples from the minority class to ensure a fair and unbiased analysis. Irrelevant features (which have a single value) were also deleted to improve the quality and effectiveness of the data for analysis and machine learning tasks.


## Datasets Description

|             Dataset               | Features | Malwares | Benigns | Total |
|:---------------------------------:|:--------:|:--------:|:-------:|:-----:|
|             ADROIT                |   118    |   3418   |   3418  |  6836 |
|           AndroCrawl              |   136    |   10170  |  10170  | 20340 |
|       Android Permissions         |   148    |   9077   |   9077  | 18154 |
|  DefenseDroid APICalls Closeness  |   4273   |   5222   |   5222  | 10444 |
|   DefenseDroid APICalls Degree    |   6001   |   5222   |   5222  | 10444 |
|    DefenseDroid APICalls Katz     |   6001   |   5222   |   5222  | 10444 |
|      DefenseDroid PRS[^PRS]       |   2875   |   5975   |   5975  | 11950 |
|           DREBIN-215              |   215    |   5555   |   5555  | 11110 |
|      KronoDroid Real Device       |   285    |   36755  |  36755  | 73510 |
|        KronoDroid Emulator        |   275    |   28745  |  28745  | 57490 |


[^PRS]: Permissions, Receivers and Services

## Usage

### Downloading

- Clone or download this directory to your local machine.

### Accessing the Datasets

- The datasets are provided as CSV files. Use Python with pandas or any compatible tool to load and analyze the data.

### Analysis

- Utilize these binary-feature datasets for binary classification, clustering, and other malware-related research.

### Citation

- If you utilize these datasets in your research, please cite the repository or provide appropriate attribution to the original source.

## License

This dataset is released under the [CC BY 4.0 (Creative Commons Attribution 4.0 International)](https://creativecommons.org/licenses/by/4.0/).

## Feedback and Contributions

Feedback, suggestions, and contributions are encouraged! Contact us or submit a pull request if you wish to contribute.
