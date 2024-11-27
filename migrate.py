import subprocess
import time

def run_migrations():
    """
    Verifica se o banco de dados está acessível e executa as migrações do Django.
    """
    db_ready = False
    retries = 10
    delay = 5  # segundos entre as tentativas

    print("Aguardando o banco de dados ficar pronto...")

    for i in range(retries):
        try:
            # Teste de conexão com o banco de dados
            subprocess.run(
                ["pg_isready", "-h", "db", "-p", "5432", "-U", "postgres"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            db_ready = True
            print("Banco de dados está pronto!")
            break
        except subprocess.CalledProcessError:
            print(f"Tentativa {i + 1}/{retries} falhou. Tentando novamente em {delay} segundos...")
            time.sleep(delay)

    if not db_ready:
        print("Erro: O banco de dados não ficou pronto a tempo.")
        exit(1)

    print("Executando migrações do Django...")
    try:
        subprocess.run(
            ["python", "manage.py", "migrate"],
            check=True,
        )
        print("Migrações concluídas com sucesso!")
    except subprocess.CalledProcessError as e:
        print("Erro ao executar migrações:", e)
        exit(1)

if __name__ == "__main__":
    run_migrations()
