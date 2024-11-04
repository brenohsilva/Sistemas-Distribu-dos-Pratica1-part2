import pika

def send_message(message):
    # Conecte-se ao RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a fila (ela será criada se ainda não existir)
    channel.queue_declare(queue='product_queue')

    # Enviar a mensagem para a fila
    channel.basic_publish(exchange='', routing_key='product_queue', body=message)
    print(f"[Produtor] Enviado: {message}")

    # Feche a conexão
    connection.close()

# Enviar uma mensagem de exemplo
send_message("Produto A disponível em estoque")
