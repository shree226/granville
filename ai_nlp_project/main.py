

from modules.content_generator import ContentGenerator
from modules.content_refiner import ContentRefiner
from modules.bias_detector import BiasDetector

api_key = 'AIzaSyAvdw9a1RiOTpaVEfzXU5edP3e83hcf_8E' # Replace with your actual API key
generator = ContentGenerator(api_key)
refiner = ContentRefiner()
bias_detector = BiasDetector()

prompt = "Explain the importance of photosynthesis for high school students."
generated_content = generator.generate_content(prompt)
refined_content = refiner.refine_content(generated_content)
bias_checked_content = bias_detector.analyze_text(refined_content)

print("Generated Content:\n", generated_content)
print("\nRefined Content:\n", refined_content)
print("\nBiases Detected:", bias_checked_content["biases_found"])
print("\nFinal Bias-Free Content:\n", bias_checked_content["refined_text"])

