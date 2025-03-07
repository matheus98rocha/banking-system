# bank_operations.py

user_balance = 0.0
transactions = []
withdraws_by_day = 0 

LIMIT_WITHDRAW = 3
MAX_WITHDRAW_AMOUNT = 500.0


def verify_withdraw_rules(withdraw_amount):
    if withdraw_amount > MAX_WITHDRAW_AMOUNT:
        print("❌ São permitidos saques de no máximo R$ 500,00.")
        return False

    if withdraw_amount > user_balance:
        print("❌ Saldo insuficiente para realizar o saque.")
        return False

    if withdraw_amount <= 0:
        print("❌ Valor inválido!")
        return False

    return True


def withdraw():
    global user_balance, withdraws_by_day

    if withdraws_by_day >= LIMIT_WITHDRAW:
        print("❌ Limite diário de saques atingido!")
        return

    try:
        withdraw_amount = float(input("Digite o valor do saque: ").replace(",", "."))

        # Verificando se o saque pode ser feito
        if not verify_withdraw_rules(withdraw_amount):
            return

        user_balance -= withdraw_amount
        withdraws_by_day += 1
        transactions.append({"type": "Saque", "amount": withdraw_amount})

        print(f"✅ Saque de R$ {withdraw_amount:.2f} realizado com sucesso!")

    except ValueError:
        print("❌ Entrada inválida! Digite um número válido.")


def deposit():
    global user_balance

    try:
        deposit_amount = float(input("Digite o valor do depósito: ").replace(",", "."))

        if deposit_amount <= 0:
            print("❌ Valor inválido!")
            return

        user_balance += deposit_amount
        transactions.append({"type": "Depósito", "amount": deposit_amount})

        print(f"✅ Depósito de R$ {deposit_amount:.2f} realizado com sucesso!")

    except ValueError:
        print("❌ Entrada inválida! Digite um número válido.")


def get_statement():
    print("\n--- Extrato ---")

    if not transactions:
        print("Nenhuma movimentação registrada.")
    else:
        for i, transaction in enumerate(transactions, 1):
            print(f"{i}. {transaction['type']}: R$ {transaction['amount']:.2f}")

    print(f"Saldo atual: R$ {user_balance:.2f}")
    print("-----------------\n")