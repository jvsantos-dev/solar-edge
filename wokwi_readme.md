## Visão Geral do Projeto

Este projeto implementa uma solução IoT para monitoramento de temperatura, umidade e luminosidade, utilizando o ESP32 e a plataforma Wokwi. Ele coleta dados de sensores (DHT22 para temperatura e umidade, LDR para luminosidade), envia esses dados a um broker MQTT e permite o controle remoto de um LED via MQTT.
Funcionalidades:

    Coleta de dados de sensores de temperatura (DHT22), umidade (DHT22) e luminosidade (LDR).
    Publicação de dados em tópicos MQTT para temperatura, umidade e luminosidade.
    Controle remoto de um LED via comandos recebidos por MQTT.
    Simulação no Wokwi, permitindo testes de código com dispositivos como o ESP32 sem a necessidade de hardware físico.

# Bibliotecas Usadas

    WiFi.h: Para gerenciar a conexão Wi-Fi do ESP32.
    PubSubClient.h: Para gerenciar a comunicação MQTT.
    DHT.h: Para interagir com o sensor de temperatura e umidade DHT22.

# Definições de Hardware

    Sensor DHT22: Conectado ao pino 4 do ESP32 para medir temperatura e umidade.
    LDR (Light Dependent Resistor): Sensor de luminosidade conectado ao pino 34, utilizado para medir a intensidade da luz no ambiente.
    LED: Um LED embutido (pino LED_BUILTIN) é controlado via MQTT, permitindo que o usuário ligue ou desligue o LED remotamente.

# Configuração de Rede e MQTT

    Wi-Fi: O ESP32 conecta-se à rede Wi-Fi configurada com o SSID "Wokwi-GUEST" e sem senha (na simulação do Wokwi).
    Broker MQTT: O código utiliza o broker MQTT público no endereço 74.163.88.61, na porta 1883, para enviar dados e receber comandos.
    Tópicos MQTT:
        /monitor/cmd: Para ouvir comandos e controlar o LED.
        /monitor/temperature: Para publicar a temperatura medida.
        /monitor/humidity: Para publicar a umidade medida.
        /monitor/lux: Para publicar a luminosidade medida.

# Funções Principais

    initSerial(): Inicializa a comunicação serial com o monitor, permitindo que você veja os logs e leituras dos sensores.
    initWiFi(): Conecta o ESP32 à rede Wi-Fi utilizando as credenciais configuradas.
    initMQTT(): Configura a conexão MQTT com o broker e define a função de callback para lidar com mensagens recebidas.
    initOutput(): Configura o pino do LED (LED_BUILTIN) como saída e garante que ele esteja desligado inicialmente.

# Função setup():

    Inicializa a comunicação serial.
    Conecta ao Wi-Fi.
    Conecta ao broker MQTT.
    Inicializa o sensor DHT22 e o LED.
    Publica o estado inicial do sistema no MQTT.

# Função loop():

# Executada continuamente:

    Verifica Conexões: Verifica se o ESP32 está conectado ao Wi-Fi e ao MQTT.
    Mede Sensores: Coleta dados de luminosidade (via LDR), temperatura e umidade (via DHT22), publicando essas leituras no broker MQTT.
    Média das Leituras: Calcula a média de 10 leituras consecutivas para cada sensor.
    Publicação no MQTT: Envia as medições de luminosidade, temperatura e umidade ao broker MQTT.

# Funções de Classificação

    classificarLuminosidade(): Classifica o nível de luminosidade em categorias (Escuro, Nublado, Parcialmente Ensolarado, Ensolarado) com base no valor medido.
    classificarTemperatura(): Classifica a temperatura em categorias (Muito Frio, Frio, Moderado, Quente, Muito Quente).
    classificarSolar(): Classifica a radiação solar com base na temperatura e condições climáticas (simulação de "sol", "nuvem", ou "chuva").

# Funções de Conexão e Reconexão

    VerificaConexoesWiFIEMQTT(): Verifica se o ESP32 está conectado ao Wi-Fi e ao broker MQTT, tentando reconectar caso contrário.
    EnviaEstadoOutputMQTT(): Envia o estado atual do LED (ligado ou desligado) para o broker MQTT.
    handleLuminosity(): Lê o valor do sensor de luminosidade (LDR) e publica no broker MQTT.
    handleDHT(): Lê os valores de temperatura e umidade do sensor DHT22 e publica no broker MQTT.

# Funções de Reconexão

    reconectWiFi(): Reconecta ao Wi-Fi se a conexão for perdida.
    reconnectMQTT(): Reconecta ao broker MQTT se a conexão for perdida.

# Como Usar no Wokwi

O Wokwi é uma plataforma de simulação que permite testar o código do ESP32 e simular sensores como o DHT22 e o LDR. Ao usar o Wokwi, é possível simular a leitura dos sensores e a comunicação MQTT sem precisar de hardware físico.
Passos:

    Abra o projeto no Wokwi e conecte os sensores virtuais (DHT22 e LDR).
    Importe o código para o ambiente de simulação.
    Execute o código e visualize os dados de temperatura, umidade e luminosidade sendo publicados no broker MQTT.
    Utilize o MQTT Dashboard ou outra ferramenta de monitoramento para observar as mensagens publicadas.

## Considerações Finais

# Este projeto demonstra como integrar sensores simples com MQTT, criando um sistema de monitoramento em tempo real com ESP32. O código está configurado para testes na plataforma Wokwi, permitindo explorar a IoT de forma prática, sem a necessidade de hardware físico.
