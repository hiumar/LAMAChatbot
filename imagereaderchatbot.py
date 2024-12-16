# -*- coding: utf-8 -*-
"""ImageReaderChatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18lI3nZCL0LecsdLwrai9CiPbnL_oKWcJ
"""

import google.generativeai as genai
genai.configure(api_key="AIzaSyBt6fdoOnj5L1p74aio7QTsSpzfuQ5Lc5E")
model_name="gemini-1.5-flash"
model=genai.GenerativeModel(model_name)
import PIL.Image as img;

image=img.open("AbuDhabi.jpeg")
prompt="explain this image"

response=model.generate_content([image,prompt])
print(response.text)
