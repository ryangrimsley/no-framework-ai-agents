import requests
import json

class OllamaModel:
    def __init__(self, model, system_prompt, temperature=0, stop=None):
        """
        Initializes the OllamaModel with the given parameters.

        Parameters:
        model (str): The name of the model to use.
        system_prompt (str): The system prompt to use.
        temperature (float): The temperature setting for the model.
        stop (str): The stop token for the model.
        """
        self.model_endpoint = "http://localhost:11434/api/generate"
        self.temperature = temperature
        self.model = model
        self.system_prompt = system_prompt #make sure to specify result must be in JSON in system prompt
        self.headers = {"Content-Type": "application/json"}
        self.stop = stop

    def generate_json(self, prompt):
        """
        Generates a response from the Ollama model based on the provided prompt.

        Parameters:
        prompt (str): The user query to generate a response for.

        Returns:
        dict: The response from the model as a dictionary.
        """
        payload = {
            "model": self.model,
            "format": "json",
            "prompt": prompt,
            "system": self.system_prompt,
            "stream": False,
            "options": {"temperature": self.temperature, 
                        "seed": 42},
            "stop": self.stop
        }

        try:
            print("Thinking...")
            request_response = requests.post(
                self.model_endpoint, 
                headers=self.headers, 
                data=json.dumps(payload)
            )
            
            print(f"REQUEST RESPONSE {request_response} -- time elapsed: {request_response.elapsed}")
            request_response_json = request_response.json()
            #if there is no error with ollama
            if not request_response_json.get("error"):

                response = request_response_json['response']
                response_dict = json.loads(response)
                print(f"\n\nResponse from Ollama model: {response}")
                return response_dict
            #if there is an error, raise an exception
            else:
                raise requests.RequestException(request_response_json.get('error'))
            
        except requests.RequestException as e:
            response = {"error": f"Error in invoking model! {str(e)}"}
            return response
        
