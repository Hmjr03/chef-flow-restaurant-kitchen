# 🍳 ChefFlow Restaurant Kitchen

![Django](https://img.shields.io/badge/Django-5.x-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## 📌 Sobre o projeto

**ChefFlow Restaurant Kitchen** é uma aplicação web desenvolvida com Django para gerenciamento de uma cozinha profissional.

O objetivo do projeto é centralizar informações importantes de um restaurante, permitindo o controle de:

- pratos;
- ingredientes;
- categorias de pratos;
- cozinheiros;
- relacionamentos entre equipe e cardápio.

O sistema foi desenvolvido como projeto de portfólio Django, aplicando boas práticas de desenvolvimento web, arquitetura MVC do Django, autenticação de usuários e operações CRUD completas.

---

# 🎯 Problema resolvido

Restaurantes precisam organizar diversas informações diariamente:

- quais pratos estão disponíveis;
- quais ingredientes fazem parte de cada receita;
- quais cozinheiros são responsáveis pelos pratos;
- como organizar o cardápio.

O ChefFlow oferece uma solução simples e organizada para facilitar essa gestão.

---

# 🚀 Funcionalidades

## Dashboard

- Visão geral da cozinha;
- Quantidade de pratos cadastrados;
- Quantidade de ingredientes;
- Quantidade de cozinheiros;
- Quantidade de categorias.

---

## Gestão de pratos

Permite:

✅ cadastrar pratos  
✅ visualizar detalhes  
✅ editar pratos  
✅ excluir pratos  

Cada prato possui:

- nome;
- descrição;
- preço;
- categoria;
- ingredientes;
- cozinheiros responsáveis.

---

## Gestão de ingredientes

Permite:

✅ cadastrar ingredientes  
✅ editar ingredientes  
✅ excluir ingredientes  

---

## Gestão de categorias

Permite:

✅ criar categorias de pratos  
✅ editar categorias  
✅ excluir categorias  

Exemplos:

- Entradas
- Pratos principais
- Sobremesas
- Bebidas

---

## Gestão de cozinheiros

Sistema de usuários personalizado baseado no Django User Model.

Cada cozinheiro possui:

- username;
- nome;
- email;
- anos de experiência.

---

# 🔐 Autenticação

O projeto utiliza o sistema nativo de autenticação do Django.

Recursos:

- login;
- logout;
- proteção de páginas privadas;
- controle de acesso através de usuários autenticados.

---

# 🛠 Tecnologias utilizadas

## Backend

- Python
- Django

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- Django Templates

## Banco de dados

- SQLite

## Ferramentas

- Git
- GitHub
- PyCharm
- Virtual Environment

---

# 🏗 Estrutura do projeto

```
chef-flow-restaurant-kitchen/

├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── kitchen/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   └── kitchen/
│
├── static/
│   └── css/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🗄 Modelagem do sistema

## DishType

Representa categorias de pratos.

Exemplo:

```
Pizza
Sobremesa
Entrada
```

---

## Ingredient

Representa ingredientes utilizados nas receitas.

Exemplo:

```
Tomate
Queijo
Manjericão
```

---

## Cook

Usuário personalizado responsável pela cozinha.

Possui:

```
Nome
Email
Experiência
```

---

## Dish

Representa um prato do restaurante.

Relacionamentos:

```
Dish
 |
 |---- DishType
 |
 |---- Ingredients
 |
 |---- Cooks
```

---

# ⚙️ Como executar o projeto localmente

## 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/chef-flow-restaurant-kitchen.git
```

---

## 2. Entrar no projeto

```bash
cd chef-flow-restaurant-kitchen
```

---

## 3. Criar ambiente virtual

Mac/Linux:

```bash
python3 -m venv venv
```

Ativar:

```bash
source venv/bin/activate
```

---

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 5. Executar migrações

```bash
python manage.py migrate
```

---

## 6. Criar superusuário

```bash
python manage.py createsuperuser
```

---

## 7. Executar servidor

```bash
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000/
```

---

# 🧪 Testes

Executar testes Django:

```bash
python manage.py test
```

Verificar configuração:

```bash
python manage.py check
```

---

# 🔮 Melhorias futuras

Possíveis evoluções:

- sistema de pedidos;
- controle de estoque;
- dashboard com gráficos;
- calendário de produção;
- notificações;
- API REST;
- integração com pagamentos.

---

# 👨‍💻 Desenvolvimento

Projeto desenvolvido utilizando:

- Django Framework;
- boas práticas de organização;
- relacionamento entre modelos;
- autenticação;
- CRUD completo;
- interface responsiva.

---

# 📄 Licença

Este projeto está disponível para fins educacionais e de portfólio.
