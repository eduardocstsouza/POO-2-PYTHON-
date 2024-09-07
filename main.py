class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao


livro1 = Livro("Orgulho e Preconceito", "Jane Austen", "1813")
livro2 = Livro("O Alquimista", "Paulo Coelho", "1988")
livro3 = Livro("1984", "George Orwell", "1949")

print(livro1.titulo, livro1.autor,  livro1.ano_publicacao)
print(livro2.titulo, livro2.autor,  livro2.ano_publicacao)
print(livro3.titulo, livro3.autor,  livro3.ano_publicacao)

class produto:
    def __init__(self, *args, **kwargs):
        if len(args) >= 1:
            self.nome = args[0]
        else:
            self.nome = kwargs.get ("Nome", "Sem Nome")
        if len(args) >= 2:
            self.preco = args[1]
        else:
            self.preco = kwargs.get("preco", 0)

    def __str__(self):
        return f'produto: {self.nome}, Preço: R${self.preco:.2f}'  
   

produto1 = produto("Notebook", 1500.00)
produto2 = produto ("Tablet")


print(produto1)
print(produto2)

        
