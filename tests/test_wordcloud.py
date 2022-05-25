from pathlib import Path

from asreviewcontrib.wordcloud.entrypoint import word_cloud

def test_wordcloud(tmpdir):

	word_cloud(
		"benchmark:van_de_schoot2017",
		output_fp=Path(tmpdir, "demo.png")
	)
