# Product matching

In this project we are going to match various products on two famous e-commerce website __Flipkart__ and __Amazon__ with the help of dataset provided. [Dataset link](https://www.dropbox.com/sh/aypq6h3254207bs/AACzMLvo-XtK9sYAAma6FW0la?dl=0)

> Note: The datasets shared are from free open data sources. We are not affiliated with Flipkart or Amazon.

## Libraries & Framework used
- Pandas
- Pandas Profiling
- TheFuzz

## Pandas Profiling :
> `pandas-profiling` generates profile reports from a pandas `DataFrame`. The pandas `df.describe()` function is handy yet a little basic for exploratory data analysis. `pandas-profiling` extends pandas `DataFrame` with `df.profile_report()`, which automatically generates a standardized univariate and multivariate report for data understanding. <br><br>
The report consist of the following:
- DataFrame overview,
- Each attribute on which DataFrame is defined,
- Correlations between attributes (Pearson Correlation and Spearman Correlation), and
- A sample of DataFrame.

> __Download and View__ [`AMZprofile.html`](https://github.com/Poseidon-SV/AMZ-FK_Product_Matching/blob/main/AMZprofile.html) and [`FKprofile.html`](https://github.com/Poseidon-SV/AMZ-FK_Product_Matching/blob/main/FKprofile.html) for more detailed report of Amazon and Flipkart dataset.

## The Fuzz :
> [FuzzyWuzzy](https://pypi.org/project/thefuzz/) is a library of Python which is used for string matching. Fuzzy string matching is the process of finding strings that match a given pattern. Basically it uses __Levenshtein Distance__ to calculate the differences between sequences.

### Levenshtein distance :
> The Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. 

![Screenshot (2208)](https://user-images.githubusercontent.com/87477923/206461984-9e6e46e7-fcbd-499d-bdf3-746d352ba25e.png)

## About Programme
In this programme you have to input the product name from the given product list which is from the database or you can input your own product. The Programme will search for the best result/s for your input product matching to the Flipkart and Amazon _Retail Price_ and _Discounted Price_ from cheapest to expensive using Levenshtein distance.

### Product List
![Screenshot (2220)](https://user-images.githubusercontent.com/87477923/206462082-c5733624-b5b1-4fb4-bcb8-23b3c15981cc.png)

### Input and Matching Product name
![Screenshot (2219)](https://user-images.githubusercontent.com/87477923/206462113-d8f9273b-3e84-4bbb-a4bf-49160bea51d0.png)


## You can just download and run my [`Product_Matching.exe`](https://github.com/Poseidon-SV/AMZ-FK_Product_Matching/releases/tag/v0.1) executable file instead of running whole programme in your machine.
[Download Link](https://github.com/Poseidon-SV/AMZ-FK_Product_Matching/releases/tag/v0.1)

### 1. Product List
![Screenshot (2223)](https://user-images.githubusercontent.com/87477923/206463244-36ae0079-11b8-4a07-9d09-713f82565b5f.png)

### 2. Input Product name
![Screenshot (2224)](https://user-images.githubusercontent.com/87477923/206463290-887a3a35-d0b9-4139-9c9e-a695b08af93c.png)

### 3. Result
![Screenshot (2227)](https://user-images.githubusercontent.com/87477923/206463308-8f845c3a-3f88-49c3-afaf-983a10894ebe.png)

