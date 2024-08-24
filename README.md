# 🌍 WorldMap API - Consumo da REST Countries

Este projeto tem como objetivo o consumo da API [REST Countries](https://restcountries.com/) para buscar informações detalhadas sobre países. Ao fornecer o nome de um país, a aplicação retorna dados relevantes como:

- **🚩Nome do país**
- **❗Capital**
- **🏝️Sub-região**
- **🤼‍♂️População**
- **🚵‍♂️Região (Continente)**

## Objetivo do Projeto 📋

O projeto foi desenvolvido para o desafio da Fabrica de software, projeto de extensão na unipe. Tem o intuito de criar uma API simples que facilite a busca por informações de países de forma dinâmica e prática. A aplicação pode ser usada como base para projetos que envolvem geografia, sistemas de informação ou até mesmo para estudos de APIs e consumo de dados externos(A aplicação está incompleta e não funcional por problemas técnicos, como falta de conhecimento para o desenvolvimento, aprendi um dia antes como consumir uma API então é minha primeira experiência, dei meu melhor mas mesmo dessa forma reconheço que ficou incompleto).

## Funcionalidades

- Busca por países através do nome.
- Exibição das informações principais, como capital, população, sub-região e continente.
- Persistência dos dados no banco de dados caso o país não esteja previamente registrado.

## Tecnologias Utilizadas 💻

- **Django**: Framework principal para o desenvolvimento da aplicação.
- **Django Rest Framework**: Utilizado para a criação da API REST.
- **requests**: Biblioteca Python usada para fazer as requisições à API REST Countries(Por algum motivo não consegui utilizar o requests, houve erro e não consegui identificar).

## 🔧Como Configurar o Projeto🔨

- Certifique-se de ter instalado na máquina o Python e Visual Studio Code como IDE
- Baixe a venv com o código "python -m venv venv" (No terminal)
- Baixe o Django rest framework em sua máquina, no terminal digite o código "pip install djangorestframework" dessa forma você terá tudo que preciso para utilizar o projeto, dado que o app e o projeto já forma instalados
- E mais uma coisa é lembrar de ativar a venv pelo terminal, usando o comando ".\venv\Scripts\activate"

## Como Usar ✈️

- Inicie com os comandos "py manage.py migrate" para enviar os dados para o banco de dados e em seguida o "py manage.py makemigrations"
- Depois para rodar o projeto coloque "py manage.py runserver" e então vai se gerar um link que você pode acessar segurando a tecla CTRL(Control) e clicando com o mouse.



## Considerações Finais 🎬

- Tive meu primeiro contato com django, rest framework, e API, então não esperava que eu fosse conseguir executar com perfeição, mas até onde testei saiu "ok".
- Caso não consiga passar no desafio irei tentar no próximo semestre que vem com mais experiência e estudo encima de django.
- De toda forma curti a experiência de ter uma demanda, embora era de certa forma estressante e atacava direto minha ansiedade kkk mas deu tudo certo.
- Devo agradecer a ao meu amigo da fábrica João Pedro Feitoza, que me motivou a continuar mesmo eu querendo desistir em alguns momentos, aos meus amigos de classe que estavam sempre tentando em me motivando também, e principalmente a minha namorada por me apoiar e por aceitar eu ficar o sábado inteiro fazendo o desafio mesmo tendo marcado de me encontrar com ela kkkkkkk

