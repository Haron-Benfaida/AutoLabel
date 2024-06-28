import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class LLMEngine:
    def __init__(self, model):
        models = {"mixtral": "mixtral-8x7b-32768", "llama3 8b": "llama3-8b-8192", "llama3 70b": "llama3-70b-8192"}
        self.model = models[model]

    def ocr_to_llm(self, ocr_text):
        input_text = str(ocr_text) + "  " + ("Analysez méticuleusement le texte précédent et extrayez-en toutes les informations "
                             "pertinentes que vous pouvez identifier avec certitude. Ne vous limitez pas à une liste"
                             " prédéfinie d'éléments, mais assurez-vous que chaque information extraite correspond "
                             "exactement à un élément présent dans le document original. Cela peut inclure, entre autres,"
                             " le nom de l'entreprise, la date, l'ICE, le numéro de téléphone, le total à payer, et tout"
                             " autre élément que vous jugez important et qui figure explicitement dans le texte.Présentez"
                             " ces informations sous forme de paires clé-valeur, en utilisant le format suivant : "
                             "{'Clé1':'Valeur1'; 'Clé2' : 'Valeur2'; 'Clé3' : 'Valeur3'; ...}. Utilisez des points-virgules "
                             "pour séparer les éléments. Important : N'ajoutez aucune information qui ne serait pas "
                             "directement présente dans le document original. Chaque valeur extraite doit correspondre "
                             "exactement à un texte existant dans le document, car ces informations seront ensuite mappées"
                             " sur l'image du document.")

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


