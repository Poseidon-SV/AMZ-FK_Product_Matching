# Product matching

In this project we are going to match various products on two famous e-commerce website __Flipkart__ and __Amazon__ with the help of dataset provided. [Dataset link](https://www.dropbox.com/sh/aypq6h3254207bs/AACzMLvo-XtK9sYAAma6FW0la?dl=0)

> Note: The datasets shared are from free open data sources. We are not affiliated with Flipkart or Amazon.

## Libraries & Framework used
- Pandas
- Pandas Profiling
- TheFuzz

## Pandas Profiling ▶
> `pandas-profiling` generates profile reports from a pandas `DataFrame`. The pandas `df.describe()` function is handy yet a little basic for exploratory data analysis. `pandas-profiling` extends pandas `DataFrame` with `df.profile_report()`, which automatically generates a standardized univariate and multivariate report for data understanding. <br><br>
The report consist of the following:
- DataFrame overview,
- Each attribute on which DataFrame is defined,
- Correlations between attributes (Pearson Correlation and Spearman Correlation), and
- A sample of DataFrame.

## The Fuzz ▶
> [FuzzyWuzzy](https://pypi.org/project/thefuzz/) is a library of Python which is used for string matching. Fuzzy string matching is the process of finding strings that match a given pattern. Basically it uses __Levenshtein Distance__ to calculate the differences between sequences.

### Levenshtein distance ▶
> The Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. 

Leve SS

In this programme you have to input the product name from the given product list which is from the database or you can input your own product. The Programme will search for the best result/s for your input product matching to the Flipkart and Amazon _Retail Price_ and _Discounted Price_ from cheapest to expensive using Levenshtein distance.

> View [`AMZprofile.html`]() and [`FKprofile.html`]() for more detailed report of Amazon and Flipkart dataset.

SS

__You can just download and run my `Product_Matching.exe` executable file instead of running whole programme in your machine.__

