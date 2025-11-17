import time
from pathlib import Path
from smart_pdf_for_business import PDFDocBatch

start_time = time.time()

reports = PDFDocBatch.from_folder(Path(__file__).parent / "testPdf" / "articles")
result = reports.search_header(["abstract"])
for i, v in enumerate([report for report in reports]):
    print(v.name)

end_time = time.time()

total_time = end_time - start_time
avg_time_per_pdf = total_time / 40

print(f"Processed {40} PDFs in {total_time:.2f} seconds")
print(f"Average time per PDF: {avg_time_per_pdf:.2f} seconds")