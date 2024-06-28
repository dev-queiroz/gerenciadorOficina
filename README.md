# Sistema de Gerenciamento de Produtos para Oficina

Este é um sistema simples de gerenciamento de produtos em Python. Ele permite cadastrar, listar, editar e remover produtos. Abaixo estão as principais funcionalidades:

## Classe `Produto`

A classe `Produto` representa um item no estoque. Ela possui os seguintes atributos:

- `codigo`: o código único do produto.
- `descricao`: uma breve descrição do produto.
- `categoria`: a categoria à qual o produto pertence.
- `preco`: o preço do produto.
- `estoque`: a quantidade disponível em estoque.

### Métodos

- `get_codigo()`: retorna o código do produto.
- `get_descricao()`: retorna a descrição do produto.
- `get_categoria()`: retorna a categoria do produto.
- `get_preco()`: retorna o preço do produto.
- `get_estoque()`: retorna a quantidade em estoque.
- `set_codigo(codigo)`: define o código do produto.
- `set_descricao(descricao)`: define a descrição do produto.
- `set_categoria(categoria)`: define a categoria do produto.
- `set_preco(preco)`: define o preço do produto.
- `set_estoque(estoque)`: define a quantidade em estoque.

## Funcionalidades

1. **Cadastrar Produto**: Permite adicionar um novo produto ao sistema.
2. **Listar Produtos**: Exibe todos os produtos cadastrados.
3. **Editar Produto**: Permite modificar os detalhes de um produto existente.
4. **Remover Produto**: Remove um produto do sistema.
