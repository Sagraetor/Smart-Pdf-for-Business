from pathlib import Path
from smart_pdf_for_business import PDFDocBatch
import pandas as pd


pd.set_option('display.max_columns', None)

reports = PDFDocBatch.from_folder(Path(__file__).parent / "testPdf" / "article")
result1 = reports.search_header(["abstract"])
result2 = reports.search_header(["introduction"])
print("----------Abstract---------")
print(result1.to_dataframe())
print("----------Introduction---------")
print(result2.to_dataframe())
print("----------Abstract + Introduction---------")
result3 = result1 + result2
print(result3.to_dataframe())