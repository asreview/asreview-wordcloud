# ❗❗❗ Deprecated: ASReview-wordcloud

## ASReview-wordcloud is deprecated and has not been updated to ASReview version 2. To get insights into datasets and subsets of labels, you can use ASReview LAB's new dashboard. 

[![PyPI version](https://badge.fury.io/py/asreview-wordcloud.svg)](https://badge.fury.io/py/asreview-wordcloud) [![Downloads](https://pepy.tech/badge/asreview-wordcloud)](https://pepy.tech/project/asreview-wordcloud) ![Deploy and release](https://github.com/asreview/asreview-wordcloud/workflows/Deploy%20and%20release/badge.svg) ![Build status](https://github.com/asreview/asreview-wordcloud/workflows/test-suite/badge.svg) [![DOI](https://zenodo.org/badge/332095019.svg)](https://zenodo.org/badge/latestdoi/332095019)


ASReview-wordcloud is an extension for the [ASReview
LAB](https://github.com/asreview/asreview) software. It offers an easy way to
create a visual impression of the contents of datasets.

## Installation

The easiest way to install the wordcloud extension is to install from PyPI:

``` bash
pip install asreview-wordcloud
```

After installation of the wordcloud extension, `asreview` should automatically
detect it. Test this by:

```bash
asreview --help
```

It should list the `wordcloud` subcommand.

## Basic usage

The dataset should contain a column containing titles and/or abstracts.
For specific requirements check the [ASReview documentation](https://asreview.readthedocs.io/en/latest/intro/datasets.html).
To use your data use:

```
asreview wordcloud MY_DATA.csv
```

The following shows the [Schoot et al. (2017) dataset:](https://asreview.readthedocs.io/en/latest/intro/datasets.html#benchmark-datasets)

![All texts](https://github.com/asreview/asreview-wordcloud/blob/main/figures/ptsd_all.png?raw=true)

To make a wordcloud on titles only, use the `title` flag.

```
asreview wordcloud MY_DATA.csv --title
```

![Titles only](https://github.com/asreview/asreview-wordcloud/blob/main/figures/ptsd_title.png?raw=true)

To make a wordcloud on abstracts only, use the `abstract` flag.

```
asreview wordcloud MY_DATA.csv --abstract
```

![Abstracts only](https://github.com/asreview/asreview-wordcloud/blob/main/figures/ptsd_abstract.png?raw=true)

To make a wordcloud on relevant (inclusions) only, use the `relevant` flag.

```
asreview wordcloud MY_DATA.csv --relevant
```

### Save figure

Save the wordcloud to a file with the `-o`  flag.

```
asreview wordcloud MY_DATA.csv -o MY_DATA_WORDCLOUD.png
```

## License

This extension is published under the [MIT license](/LICENSE).

## Contact

This extension is part of the ASReview project ([asreview.ai](https://asreview.ai)). It is maintained by the
maintainers of ASReview LAB. See [ASReview
LAB](https://github.com/asreview/asreview) for contact information and more
resources.
