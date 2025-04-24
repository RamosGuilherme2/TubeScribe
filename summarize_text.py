import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_resumo(texto):
    resposta = openai.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "system",
                "content": (
                    "Objetivo: Resumo detalhado e estruturado.\n"
                    "Por favor, resuma de forma detalhada o conteúdo do texto fornecido, "
                    "estruturando as informações em tópicos e subtópicos claros. Certifique-se de:\n"
                    "- Incluir todos os detalhes relevantes.\n"
                    "- Organizar o conteúdo de maneira lógica e coesa.\n"
                    "- Apresentar o resumo em um formato que facilite o estudo aprofundado e a compreensão total do tema abordado.\n"
                    "O formato do texto deve ser informativo, claro e voltado para o aprendizado, com prioridade na organização e clareza das ideias."
                )
            },
            {
                "role": "user",
                "content": texto
            }
        ]
    )
    return resposta["choices"][0]["message"]["content"]
