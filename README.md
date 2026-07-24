# 🍔 RedBurger

Sistema desenvolvido em **Django** para gerenciamento de cardápios digitais de lanchonetes, hamburguerias e restaurantes. Cada estabelecimento possui seu próprio cardápio, podendo gerenciar produtos, categorias e receber pedidos diretamente pelo WhatsApp.

---

# ✨ Funcionalidades

## 🔐 Autenticação e Administração

- Sistema de autenticação nativo do Django.
- Login e logout de usuários.
- Painel administrativo utilizando o Django Admin.
- Gerenciamento de usuários e permissões.
- Controle de acesso por usuário.
- Cada cardápio é vinculado a um único usuário.
- Usuários comuns possuem acesso apenas ao próprio cardápio.
- Superusuários possuem acesso total ao sistema.

---

## 🍔 Gerenciamento do Cardápio

O usuário pode editar as informações do seu estabelecimento:

- Nome da lanchonete.
- Logo.
- Banner.
- Descrição.
- Localização.
- Horário de funcionamento.

---

## 📂 Categorias

- Categorias padrão cadastradas.
- Criação de novas categorias.
- Edição de categorias.
- Exclusão de categorias.
- Organização dos produtos por categoria.

---

## 🍟 Produtos

- Cadastro de produtos.
- Upload de imagens.
- Descrição dos produtos.
- Preço.
- Associação às categorias.
- Ativação e desativação de produtos.

---

## 🛒 Carrinho de Compras

- Desenvolvido totalmente em JavaScript.
- Integração dinâmica das informações dos produtos.
- Adição e remoção de itens sem recarregar a página.
- Atualização automática das quantidades.
- Cálculo automático do valor total.
- Montagem dinâmica do resumo do pedido.

---

## 💬 Pedido via WhatsApp

- Geração automática da mensagem do pedido.
- Inclusão dos produtos selecionados.
- Quantidade de cada produto.
- Observações do cliente.
- Valor total da compra.
- Envio direto para o WhatsApp do estabelecimento.

---

## 📱 Interface

- Layout responsivo.
- Compatível com celulares, tablets e computadores.
- Interface simples e intuitiva.

---

# 🔒 Controle de Acesso

## Administrador

Pode:

- Criar usuários.
- Criar cardápios.
- Vincular cardápios aos usuários.
- Gerenciar todos os usuários.
- Gerenciar todos os cardápios.
- Gerenciar categorias e produtos de qualquer estabelecimento.

## Usuário

Pode:

- Fazer login.
- Editar as informações do próprio estabelecimento.
- Gerenciar apenas o próprio cardápio.
- Criar, editar e excluir categorias.
- Criar, editar e excluir produtos.

---

# ⚙️ Tecnologias Utilizadas

- Python
- Django
- Django Admin
- HTML5
- CSS3
- Bootstrap
- JavaScript
- SQLite

---

# ▶️ Como executar o projeto

Clone o repositório:

```bash
git clone <url-do-repositorio>
cd RedBurger
```

Crie o ambiente virtual:

```powershell
python -m venv venv
```

Ative o ambiente virtual:

```powershell
venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

Execute as migrações:

```powershell
python manage.py migrate
```

Crie um superusuário:

```powershell
python manage.py createsuperuser
```

Inicie o servidor:

```powershell
python manage.py runserver
```

---

# 🌐 Acessos

**Sistema**

```
http://127.0.0.1:8000/
```

**Painel Administrativo**

```
http://127.0.0.1:8000/admin/
```

---

# 📂 Estrutura do Projeto

```
RedBurger/
│
├── cardapio/
├── usuarios/
├── templates/
├── static/
├── media/
├── manage.py
└── requirements.txt
```

---

# 📌 Fluxo do Sistema

1. O administrador cria um usuário.
2. O administrador cria um cardápio e o vincula ao usuário.
3. O usuário realiza login no sistema.
4. O usuário edita as informações do estabelecimento (nome, logo, banner, descrição, localização e horário de funcionamento).
5. O usuário gerencia as categorias do cardápio, podendo utilizar as categorias existentes, criar novas, editar ou remover as que desejar.
6. O usuário cadastra os produtos, definindo categoria, descrição, preço e imagem.
7. Os clientes acessam o cardápio online.
8. O cliente adiciona os produtos ao carrinho.
9. O carrinho é atualizado dinamicamente em JavaScript, calculando automaticamente as quantidades e o valor total.
10. O sistema monta automaticamente a mensagem do pedido.
11. O cliente é redirecionado para o WhatsApp do estabelecimento com o pedido preenchido.

---

# 🚀 Diferenciais

- Sistema multiusuário.
- Autenticação nativa do Django.
- Painel administrativo integrado.
- Controle de acesso por usuário.
- Isolamento dos dados de cada estabelecimento.
- Gerenciamento completo de cardápios.
- Carrinho de compras desenvolvido em JavaScript.
- Atualização dinâmica sem recarregar a página.
- Integração com WhatsApp para envio dos pedidos.
- Interface responsiva.

---

# 📄 Licença

Este projeto foi desenvolvido para fins de estudo e aprendizado utilizando o framework Django.
