# -*- coding: utf-8 -*-
# python 3.11
# 
APIKEY = ""    # 填入你的apikey
API_URL = "https://api.deepseek.com"

INPUT_prompt = 'You are a helpful assistant'  # 输入提示词
INPUT_message = '介绍一下你自己'                  # 输入你想要让大模型处理的信息

from openai import OpenAI

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key=APIKEY, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": str(INPUT_prompt)},
        {"role": "user", "content": str(INPUT_message)},
  ],
    max_tokens=8000,   # 最大
    temperature=1.0,   # 根据官方文档，翻译建议设置为1.3
    stream=False
)

print(response.choices[0].message.content)







