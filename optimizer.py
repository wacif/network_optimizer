import openai
from config import API_KEY, BASE_URL
from utils import handle_api_error

class NetworkOptimizer:
    def __init__(self):
        self.client = openai.OpenAI(api_key=API_KEY, base_url=BASE_URL)

    def optimize_network(self, devices):
        try:
            response = self.client.chat.completions.create(
                model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
                messages=[
                    {"role": "system", "content": "You are a network optimization AI."},
                    {"role": "user", "content": f"Optimize the following network stats: {devices}."}
                ]
            )
            return response.choices[0].message.content

        except openai.error.OpenAIError as e:
            handle_api_error(e)
            return None
