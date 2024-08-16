# Dataset Cleaning Scripts

This repository contains a collection of scripts for cleaning and preprocessing datasets related to the Android malware project. The scripts are designed to facilitate data preparation before analysis or modeling, ensuring that the datasets are in a suitable format for use.

## Content and Usage

### `pp_adroit.py`

**Description:**  
Preprocesses the Adroit dataset:

- Removes missing values and irrelevant columns.
- Removes duplicate samples.
- Renames the class column and casts numeric data.
- Generates both continuous and binary datasets.

**Usage:**  

```bash
python pp_adroit.py -d <dataset.csv>
 ```

### `pp_androcrawl.py`

**Description:**

Preprocesses the Androcrawl dataset:

- Merges datasets from permissions, receivers, and services.
- Removes missing values and duplicates.
- Handles irrelevant features and casts numeric data.
- Generates continuous and binary datasets.

**Usage:**

```bash
python pp_androcrawl.py -d <dataset0.csv> -d <dataset1.csv> -d <dataset2.csv>
 ```

### `pp_defensedroid_apicalls.py`

**Description:**

Preprocesses the DefenseDroid API Calls dataset:

- Removes missing values and duplicates.
- Handles irrelevant features and renames columns.
- Generates both continuous and binary datasets.

**Usage:** 

```bash
python pp_defensedroid_apicalls.py -d <dataset.csv>
 ```

### `pp_defensedroid_prs.py`

**Description:**

Preprocesses the DefenseDroid Permissions, Receivers, and Services dataset:

- Merges datasets from permissions, receivers, and services.
- Removes missing values and duplicates.
- Handles irrelevant features and renames columns.
- Generates continuous and binary datasets.

**Usage:**

```bash
python pp_defensedroid_prs.py -d <dataset0.csv> -d <dataset1.csv> -d <dataset2.csv>

 ```

### `pp_kronodroid_emu.py`

**Description:**

Preprocesses the Kronodroid Emulator dataset:

- Merges datasets and aligns columns.
- Removes missing values and irrelevant features.
- Renames columns and casts numeric data.
- Generates continuous and binary datasets.

**Usage:**

```bash
python pp_defensedroid_prs.py -d <dataset0.csv> -d <dataset1.csv> -d <dataset2.csv>
 ```

### `pp_kronodroid_real.py`

**Description:**

Preprocesses the Kronodroid Real Device dataset:

- Merges datasets and aligns columns.
- Removes missing values and irrelevant features.
- Renames columns and casts numeric data.
- Generates continuous and binary datasets.

**Usage:**

```bash
python pp_kronodroid_real.py -d <dataset0.csv> -d <dataset1.csv> 
```

### `pp_drebin.py`

**Description:**

Preprocesses the Drebin dataset:

- Removes missing values and irrelevant features.
- Casts numeric data and generates binary datasets.

**Usage:**

```bash
python pp_drebin.py -d <dataset.csv>
 ```

### `pp_permissions.py`

**Description:**

Preprocesses the Permissions dataset:

- Removes specific columns, missing values, and duplicates.
- Handles irrelevant features and renames the class column.
- Generates continuous and binary datasets.

**Usage:**

```bash
python pp_permissions.py -d <dataset.csv>
 ```

### `valida_dataset_binary`

**Description:**

 This C script reads from the standard input and counts the number of commas in each line of the input data. It prints the comma count for each line to the standard output.

 **Usage:**

 1.Compile

 ```bash
gcc valida_dataset_binary.c -o valida_dataset_binary
 ```

 2.Run

  ```bash
./valida_dataset_binary < file.csv
 ```

### `process_csv`

**Description:**

 This C script reads lines from the standard input (e.g., a CSV file) and processes each line based on a specified number of commas. For lines with the exact number of commas provided as a command-line argument, it prints out each value separated by commas, with each value converted to 0 if it was 0 in the original input.

**Usage:**

1.Compile

 ```bash
gcc process_csv.c -o process_csv
 ```

2.Run 

  ```bash
./process_csv <exact_number_of_commas> < file.csv
```

Replace <exact_number_of_commas> with the number of commas you expect in each line, and <file.csv> with your CSV file.

## License

This dataset is released under the CC BY 4.0 (Creative Commons Attribution 4.0 International): This license allows others to use your dataset, as long as they provide attribution to you as the creator. It's a relatively permissive option, but it still requires users to attribute authorship of the dataset to you.

## Acknowledgements


## Contact

Feedback, suggestions, and contributions are welcome! If you have any questions or wish to contribute to the datasets, please contact us.