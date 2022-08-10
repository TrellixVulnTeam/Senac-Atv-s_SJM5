from Classe_DB import *
from tkinter import messagebox


class Back:
    def __init__(self):
        self.db = BlackDB()

    def cadas_user(self, nome, sobrenome, nome_exibicao, email, senha, frame1, frame2):
        if messagebox.askyesno('confirmar', 'salvar dados?'):
            self.db.cadas_user(nome=nome.get(), sobrenome=sobrenome.get(), nome_exibicao=nome_exibicao.get(),
                               email=email.get(), senha=senha.get())
            frame1.forget()
            frame2.pack()
            nome.delete(0, 'end')
            sobrenome.delete(0, 'end')
            nome_exibicao.delete(0, 'end')
            email.delete(0, 'end')
            senha.delete(0, 'end')
        else:
            pass

    def logar(self, entry_email, entry_senha, frame1, frame2):
        if self.db.check_user(entry_email.get(), entry_senha.get()):
            frame1.pack()
            frame2.forget()
        else:
            messagebox.showerror('Acesso Negado', 'conta desconhecida, tente novamente')

    def Deletar(self, entry_email,entry_senha, frame1, frame2):
        self.db.delete_accont(email=entry_email.get())
        frame1.pack()
        frame2.forget()
        entry_email.delete(0, 'end')
        entry_senha.delete(0, 'end')

    def mudar(self, vari, bt, x, y):
        if vari.get():
            bt.place(width=206, height=15, x=x, y=y)
        else:
            bt.place_forget()

    def Lista(self, entry_email, lb_exi, lb_nome, lb_email):
        lista = self.db.info_user(entry_email.get())
        lb_exi['text'] = f'{lista[0]}'
        lb_nome['text'] = f'{lista[1]} {lista[2]}'
        lb_email['text'] = f'{lista[3]}'

    def add_biblioteca(self, bt, jogo, x, y):
        if bt['fg'] == '#191919':
            jogo.place(width=195, height=21, x=x, y=y)
            bt['text'] = 'Remover da Biblioteca'
            bt['fg'] = '#F01F15'
        elif bt['fg'] == '#F01F15':
            jogo.place_forget()
            bt['fg'] = '#191919'
            bt['text'] = 'Adicionar a Biblioteca'

