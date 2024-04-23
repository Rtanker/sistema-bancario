import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class SistemaBancario:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bancário")

        # Variáveis
        self.saldo = 0
        self.transacoes = []

        # Labels
        self.label_saldo = tk.Label(root, text="Saldo: R$0.00", font=("Arial", 12))
        self.label_saldo.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        # Botões
        self.button_depositar = tk.Button(root, text="Depositar", command=self.depositar)
        self.button_depositar.grid(row=1, column=0, padx=10, pady=5, sticky="we")

        self.button_sacar = tk.Button(root, text="Sacar", command=self.sacar)
        self.button_sacar.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        self.button_extrato = tk.Button(root, text="Visualizar Extrato", command=self.visualizar_extrato)
        self.button_extrato.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we")

    def depositar(self):
        deposito = float(simpledialog.askstring("Depositar", "Digite o valor a ser depositado:"))
        if deposito > 0:
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.transacoes.append((data_hora, f"Depósito de R${deposito:.2f}"))
            self.saldo += deposito
            self.atualizar_saldo()
            messagebox.showinfo("Sucesso", f"Depósito de R${deposito:.2f} realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Valor de depósito inválido!")

    def sacar(self):
        if len([transacao for transacao in self.transacoes if "Saque" in transacao[1]]) < 3:
            saque = float(simpledialog.askstring("Sacar", "Digite o valor a ser sacado:"))
            if saque > 0 and saque <= 500 and saque <= self.saldo:
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                self.transacoes.append((data_hora, f"Saque de R${saque:.2f}"))
                self.saldo -= saque
                self.atualizar_saldo()
                messagebox.showinfo("Sucesso", f"Saque de R${saque:.2f} realizado com sucesso!")
            elif saque > self.saldo:
                messagebox.showerror("Erro", "Saldo insuficiente para realizar o saque!")
            else:
                messagebox.showerror("Erro", "Valor de saque inválido!")
        else:
            messagebox.showerror("Erro", "Limite de saques diários atingido!")

    def visualizar_extrato(self):
        extrato = "Extrato:\n"
        for transacao in sorted(self.transacoes, key=lambda x: datetime.strptime(x[0], "%d/%m/%Y %H:%M:%S")):
            extrato += f"{transacao[1]} - Data: {transacao[0]}\n"
        extrato += f"Saldo atual: R${self.saldo:.2f}"
        messagebox.showinfo("Extrato", extrato)

    def atualizar_saldo(self):
        self.label_saldo.config(text=f"Saldo: R${self.saldo:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    SistemaBancario(root)
    root.mainloop()
