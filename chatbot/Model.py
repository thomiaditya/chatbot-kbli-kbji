from abc import ABC, abstractmethod

class GenerativeModel(ABC):
    @abstractmethod
    async def generate_text(self, prompt: str|list) -> str:
        """Generates text based on a given prompt with optional control over length and creativity.

        Args:
            prompt: The initial text or starting point for generation.

        Returns:
            The generated text string.
        """

class EmbeddingModel(ABC):
    @abstractmethod
    async def get_embedding(self, text: str):
        """
        Abstract method to get the embedding of a given text.

        Parameters:
            text (str): The input text for which embedding is required.

        Returns:
            Any: The embedding of the input text.
        """
    