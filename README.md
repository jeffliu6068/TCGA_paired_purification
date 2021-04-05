# TCGA paired purification

The tcga_paired_purification packages allows researchers to input common paired experiments (i.e. cancer paired with normal samples) and use that as a basis to remove contamination due to non-cancerous components. The package was specifically wrote to deal with the normal contamination in TCGA datasets. 


### Download Package

Download the tcga_paired_purification package by:
```
pip install git+https://github.com/jeffliu6068/tcga_paired_purification.git
```
or 
```
pip install tcga_paired_purification
```

### Import

Once installed, import the package by: 

```
import tcga_paired_purification
```
## Intuition: How DEA Works to Identify Differentially Expressed Genes

The package takes into account 3 seperate information:

1) Contaminated expression data (i.e. TCGA cancer RNA-seq)
2) Mean and standard deviations of the distributions of normal data
3) Purity of the contaminated data (i.e. copy number variation or histological assessment)

By taking into account the ratio of normal vs cancer proportion via copy number variation, we can remove normal contamination from the paired cancer expression data as shown in the TCGA dataset.

# Available Tools in the tcga_paired_purification Package

## tcga_paired_purification

```
import tcga_paired_purification as tpp

purified_df = tpp.tcga_paired_purification(input_data_cancer, input_data_normal, purity_df)
```
1. input_data_cancer is the input dataframe with genes (row) x samples (columns)

2. input_data_normal is a dataframe with the information of the means and standard deviation of the paired normal distribution of each gene and with columns 'mean' and 'std' 

3. purity_df is a dataframe with samples (rows) x purity (columns)

## Authors

* **Ta-Chun (Jeff) Liu** - [jeffliu6068](https://github.com/jeffliu6068)
* **Sir Walter Fred Bodmer FRS FRSE** - *Supervision*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration: Thank you for all that has contributed ideas and expertise to make this possible. Let's advance science together. 

