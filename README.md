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

The following shows the Schoot et al. (2017) dataset:

![figures/ptsd_all.png](figures/ptsd_all.png)

To make a wordcloud on titles only, use the `title` flag.

```
asreview wordcloud MY_DATA.csv --title
```

![figures/ptsd_title.png](figures/ptsd_title.png)

To make a wordcloud on abstracts only, use the `abstract` flag.

```
asreview wordcloud MY_DATA.csv --abstract
```

![figures/ptsd_abstract.png](figures/ptsd_abstract.png)

### Save figure

Save the wordcloud to a file with the `-o`  flag.

```
asreview wordcloud MY_DATA.csv -o MY_DATA_WORDCLOUD.png
```

## License

This extension is MIT licensed.
