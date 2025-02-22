from dotenv import load_dotenv
import os

load_dotenv()  # .env を読み込む

print(os.getenv("OPENAI_API_KEY"))  # my_value