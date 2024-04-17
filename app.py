from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

AZURE_MODEL_DEPLOYMENT = (
    os.environ.get() | "gpt35t"
)  # for example, my model deployment is gpt35k.


model = AzureChatOpenAI(model=AZURE_MODEL_DEPLOYMENT)

message = HumanMessage(
    content="Tanslate this sentence from English to French, I love programming."
)

response = model.invoke([message])
print(response.content)
