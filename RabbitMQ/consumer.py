import pika

def callback(ch, method, properties, body):
    print(f"[Consumidor] Recebido: {body.decode()}")

def consume_messages():
    # Conecte-se ao RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a fila (caso não tenha sido criada)
    channel.queue_declare(queue='product_queue')

    # Configurar o consumidor para ler mensagens da fila
    channel.basic_consume(queue='product_queue', on_message_callback=callback, auto_ack=True)
    
    print('[Consumidor] Aguardando mensagens. Pressione Ctrl+C para sair')
    channel.start_consuming()

consume_messages()
