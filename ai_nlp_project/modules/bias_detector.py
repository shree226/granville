import re
import spacy
import os

class BiasDetector:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        # List of potentially biased terms and their neutral replacements
        self.bias_words = {
            "he": "they",
            "she": "they",
            "manpower": "workforce",
            "chairman": "chairperson",
            "mankind": "humankind",
            "disabled person": "person with a disability",
            "foreigner": "non-local"
        }

    def detect_bias(self, text):
        """Identifies biased words/phrases in the text."""
        doc = self.nlp(text)
        biases_found = [word for word in self.bias_words if word in text.lower()]
        return biases_found

    def mitigate_bias(self, text):
        """Replaces biased words with neutral alternatives."""
        for biased_word, neutral_word in self.bias_words.items():
            text = re.sub(rf"\b{biased_word}\b", neutral_word, text, flags=re.IGNORECASE)
        return text

    def analyze_text(self, text):
        """Runs both bias detection and mitigation."""
        biases_found = self.detect_bias(text)
        if biases_found:
            text = self.mitigate_bias(text)
        return {"biases_found": biases_found, "refined_text": text}


# Global instance for easy import (in other files)
bias_detector = BiasDetector()

def check_bias(text):
    return bias_detector.detect_bias(text)

# Example usage
if __name__ == "__main__":
    sample_text = "The chairman said that manpower is essential for mankind."
    result = bias_detector.analyze_text(sample_text)

    print("Biases Detected:", result["biases_found"])
    print("\nRefined Text:\n", result["refined_text"])

def detect_bias(self, text):
        """Identifies biased words/phrases in the text."""
        doc = self.nlp(text)
        biases_found = [word for word in self.bias_words if word in text.lower()]
        return biases_found