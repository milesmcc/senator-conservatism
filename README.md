# Senator Conservatism
Senators across time, ranked by conservatism.

Created for Dr. Sarah Kreps.

## Data Sources
The raw DW-NOMINATE data was sourced from the official VoteView source, at ftp://k7moa.com/junkord/SL01113D21_BSSE.XLSX. It was then edited in Excel to add labels, which are visible in the file `data/data.xlsx`.

## Methodology
This dataset was created by parsing the official Senator Estimates for the 1st to 113th congresses, published on https://legacy.voteview.com/dwnomin.htm. Then, the data was fed into a custom Python script `rank.py` (https://github.com/milesmcc/senator-conservatism/blob/master/rank.py) that loads the DW-NOMINATE data and, for each congress, ranks its senators by their conservatism.

Conservatism is defined by the the senator's 1st dimension DW-NOMINATE score, where a score of 1 is considered most conservative, and -1 is considered least conservative. (The 1st dimension score generally corresponds to fiscal conservatism.)

The results are outputted the `congresses/` directory, where each congress is given its own file. The file pattern is `<number of congress>.csv`.

The outputted files rank the senators in order from most conservative to least conservative. The 67th most conservative senator (conversely, the 33rd most liberal) will be on row 68 (not 67, as row 1 is reserved for labels).

## How to Run
Simply run `python rank.py` with the current working directory set to this file's parent directory.
