import os

import langextract as lx
import requests
from bs4 import BeautifulSoup

# Step 1: Get article text
url = "https://www.xxx.co.jp/articles/weather/12345"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

# Yahoo! News article body selector
article_text = "\n".join([p.get_text() for p in soup.select("article p")])

# Define prompt and schema guidance
prompt = """
天気の情報を抽出してください。地域、日時を含めてください。
必ず原文のまま使用し、言い換えはしないでください。
天候をその属性（地域、日時）に明確に関連付けてください。
"""

examples = [
    lx.data.ExampleData(
        text="今日の午後には四国に活発な雨雲がかかり、非常に激しい雨が降るおそれがあります。",
        extractions=[
            lx.data.Extraction(
                extraction_class="天気",
                extraction_text="激しい雨",
                attributes={
                    "地域": "四国",
                    "日時": "今日の午後"
                }
            )
        ]
    )
]

# Run the extraction
result = lx.extract(
    text_or_documents=article_text,
    prompt_description=prompt,
    examples=examples,
    model_id="gpt-4o",  # auto-selects OpenAI GPT-4o
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Save and visualize
output_file = "japanese2"
lx.io.save_annotated_documents([result], output_name=f"{output_file}.jsonl", output_dir=".")
