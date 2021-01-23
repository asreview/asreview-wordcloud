# ASReview-wordcloud

![Deploy and release](https://github.com/asreview/asreview-wordcloud/workflows/Deploy%20and%20release/badge.svg)![Build status](https://github.com/asreview/asreview-wordcloud/workflows/test-suite/badge.svg)

This is a wordcloud supplemental package for the
[ASReview](https://github.com/asreview/asreview) software. It is an easy way
to create a visual impression of the contents of datasets.

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

It should list the 'wordcloud' modus.

## Basic usage

```
asreview wordcloud MY_DATA.csv
```
