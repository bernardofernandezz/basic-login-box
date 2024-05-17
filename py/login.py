from customtkinter import*

tela = CTk()
tela.geometry ("500x400")

title = CTkLabel(tela, text="Sistema de Login", font=("Arial",20)).pack(pady=20)

user = CTkEntry(tela, placeholder_text= "User name...", width=300).pack(pady=20)

password = CTkEntry(tela, placeholder_text="Password..", width=300, show="*").pack()

checkbox = CTkCheckBox(tela, text="Lembrar de Mim").place (x=100, y=180 )

button = CTkButton (tela, text="Login", width=300).pack(pady="70")

tela.mainloop()