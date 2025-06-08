from .llm import LLM, AzureOpenAILLMInterface, OpenAILLMInterface
import os

class LLMFactory:

    @staticmethod
    def get_llm_interface() -> LLM:

        local_str_llmType = os.environ["LLM_TYPE"]
        if local_str_llmType == "openai":
            return OpenAILLMInterface()
        elif local_str_llmType == "azure_openai":
            return AzureOpenAILLMInterface()
        else:
            raise ValueError(f"Unsupported LLM type: {local_str_llmType}")

