from doctr.io import DocumentFile
from doctr.models import ocr_predictor
from fastapi import FastAPI

def ocrFunction():
  file = "Cash-Payment-Receipt-Template.pdf"
  #file = "KTP_Radit.jpg"

  if file.lower().endswith(".pdf"):
    doc = DocumentFile.from_pdf(file)
  else:
    doc = DocumentFile.from_images(file)

  print(f"Number of pages: {len(doc)}")
  model = ocr_predictor(pretrained=True)
  out = model(doc)

  for page, img in zip(out.pages, doc):
    page.show(img, block="false")

  json_output = out.export()

  text = out.render()
  return text

app = FastAPI()

@app.get("/getOCR")
async def root():
  message = "Success"
  code = 200
  data = ocrFunction()
  return {
      "message": message,
      "status" : code,
      "data" : data
}

#ocr tutorial link : https://colab.research.google.com/drive/1ZPQwneM29k9Pf1nyF_q6pNZwylVIK9u_#scrollTo=jO-Ktj_we_9Z