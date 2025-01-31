import re
import nltk
from nltk.tokenize import sent_tokenize


nltk.download('punkt')

class ContentRefiner:
    def __init__(self):
        pass

    def clean_text(self, text):
        """Removes unnecessary spaces, multiple newlines, and special characters."""
        text = re.sub(r'\s+', ' ', text)  
        text = re.sub(r'\n+', '\n', text)  
        return text.strip()

    def improve_readability(self, text):
        """Splits long sentences and simplifies structure if needed."""
        sentences = sent_tokenize(text)
        refined_sentences = [self.simplify_sentence(sentence) for sentence in sentences]
        return " ".join(refined_sentences)

    def simplify_sentence(self, sentence):
        """A placeholder for sentence simplification (can be expanded later)."""
        return sentence 

    def refine_content(self, text):
        """Applies all refinement steps."""
        text = self.clean_text(text)
        text = self.improve_readability(text)
        return text


if __name__ == "__main__":
    refiner = ContentRefiner()
    sample_text = "  Photosynthesis is the process where plants make food.   It uses sunlight, carbon dioxide, and water.\n\n\n It occurs in chloroplasts.  "
    print(refiner.refine_content(sample_text))




refiner = ContentRefiner()

def refine_text(text):
    return refiner.refine_content(text)

def refine_content(self, text):
        """Applies all refinement steps."""
        text = self.clean_text(text)
        text = self.improve_readability(text)
        return text