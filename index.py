import _mysql_connector as mysql
import tkinter as tk

conexao = mysql(
    host = "localhost",
    user = "root",
    password = "teste",
    database = "julio"
)

nome = input("Digite seu nome: ")
altura = input("Digite sua altura: ")

