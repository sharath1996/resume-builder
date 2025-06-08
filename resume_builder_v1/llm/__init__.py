from .llm import LLM, AzureOpenAILLMInterface, OpenAILLMInterface


class LLMFactory:

    @staticmethod
    def get_llm_interface(param_str_llmType: str) -> LLM:
        if param_str_llmType == "openai":
            return OpenAILLMInterface()
        elif param_str_llmType == "azure_openai":
            return AzureOpenAILLMInterface()
        else:
            raise ValueError(f"Unsupported LLM type: {param_str_llmType}")

