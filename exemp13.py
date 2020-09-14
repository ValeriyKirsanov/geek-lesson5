# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
exemp = input("input text")
out_f = open("text.txt", "w")
out_f.write(exemp)

out_f.close()
