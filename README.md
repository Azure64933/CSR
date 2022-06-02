# CSR

此專案為個人練習專案。

此專案的目的是將CSR轉化成可以進行文字分析的檔案。

企業社會責任（Corporate Social Responsibility, 簡稱CSR）
此專案將各個企業的"企業社會責任報告書"轉成Combine以及Segment兩個部分。


## <h2> Getting started

將code clone之後，執行main便會將`CSR_TXT_TEST`中所有的TXT檔案進行轉換。(之所以會是`CSR_TXT_TEST`而非`CSR_REPORT_TXT`底下的TXT，是因為目前轉換結果仍在修改)

轉換過後的結果將儲存在Fin資料夾底下，分別為Combine以及Segment兩個部分。

## Combine

大部分的"企業社會責任報告書"是PPT，將PPT轉成純文字後會導致句子有許多不合理的斷句。

本專案透過`cogs/combine.py`將斷句接上。

### 合併判斷基準：

1.當段落中有spe_str中的特殊符號時，便判斷該段落為句子，將該段落與下一段落進行合併。

2.當該段落的結尾有"。"、"！"、"？"三種符號時，判斷該段落為一段話的結尾，進行換行的動作。


## Segment

由於合併判斷基準(2)會導致部分句子無法Combine，因此會重新Combine一次。

"企業社會責任報告書"中有許多表格數據，這些表格數據無法進行文字分析，於是將其刪除。

本專案透過`cogs/segment.py`將`Fin/Combine/`中的句子重新分為不同段落。


### 分段判斷基準：

1.當段落中"."的數量超過六個，判斷為目錄將其刪除。

2.當段落中字數少於12個，判斷該段落並非句子將其刪除。

3.當該段落沒有"。"，判斷該段落並非句子將其刪除。

4.將符合條件的段落中，以"。"為基準進行分段。


## <h2> Result

1.轉換結果將儲存於`Fin`資料夾底下

2.於原本資料夾底下生成檔名為Conversion_ratio的xlsx，裡面紀錄文字的轉換率