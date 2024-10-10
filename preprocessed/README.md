# Malware Datasets - Preprocessed

## Overview

This repository contains several preprocessed datasets of malware samples ready for analysis. Each dataset has undergone cleaning, transformation, and preparation for use in malware detection and analysis projects. Three types of preprocessed datasets are available for each dataset: binaries, continuous, and complete.

While we provide these preprocessed datasets for convenience, the original datasets and the tools used for preprocessing are also available in the repository, allowing users to replicate the process themselves if they wish.

The original datasets can be found in the [Originals] (https://github.com/Malware-Hunter/datasets/tree/main/originals) folder, and the [Code for Handling Datasets](https://github.com/Malware-Hunter/datasets/tree/main/tools) used for preprocessing are available in the tools directory. This allows users to replicate the preprocessing themselves if desired, though the preprocessed datasets are provided for convenience.

## Datasets Description

| Dataset Name                        | Samples | Features | Type Features               |
|-------------------------------------|---------|----------|-----------------------------|
| ADROIT                              | 11476   | 182      | Permission                  |
| AndroCrawl                          | 162983  | 221      | Permission                  |
| Android Permissions                 | 29999   | 183      | Permission                  |
| DefenseDroid APICalls Closeness     | 10476   | 21997    | API Calls                   |
| DefenseDroid APICalls Degree        | 10476   | 21997    | API Calls                   |
| DefenseDroid APICalls Katz          | 10476   | 21997    | API Calls                   |
| DefenseDroid[^PRS]                  | 11975   | 2938     | API Calls                   |
| DREBIN-215                          | 15031   | 215      | Permissions, Intents, API Calls |
| KronoDroid Real Device              | 78137   | 483      | Permissions, Intents, API Calls |
| KronoDroid Emulator                 | 63911   | 482      | Permissions, Intents, API Calls |

[^PRS]: Permissions, Receivers and Services

## Preprocessing Steps

The datasets have undergone the following preprocessing steps:

- **Removal of Missing Values**: Any samples with missing values have been removed from the datasets.
- **Removal of Duplicate Columns and/or Samples**: Duplicate columns and/or samples have been removed to ensure data integrity.
- **Removal of Irrelevant Features**: Columns containing only one value across all samples have been removed as they do not provide useful information for analysis.
- **Conversion of Data Types**: Data types have been converted as necessary to ensure consistency and compatibility with analysis tools.

### Types of Preprocessed Datasets:

1. **Binaries**: Preprocessed dataset focusing on binary features extracted from malware samples.
2. **Continuous**: Preprocessed dataset containing continuous features extracted from malware samples.
3. **Complete**: Preprocessed dataset containing a combination of binary and continuous features, providing a comprehensive view of malware characteristics.

## Usage

- **Downloading**: Clone or download the repository to your local machine.
- **Accessing the Datasets**: The preprocessed datasets can be found in [Preprocessed](https://github.com/Malware-Hunter/datasets/tree/main/preprocessed). Ensure you have the necessary tools (e.g., Python with pandas) to load and analyze the datasets.
- **Analysis**: Utilize the datasets for malware detection, classification, clustering, or any other malware-related research.
- **Citation**: If you utilize these datasets in your research or project, please cite this repository or provide appropriate attribution to the original source.

## License

This dataset is released under the CC BY 4.0 (Creative Commons Attribution 4.0 International): This license allows others to use your dataset, as long as they provide attribution to you as the creator. It's a relatively permissive option, but it still requires users to attribute authorship of the dataset to you.

## Feedback and Contributions

Feedback, suggestions, and contributions are encouraged! If you have any questions or wish to contribute to the datasets, please contact us or submit a pull request.
