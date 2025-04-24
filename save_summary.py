def salvar_resumo(texto, arquivo="resumo.txt"):
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(texto)
        