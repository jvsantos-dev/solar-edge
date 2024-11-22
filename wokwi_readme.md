Visão Geral do Projeto

O código implementa uma solução IoT que:

    Coleta dados de sensores (DHT22 para temperatura e umidade, LDR para luminosidade).
    Conecta-se a uma rede Wi-Fi para enviar esses dados a um broker MQTT.
    Publica informações em tópicos MQTT, como temperatura, umidade e luminosidade.
    Permite controlar um LED remotamente via MQTT, baseado em comandos recebidos.
    Usa o Wokwi como ambiente de simulação, permitindo testar o código com dispositivos como o ESP32 em uma plataforma online.

Bibliotecas Usadas

    WiFi.h: Para gerenciar a conexão Wi-Fi do ESP32.
    PubSubClient.h: Para gerenciar a comunicação MQTT.
    DHT.h: Para interagir com o sensor de temperatura e umidade DHT22.

Definições de Hardware

    DHT Sensor: O sensor DHT22 está conectado ao pino 4 do ESP32 para medir temperatura e umidade.
    LDR (Light Dependent Resistor): Sensor de luminosidade conectado ao pino 34, utilizado para medir a intensidade da luz no ambiente.
    LED: Um LED embutido (pino LED_BUILTIN) é controlado via MQTT, permitindo que o usuário ligue ou desligue o LED remotamente.

Configuração de Rede e MQTT

    Wi-Fi: O ESP32 conecta-se à rede Wi-Fi configurada com o SSID "Wokwi-GUEST" e sem senha (na simulação do Wokwi).
    Broker MQTT: O código usa o broker MQTT público em 74.163.88.61 na porta 1883. O ESP32 se conecta a esse broker para publicar dados e receber comandos.
    Tópicos MQTT:
        /monitor/cmd: Para ouvir comandos e controlar o LED.
        /monitor/temperature: Para publicar a temperatura medida.
        /monitor/humidity: Para publicar a umidade medida.
        /monitor/lux: Para publicar a luminosidade medida.

Funções Principais
initSerial()

Inicializa a comunicação serial com o monitor serial, permitindo que você veja os logs e as leituras dos sensores.
initWiFi()

Conecta o ESP32 à rede Wi-Fi usando as credenciais configuradas.
initMQTT()

Configura a conexão MQTT com o broker e define a função de callback para lidar com as mensagens recebidas.
initOutput()

Configura o pino do LED (usando LED_BUILTIN) como saída e garante que ele esteja desligado inicialmente.
setup()

Configura o ambiente:

    Inicializa a comunicação serial.
    Conecta ao Wi-Fi.
    Conecta ao broker MQTT.
    Inicializa o sensor DHT22 e o LED.
    Publica o estado inicial do sistema no MQTT.

loop()

O loop principal, que é executado continuamente:

    Verifica Conexões: Verifica se o ESP32 está conectado ao Wi-Fi e ao MQTT.
    Mede Sensores: Coleta dados de luminosidade (via LDR), temperatura e umidade (via DHT22), e publica essas leituras no broker MQTT.
    Média das Leituras: Calcula a média de 10 leituras consecutivas para cada sensor.
    Publicação no MQTT: Envia as medições de luminosidade, temperatura e umidade ao broker MQTT.

Funções de Classificação

    classificarLuminosidade(): Classifica o nível de luminosidade em categorias (Escuro, Nublado, Parcialmente Ensolarado, Ensolarado) com base no valor medido.
    classificarTemperatura(): Classifica a temperatura em categorias (Muito Frio, Frio, Moderado, Quente, Muito Quente).
    classificarSolar(): Classifica a radiação solar com base na temperatura e condições climáticas (Simulação de "sol", "nuvem", ou "chuva").

VerificaConexoesWiFIEMQTT()

Verifica se o ESP32 está conectado ao Wi-Fi e ao broker MQTT, e tenta reconectar caso contrário.
EnviaEstadoOutputMQTT()

Envia o estado atual do LED (ligado ou desligado) para o broker MQTT.
handleLuminosity()

Lê o valor do sensor de luminosidade (LDR) e publica no broker MQTT.
handleDHT()

Lê os valores de temperatura e umidade do sensor DHT22 e publica no broker MQTT.
mqtt_callback()

Função que é chamada sempre que uma mensagem é recebida no broker MQTT. O comando recebido pode ser "on" ou "off", que liga ou desliga o LED.
Funções de Reconexão

    reconectWiFi(): Reconecta ao Wi-Fi se a conexão for perdida.
    reconnectMQTT(): Reconecta ao broker MQTT se a conexão for perdida.

Como Usar no Wokwi

    Wokwi: A plataforma Wokwi permite testar o código do ESP32 e simular sensores como o DHT22 e o LDR. Ao utilizar o Wokwi, você pode simular a leitura dos sensores e a comunicação MQTT sem precisar de hardware físico.
    Passos:
        Abra o projeto no Wokwi, conecte os sensores virtuais (DHT22 e LDR).
        Importe o código para o ambiente de simulação.
        Execute o código e visualize os dados de temperatura, umidade e luminosidade sendo publicados no broker MQTT.
        Utilize o MQTT Dashboard ou outra ferramenta de monitoramento para observar as mensagens publicadas.

Considerações Finais

Este projeto é uma demonstração de como integrar sensores simples com MQTT e pode ser utilizado para criar sistemas de monitoramento em tempo real com ESP32. O código é configurado para testes no Wokwi, permitindo que você explore a IoT de maneira prática sem a necessidade de hardware físico.
