import requests
import json

class ContentGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

    def ask_gemini(self, prompt):
       
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }
        
        headers = {
            'Content-Type': 'application/json'
        }

        
        response = requests.post(f"{self.url}?key={self.api_key}", headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            response_data = response.json()
           
            generated_content = response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            return generated_content
        else:
            return f"Error: {response.status_code}, {response.text}"
    
    def generate_content(self, prompt):
        return self.ask_gemini(prompt)


if __name__ == "__main__":
    api_key = 'AIzaSyAvdw9a1RiOTpaVEfzXU5edP3e83hcf_8E'  
    generator = ContentGenerator(api_key)
    prompt = "Explain the importance of photosynthesis for high school students."
    print(generator.generate_content(prompt))
api_key = 'AIzaSyAvdw9a1RiOTpaVEfzXU5edP3e83hcf_8E'
generator = ContentGenerator(api_key)  

def generate_content(prompt):
    return generator.ask_gemini(prompt)
