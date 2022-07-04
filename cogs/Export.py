import pandas as pd


def excel_export(Lst1, Lst2, Lst3, Lst4, Name):
    list1 = Lst1
    list2 = Lst2
    list3 = Lst3
    list4 = Lst4
    col1 = "原始TXT檔"
    col2 = "Comb/TXT"
    col3 = "Segm/TXT"
    col4 = "Segm/Comb"
    data = pd.DataFrame({col1: list1, col2: list2, col3: list3, col4: list4})
    xlsx = Name + ".xlsx"
    data.to_excel(xlsx, sheet_name='sheet1', index=False)
