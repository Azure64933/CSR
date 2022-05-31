import pandas as pd


def excel_export(Lst1, Lst2, Lst3):
    list1 = Lst1
    list2 = Lst2
    list3 = Lst3
    col1 = "原始TXT檔"
    col2 = "Comb轉換比率"
    col3 = "Segm轉換比率"
    data = pd.DataFrame({col1: list1, col2: list2, col3: list3})
    data.to_excel('Conversion_ratio.xlsx', sheet_name='sheet1', index=False)
