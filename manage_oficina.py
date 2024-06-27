class Produto:

    def __init__(self, codigo, descricao, categoria, preco, estoque):
        self.codigo = codigo
        self.descricao = descricao
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque

    def get_codigo(self):
        return self.codigo

    def get_descricao(self):
        """
        Retorna a descrição do produto.
        """
        return self.descricao

    def get_categoria(self):
        return self.categoria

    def get_preco(self):
        return self.preco

    def get_estoque(self):
        return self.estoque

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_categoria(self, categoria):
        self.categoria = categoria

    def set_preco(self, preco):
        self.preco = preco

    def set_estoque(self, estoque):
        self.estoque = estoque


def cadastrar_produto(produtos):
    while True:
        try:
            codigo = int(input("Código: "))
            break
        except ValueError:
            print("Código inválido. Digite um número inteiro.")

    while True:
        descricao = input("Descrição: ")
        if descricao:
            break
        else:
            print("Descrição não pode ser vazia.")

    while True:
        categoria = input("Categoria: ")
        if categoria:
            break
        else:
            print("Categoria não pode ser vazia.")

    while True:
        try:
            preco = float(input("Preço: "))
            if preco >= 0:
                break
            else:
                print("Preço inválido. Digite um valor positivo ou zero.")
        except ValueError:
            print("Preço inválido. Digite um número decimal separado por pontos.")

    while True:
        try:
            estoque = int(input("Estoque: "))
            if estoque > 0:
                break
            else:
                print("Estoque inválido. Digite um número inteiro positivo ou zero.")
        except ValueError:
            print("Estoque inválido. Digite um número inteiro.")

    produtos.append(Produto(codigo, descricao, categoria, preco, estoque))

    print("Produto cadastrado com sucesso!")


def listar_produtos(produtos):
    if not produtos:
        print("Não há produtos cadastrados.")
        return

    print("Lista de Produtos")
    print("------------------")

    for produto in produtos:
        print(f"Código: {produto.get_codigo()}")
        print(f"Descrição: {produto.get_descricao()}")
        print(f"Categoria: {produto.get_categoria()}")
        print(f"Preço: {produto.get_preco()}")
        print(f"Estoque: {produto.get_estoque()}")
        print("------------------")


def editar_produto(produtos):
    codigo = int(input("Código do produto a ser editado: "))

    produto = next((p for p in produtos if p.get_codigo() == codigo), None)

    if not produto:
        print("Produto não encontrado.")
        return

    print(f"Descrição: [{produto.get_descricao()}]: ")
    produto.set_descricao(input())

    print(f"Categoria: [{produto.get_categoria()}]: ")
    produto.set_categoria(input())

    print(f"Preço: [{produto.get_preco()}], ")
    produto.set_preco(float(input()))

    print(f"Estoque: [{produto.get_estoque()}]: ")
    produto.set_estoque(int(input()))

    print("Produto editado com sucesso!")


def remover_produto(produtos):
    codigo = int(input("Código do produto a ser removido: "))

    produto = next((p for p in produtos if p.get_codigo() == codigo), None)

    if not produto:
        print("Produto não encontrado.")
        return

    produtos.remove(produto)

    print("Produto removido com sucesso!")


def main():
    produtos = []  # Vetor para armazenar os produtos

    while True:
        print("\nGerenciamento de Produtos")
        print("------------------------")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Editar Produto")
        print("4. Remover Produto")
        print("5. Sair")
        print("Opção: ", end="")
        opcao = int(input())

        if opcao == 1:
            cadastrar_produto(produtos)
        elif opcao == 2:
            listar_produtos(produtos)
        elif opcao == 3:
            editar_produto(produtos)
        elif opcao == 4:
            remover_produto(produtos)
        elif opcao == 5:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
