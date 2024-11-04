# Sistema de Comunicação por Mensagens com RabbitMQ

Este projeto é uma implementação de um sistema de comunicação baseado em filas de mensagens usando RabbitMQ, onde produtores enviam mensagens para uma fila e consumidores lêem essas mensagens.

## Objetivo

O objetivo deste projeto é implementar um sistema básico de mensageria, permitindo que diferentes serviços se comuniquem de forma assíncrona. Em um sistema distribuído, isso facilita a troca de informações entre componentes desacoplados.

## Tecnologias Utilizadas

- **RabbitMQ**: Servidor de mensagens para gerenciar as filas e troca de mensagens.
- **Python**: Linguagem de programação utilizada para a implementação dos produtores e consumidores.

## Estrutura do Projeto

O projeto possui duas partes principais:

- **Produtor**: Serviço que envia mensagens para a fila no RabbitMQ.
- **Consumidor**: Serviço que lê e processa mensagens da fila no RabbitMQ.

## Requisitos

- **Python 3.x**
- **RabbitMQ**: Instale o RabbitMQ localmente ou utilize uma instância em um servidor. Para instalar o RabbitMQ no sistema local, siga [este guia](https://www.rabbitmq.com/download.html).

## Configuração do Ambiente

1. **Instalar o Pika**: Pika é a biblioteca de cliente para comunicação com o RabbitMQ em Python.

   ```bash
   pip install pika
