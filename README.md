# Senator Conservatism
Senators across time, ranked by conservatism.

Created for Dr. Sarah Kreps.

## Data Sources
The raw DW-NOMINATE data was sourced from the official VoteView source, at ftp://k7moa.com/junkord/SL01113D21_BSSE.XLSX. It was then edited in Excel to add labels, which are visible in the file `data/data.xlsx`.

## Methodology
The Python program `rank.py` loads the DW-NOMINATE data and, for each congress, ranks its senators by their conservatism. Conservatism is defined by the the senator's 1st dimension DW-NOMINATE score, where a score of 1 is considered most conservative, and -1 is considered least conservative.

The results are outputted the `congresses/` directory.

## How to Run
Simply run `python rank.py` with the current working directory set to this file's parent directory.
