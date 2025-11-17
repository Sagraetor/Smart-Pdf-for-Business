from pathlib import Path
from smart_pdf_for_business import PDFDoc

file = "Bai_Re-Ranking_via_Metric_Fusion_for_Object_Retrieval_and_Person_Re-Identification_CVPR_2019_paper.pdf"
report = PDFDoc.from_file(Path(__file__).parent / "testPdf" / "article" / file)
result1 = report.search_header(["abstract"], as_tuple=True)
print(result1)
print("----------")
result2 = report.search_body(["limitations"], as_tuple=True)
print(result2)
print("----------")
result3 = report.search_by_meaning("writer", as_tuple=True, chunk_by="semantic")
print(result3)