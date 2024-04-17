# Using Azure OpenAI in LangChain

OpenAI's LLM is used by default in LangChain. in order for you to use Azure's Openai API in LangChain, I made this example.
It can be used as a starting point for your project.


## Running locally
1. clone the repo.
2. run `pip install`
3. Add `.env` file to the root directory with the following content:
    ```yaml
    AZURE_OPENAI_API_KEY=<your azure openai key>
    OPENAI_API_VERSION=<api version> #eg: 2024-02-15-preview
    AZURE_OPENAI_ENDPOINT=<your azure openai endpoint> #eg: https://<azure resource>.openai.azure.com/
    ```
    All these information are shown on your Azure Openai Portal.
4. run `python app.py`
