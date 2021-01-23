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

from asreview.entry_points import BaseEntryPoint
from asreview.data import ASReviewData


def extend_stopwords(extended_words):
    """Add extra stopwords"""
    # create stopword list
    stopwords = set(STOPWORDS)
    stopwords.update(extended_words)

    return list(stopwords)


def word_cloud(words, caption=None, output_fp=None):
    """Word cloud for texts."""

    # create word cloud text
    text = " ".join(str(word) for word in words)

    # generate word cloud images
    wordcloud = WordCloud(
        stopwords=STOPWORDS,
        max_words=100,
        background_color="white"
    ).generate(text)

    # render plot
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    if caption:
        plt.set_title(caption)
    plt.axis("off")

    # save or show
    if output_fp:
        plt.savefig(output_fp, bbox_inches="tight")
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
        parser = _parse_arguments(version=f"{self.extension_name}: {self.version}")
        args = parser.parse_args(argv)

        # read data in ASReview data object
        asdata = ASReviewData.from_file(args.path)

        # all texts
        if (args.title and args.abstract) or (not args.title and not args.abstract):
            word_cloud(asdata.title, output_fp=args.output)

        # only title
        if args.title:
            word_cloud(asdata.title, output_fp=args.output)

        # only abstract
        if args.abstract:
            word_cloud(asdata.abstract, output_fp=args.output)


def _parse_arguments(version="Unknown"):
    parser = argparse.ArgumentParser(prog="asreview wordcloud")
    parser.add_argument("path",
                        type=str,
                        help="The file path of the dataset.")
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=version,
    )
    parser.add_argument(
        "--title",
        action="store_true",
        help="Create wordcloud of titles only.")
    parser.add_argument(
        "--abstract",
        action="store_true",
        help="Create wordcloud of abstracts only.")
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Save the wordcloud to a file.")

    return parser
