import google.generativeai as generativeaiimport PIL.imageimport jsonify
CONFIG = {
 "temperature": 0.4,
  "max_output_tokens": 150,
}

genai.configure(api_key="")
model = genai.GenerativeModel(model_name='gemini-pro-vision', generation_config=CONFIG)


def getData(image):
    result = model.generate_content([
    """You are a vision data extraction API capable of extracting data from an image. 
  extract date, time, total amount, merchant name, address, city and number about the receipt in the image.
        Please respond with follow the JSON format without any formatting or char.
     The JSON schema should include:
          {
            "date": "yyyy:mm:dd",
            "time": "hh:mm:ss",
            "total": double,
            "city": "string",
            "coutry": "string",
            "address": "string",
         "merchant_name": "string",
            "number": "string"
          }""", PIL.Image.open(image)])
    
    data = result.text.strip()
    open = data.find('{')
    close = data.rfind('}')+1. data = data[open:close]
    print(data)
    return json.loads(data)


if(__name__ == "__main__"):
    d=getData('f.jpg')
    
    for e in d:
        print(f"{e}: {d[e]}")

