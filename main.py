# bank_system.py

from bank_operations import withdraw, deposit, get_statement

def main():
    while True:
        print("\n=== Sistema Bancário ===")
        print("1 - Saque")
        print("2 - Depósito")
        print("3 - Visualizar Extrato")
        print("4 - Sair")

        user_operation = input("Escolha uma operação: ")

        if user_operation == "1":
            withdraw()
        elif user_operation == "2":
            deposit()
        elif user_operation == "3":
            get_statement()
        elif user_operation == "4":
            print("Encerrando sistema. Até logo! 👋")
            break
        else:
            print("❌ Opção inválida! Digite um número entre 1 e 4.")


if __name__ == "__main__":
    main()