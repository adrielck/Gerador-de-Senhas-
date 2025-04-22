import random
import string

def gerar_senha(tamanho=12):
    """Gera uma senha segura com letras, números e símbolos."""
    if tamanho < 6:
        raise ValueError("O tamanho da senha deve ser pelo menos 6 caracteres.")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    try:
        tamanho = int(input("Informe o tamanho da senha desejada (mínimo 6): "))
        senha = gerar_senha(tamanho)
        print(f"Senha gerada: {senha}")
    except ValueError as e:
        print(f"Erro: {e}")
