# Copyright 2020 The ASReview Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse

import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from wordcloud import WordCloud

from asreview.data import ASReviewData
from asreview.entry_points import BaseEntryPoint

try:
    from asreview.data import load_data
except ImportError:

    # backwards compat
    try:
        from pathlib import Path
        from asreview.utils import is_url
        from asreview.datasets import DatasetManager
        from asreview.datasets import DataSetNotFoundError

        def load_data(name, *args, **kwargs):
            """Load data from file, URL, or plugin.

            Parameters
            ----------
            name: str, pathlib.Path
                File path, URL, or alias of extension dataset.

            Returns
            -------
            asreview.ASReviewData:
                Inititalized ASReview data object.
            """

            # check is file or URL
            if Path(name).exists() or is_url(name):
                return ASReviewData.from_file(name, *args, **kwargs)

            # check if dataset is plugin dataset\
            try:
                dataset_path = DatasetManager().find(name).get()
                return ASReviewData.from_file(dataset_path, *args, **kwargs)
            except DataSetNotFoundError:
                pass

            # Could not find dataset, return None.
            raise FileNotFoundError(
                f"File, URL, or dataset does not exist: '{name}'")

    except ImportError:
        # fall back to from_file (without plugin datasets)
        load_data = ASReviewData.from_file


DPI = 100


def extend_stopwords(extended_words):
    """Add extra stopwords"""
    # create stopword list
    stopwords = set(STOPWORDS)
    stopwords.update(extended_words)

    return list(stopwords)


def word_cloud(words,
               caption=None,
               output_fp=None,
               random_state=None,
               width=400,
               height=200,
               **wordcloud_kwargs):
    """Word cloud for texts."""

    # create word cloud text
    text = " ".join(str(word) for word in words)

    # generate word cloud images
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          max_words=100,
                          random_state=random_state,
                          background_color="white",
                          width=width,
                          height=height,
                          **wordcloud_kwargs).generate(text)

    # render plot
    plt.figure(figsize=(width / DPI, height / DPI))
    plt.imshow(wordcloud, interpolation="bilinear")
    if caption:
        plt.set_title(caption)
    plt.axis("off")

    # save or show
    if output_fp:
        plt.tight_layout(pad=1)
        plt.savefig(output_fp, dpi=100)
    else:
        plt.show()


class WordCloudEntryPoint(BaseEntryPoint):
    description = "Wordcloud functionality for ASReview datasets."
    extension_name = "asreview-wordcloud"

    def __init__(self):
        from asreviewcontrib.wordcloud.__init__ import __version__
        super(WordCloudEntryPoint, self).__init__()

        self.version = __version__

    def execute(self, argv):
        parser = _parse_arguments(
            version=f"{self.extension_name}: {self.version}")
        args = parser.parse_args(argv)

        # read data in ASReview data object
        asdata = load_data(args.path)

        # wordcloud styling
        styling = {
            "colormap": args.colormap,
            "width": args.width,
            "height": args.height
        }

        # Slice relevant or irrelevant items
        if (args.relevant and args.irrelevant) or \
                (not args.relevant and not args.irrelevant):
            subset = [True] * len(asdata)

        # only relevant
        if args.relevant:
            subset = asdata.labels == 1

        # only irrelevant
        if args.irrelevant:
            subset = asdata.labels == 0

        # all texts
        if (args.title and args.abstract) or \
                (not args.title and not args.abstract):
            word_cloud(asdata.texts[subset],
                       output_fp=args.output,
                       random_state=args.random_state,
                       **styling)

        # only title
        if args.title:
            word_cloud(asdata.title[subset],
                       output_fp=args.output,
                       random_state=args.random_state,
                       **styling)

        # only abstract
        if args.abstract:
            word_cloud(asdata.abstract[subset],
                       output_fp=args.output,
                       random_state=args.random_state,
                       **styling)


def _parse_arguments(version="Unknown"):
    parser = argparse.ArgumentParser(prog="asreview wordcloud")
    parser.add_argument("path", type=str, help="The file path of the dataset.")
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=version,
    )
    parser.add_argument("--title",
                        action="store_true",
                        help="Create wordcloud of titles only.")
    parser.add_argument("--abstract",
                        action="store_true",
                        help="Create wordcloud of abstracts only.")
    parser.add_argument("--relevant",
                        action="store_true",
                        help="Create wordcloud of relevant records only.")
    parser.add_argument("--irrelevant",
                        action="store_true",
                        help="Create wordcloud of irrelevant records only.")
    parser.add_argument("--random_state",
                        type=int,
                        default=535,
                        help="Set random state of wordcloud.")
    parser.add_argument("--colormap",
                        type=str,
                        default="viridis",
                        help="The colormap of the wordcloud.")
    parser.add_argument("--width",
                        type=int,
                        default=400,
                        help="The width of the wordcloud.")
    parser.add_argument("--height",
                        type=int,
                        default=200,
                        help="The height of the wordcloud.")
    parser.add_argument("-o",
                        "--output",
                        default=None,
                        help="Save the wordcloud to a file.")

    return parser
