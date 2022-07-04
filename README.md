# <h1> CSR 
CSR全名為（Corporate Social Responsibility)，意旨企業社會責任。

## <h2> Table of Contents </h2>
- [Introduce](#Introduce)
	- [The purpose](#The-purpose)
	- [Pre-preparation](#Pre-preparation)
	- [Result](#Result)
- [Getting started](#Getting-started)
	- [main](#main)
	- [Combine](#Combine)
	- [Segment](#Segment)
- [Result](#Result)

## Introduce 

### The purpose
此專案的目的是將純文字檔(.txt)轉譯可以進行語意分析的檔案。

### Pre-preparation
1. 蒐集純文字檔(.txt):

此專案蒐集自民國99年至今、不同公司的CSR報告書。由於一般CSR報告書為pdf檔，因此須將pdf檔轉檔成txt檔才能進行後續的語意分析。

2. 存放資料：

將資料存放於`CSR_REPORT_TXT/`檔案路徑底下。可在`CSR_REPORT_TXT/`底下存放多個資料夾。

### Result
-  Combine
將所有句子接上的`"FileName"_Comb`儲存於`Fin/Combine/`

- Segment
將`"FileName"_Comb`切割後的`"FileName"_Seg`儲存於`Fin/Segment/`

- Excel
有Comb/TXT, Segm/TXT, Segm/Comb三種比例，可以確認純文字檔(.txt)經過處理後剩餘的文字比例。

## Getting started
### main

----------

預設為執行`CSR_REPORT_TXT/`檔案路徑底下的`109_txt`資料夾。

可透過修改下列的`109_txt`更改選擇執行的資料夾。

```
main("109_txt")
```

### Combine

----------

大部分的"企業社會責任報告書"是PPT，將PPT轉成純文字後會導致句子有許多不合理的斷句。

本專案透過`cogs/combine.py`將斷句接上。

##### 合併判斷基準：
- 當段落中有spe_str中的特殊符號時，便判斷該段落為句子，將該段落與下一段落進行合併。

- 當該段落的結尾有"。"、"！"、"？"三種符號時，判斷該段落為一段話的結尾，進行換行的動作。

### Segment

----------


由於合併判斷基準(2)會導致部分句子無法Combine，因此會重新Combine一次。

"企業社會責任報告書"中有許多表格數據，這些表格數據無法進行文字分析，於是將其刪除。

本專案透過`cogs/segment.py`將`Fin/Combine/`中的句子重新分為不同段落。


##### 分段判斷基準：
- 當段落中"."的數量超過六個，判斷為目錄將其刪除。

- 當段落中字數少於12個，判斷該段落並非句子將其刪除。

- 當該段落沒有"。"，判斷該段落並非句子將其刪除。

- 將符合條件的段落中，以"。"為基準進行分段。


## Result
- 原始文章完整：
Excel中 Segm/TXT, Segm/Comb兩個欄位的值通常會有4成到7成的成果。

- 原始文章缺損：
原始文章可能為空值或亂碼，Excel中 Segm/TXT, Segm/Comb兩個欄位的值趨近0。


