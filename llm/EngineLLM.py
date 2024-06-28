import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class LLMEngine:
    def __init__(self, model):
        models = {"mixtral": "mixtral-8x7b-32768", "llama3 8b": "llama3-8b-8192", "llama3 70b": "llama3-70b-8192"}
        self.model = models[model]

    def ocr_to_llm(self, ocr_text):
        input_text = str(ocr_text) + "  " + ("Analysez le texte et extrayez toutes les informations importantes : "
                                             "qu'un logiciel de numérisation de facture extrairait tel que le numéro"
                                             "de facture Présentez-les sous forme de paires clé-valeur, en utilisant le"
                                             "format suivant : ""{'Clé1':'Valeur1'; 'Clé2':'Valeur2'; ...}. "
                                             "Utilisez des points-virgules pour séparer ""les éléments.")

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": input_text,
                }
            ],
            model=self.model,
        )

        return chat_completion.choices[0].message.content


