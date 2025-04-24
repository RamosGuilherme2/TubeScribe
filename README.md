## TubeScribe 🎥📝
Um programa para transcrição e resumo automatizado de vídeos do YouTube!
## 📋 Descrição do Projeto
TubeScribe é uma ferramenta que permite baixar o áudio de vídeos do YouTube, transcrever o conteúdo automaticamente e gerar resumos detalhados e estruturados para facilitar o estudo ou a análise dos temas abordados nos vídeos.
Com foco em simplicidade e eficiência, o programa foi projetado para remover automaticamente arquivos temporários após o uso, garantindo a organização e o bom uso de recursos.

## 🚀 Recursos
- Download automático do áudio: Obtém o áudio dos vídeos do YouTube no formato MP3.
- Transcrição automatizada: Converte o áudio em texto utilizando tecnologias de reconhecimento de voz (Whisper).
- Geração de resumos detalhados: Produz resumos organizados em tópicos e subtópicos para facilitar o estudo.
- Processamento limpo: Exclui arquivos temporários automaticamente após o processamento.


## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.8+
- **Bibliotecas Principais:**- yt-dlp: Para download de áudio de vídeos do YouTube.
- **whisper:** Para transcrição de áudio em texto.
- **openai:** Para geração de resumos usando a API OpenAI (GPT-4.1).
- **ffmpeg:** Para manipulação de arquivos de áudio.

- **Gerenciamento de dependências:** pip e venv.


## 📂 Estrutura do Projeto
```bash
📁 TubeScribe/
├── 📄 tubescribe.py           # Arquivo principal que executa o programa.
├── 📄 download_audio.py       # Função para baixar o áudio do vídeo.
├── 📄 transcribe_audio.py     # Função para transcrição do áudio.
├── 📄 summarize_text.py       # Função para gerar resumos utilizando a API OpenAI.
├── 📄 save_summary.py         # Função para salvar o resumo gerado.
├── 📄 requirements.txt        # Arquivo com as dependências do projeto.
└── 📄 README.md               # Documentação do projeto.
```

## 🖥️ Instalação e Execução
Pré-requisitos
- **Python 3.8+** instalado no sistema.
- Instale o gerenciador de dependências **pip**.
- **ffmpeg** instalado (obrigatório para manipular arquivos de áudio).

**Passos de Instalação**
```bash
# Clone o repositório:
git clone https://github.com/RamosGuilherme2/TubeScribe.git
cd TubeScribe

# Crie e ative um ambiente virtual:
python -m venv .venv
source .venv/bin/activate  
# No Windows: 
.venv\Scripts\activate

# Instale as dependências:
pip install -r requirements.txt

# Configure sua chave de API do OpenAI no arquivo .env:
OPENAI_API_KEY=your_api_key_here


# Certifique-se de que o ffmpeg está instalado e acessível pelo terminal.

## Como executar
# Rode o programa com:
python tubescribe.py

# Insira a URL do vídeo do YouTube quando solicitado e acompanhe o processamento.
```

## 🧪 Testes
- Exemplo de URL para teste:
Experimente usar o programa com vídeos curtos para validar o fluxo (ex.: TED Talks ou vídeos educacionais de até 10 minutos).
- Certifique-se de que arquivos temporários estão sendo removidos corretamente ao final do processo.


## 📄 Licença
Este projeto está licenciado sob a MIT License. Sinta-se à vontade para utilizá-lo e modificá-lo conforme suas necessidades.

## 🙌 Contribuições
Contribuições são bem-vindas! Para contribuir:
- Faça um fork do repositório.
- Crie um branch para sua feature ou correção:git checkout -b minha-feature

- Envie um pull request para avaliação.


## 📧 Contato
Se tiver dúvidas, sugestões ou feedback, sinta-se à vontade para entrar em contato:
- LinkedIn: https://www.linkedin.com/in/guilherme-ramos-90517b235/



