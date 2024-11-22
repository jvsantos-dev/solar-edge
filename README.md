# Plataforma de Previsão e Gerenciamento de Energia com Otimização para Armazenamento e Veículos Elétricos

## Descrição Geral

Este projeto desenvolve uma plataforma unificada que integra dados meteorológicos em tempo real e históricos para otimizar o uso de energia renovável, sistemas de armazenamento de energia (baterias) e veículos elétricos. A plataforma prevê a geração de energia renovável (solar e eólica), sugere os melhores momentos para armazenar ou consumir energia e permite o controle automatizado de carregamento de veículos elétricos e baterias, maximizando a eficiência e reduzindo os custos de energia.

## Objetivo

O objetivo é permitir que os usuários maximizem o uso de energia renovável, reduzindo a dependência da rede elétrica, diminuindo os custos de energia e contribuindo para uma menor pegada de carbono, enquanto otimizam o uso de sistemas de armazenamento e veículos elétricos.

## Arquitetura do Sistema

### Hardware

- **Sensores Meteorológicos (opcional):** Para coleta de dados climáticos em tempo real.
- **Sistema de Armazenamento de Energia (ex: Baterias):** Para armazenar a energia gerada.
- **Veículos Elétricos:** Integrados à plataforma para otimizar o consumo e carregamento de energia.
- **Dispositivos de Automação Doméstica/Empresarial (opcional):** Para ajustar automaticamente o consumo de energia e carregamento de baterias.

### Software

- **Plataforma de Previsão e Gerenciamento:** Sistema central que coleta e processa os dados meteorológicos e de energia, além de sugerir ações de armazenamento e consumo.
- **Interface de Usuário:** Painel interativo para visualização das previsões de energia, status dos sistemas e gráficos em tempo real.
- **Integrações MQTT:** Para comunicação entre os sistemas de geração de energia, armazenamento e veículos elétricos.

## Fluxo de Dados

### Previsão de Geração de Energia

A plataforma coleta dados meteorológicos e históricos para prever a quantidade de energia renovável que será gerada nas próximas horas/dias (solar, eólica).

### Sugestões de Armazenamento e Consumo

Com base nas previsões, a plataforma sugere os melhores horários para armazenar energia (em baterias ou veículos elétricos) ou consumi-la (quando a geração for baixa).

### Automatização de Carga e Descarga

Caso integrada com sistemas de automação, a plataforma ajusta automaticamente o carregamento das baterias e dos veículos elétricos, com base nas previsões de geração e consumo.

### Dashboard de Monitoramento

O painel interativo exibe dados de temperatura, geração de energia, status de armazenamento e veículos, além de gráficos em tempo real.

## Funcionalidades

- **Previsão de Geração de Energia:** Análise detalhada da produção de energia renovável, levando em conta as condições climáticas.
- **Otimização de Armazenamento e Consumo:** Sugestões de quando armazenar ou consumir energia para minimizar os custos.
- **Gerenciamento Automático de Carga e Descarga:** Controle automático da carga de baterias e veículos elétricos, com base nas previsões de energia e demanda.
- **Dashboard Interativo:** Visualização em tempo real dos dados de energia, geração, consumo e status dos dispositivos conectados.
- **Alertas de Consumo Ideal:** Notificações sobre os melhores momentos para usar energia armazenada, evitando horários de pico.

## Como Usar

### 1. Configuração da Plataforma

#### Configuração de Hardware

- Instale os sensores meteorológicos (se necessário) e dispositivos de armazenamento (baterias, veículos elétricos).
- Configure os dispositivos de automação (se desejado) para integração com a plataforma.

#### Configuração de Software

## Instalação e Configuração

### 1. Instalação das Dependências

Para garantir o funcionamento adequado da plataforma, é necessário instalar as bibliotecas essenciais. Execute o seguinte comando para instalar as dependências:


pip install pandas numpy plotly dash paho-mqtt

Essas bibliotecas permitem a criação do dashboard interativo e a comunicação eficiente via MQTT.
2. Configuração da Conexão MQTT

A comunicação entre os dispositivos da plataforma (sensores, baterias, veículos elétricos, entre outros) e o sistema de gerenciamento central é realizada via MQTT. Para isso, você precisará configurar um broker MQTT.
Passos para Configuração:

    Escolha um Broker MQTT: Você pode optar por brokers MQTT como o Mosquitto, que pode ser instalado no seu servidor, ou usar serviços MQTT na nuvem, como o HiveMQ.
    Configuração de Conexão: Após configurar o broker, adicione as informações de acesso (host, porta, usuário e senha) no arquivo de configuração da plataforma.

Exemplo de Configuração:

mqtt_host = "mqtt.exemplo.com"        # Host do seu broker MQTT
mqtt_port = 1883                       # Porta padrão do MQTT
mqtt_user = "usuario_mqtt"             # Usuário para autenticação (se necessário)
mqtt_password = "senha_mqtt"           # Senha para autenticação (se necessário)
mqtt_topic = "energia/plataforma"      # Tópico principal de comunicação

3. Uso do Dashboard

O Dashboard permite a visualização em tempo real dos dados de energia, status dos sistemas de armazenamento (baterias e veículos elétricos) e alertas para otimização do consumo de energia.
Visualização em Tempo Real:

O dashboard exibe gráficos interativos que mostram a geração de energia renovável (solar e eólica), o status das baterias, veículos elétricos e alertas para o melhor uso de energia, como os horários ideais para carregar as baterias ou veículos elétricos.
Interações:

Além de visualizar as previsões de geração de energia para os próximos dias e semanas, o painel permite ao usuário ajustar configurações de automação, como o agendamento de carregamento dos veículos elétricos.
Exemplo de Saída:

    Previsão de Geração de Energia: Geração Solar Estimada: 4.5 kWh (para o dia de hoje).
    Sugestão de Armazenamento: Armazenar energia de 14h às 16h (alta geração prevista).
    Status e Alertas:
        Gráfico de Temperatura e Umidade da região.
        Gráfico de Produção de Energia Solar/Eólica.
        Status: "Armazenamento em Bateria: 70%".
        Notificação: "Recarregar veículo elétrico entre 22h e 23h para aproveitar baixa tarifa."

Requisitos e Dependências

Antes de rodar o projeto, certifique-se de que você possui os seguintes requisitos:

    Python 3.x: Certifique-se de que a versão do Python seja compatível com as bibliotecas necessárias.
    Bibliotecas Python:
        numpy
        pandas
        plotly
        dash
        paho-mqtt
    Broker MQTT: Você pode usar o Mosquitto ou qualquer outro broker MQTT de sua preferência para a comunicação entre a plataforma e os dispositivos IoT.
    API de Previsão Climática (opcional): Para integração de dados climáticos em tempo real, você pode usar APIs como OpenWeather ou WeatherAPI.

Projeto: Monitoramento IoT com ESP32 e MQTT

Este projeto utiliza um ESP32 integrado com o sensor DHT22 para monitorar a temperatura e a umidade em tempo real. Os dados coletados são enviados via MQTT para um broker. Além disso, LEDs simulam o controle de dispositivos (ventilador e aquecedor) com base nas leituras dos sensores.
Arquitetura
Hardware:

    ESP32: Microcontrolador responsável pela comunicação Wi-Fi e MQTT.
    DHT22: Sensor para medir temperatura e umidade do ambiente.
    LEDs: Simulam dispositivos como ventilador e aquecedor.

Software:

    Conexão Wi-Fi: O ESP32 transmite dados para a plataforma via Wi-Fi.
    MQTT: O ESP32 se comunica com o broker MQTT para enviar dados de temperatura e umidade.
    Monitoramento de Dados: O ESP32 publica dados nos tópicos MQTT para permitir o acompanhamento em tempo real.

Funcionalidades
Monitoramento de Temperatura e Umidade

O ESP32 publica os dados de temperatura e umidade nos seguintes tópicos MQTT:

    /monitor/temperature: Temperatura atual.
    /monitor/humidity: Umidade atual.
    /monitor/status: Status do sistema (ex.: "Ventilador Ligado").

Automação com LEDs

    Ventilador (LED): Ativado se a temperatura for maior que 25°C ou a umidade ultrapassar 60%.
    Aquecedor (LED): Ativado se a temperatura for inferior a 22°C.
    Desligado: O sistema entra em repouso caso não haja necessidade de ativação de nenhum dispositivo.

Como Usar
1. Configuração do Código

Edite o código do ESP32 conforme abaixo:

const char* ssid = "Wokwi-GUEST";          // Substitua pelo nome da sua rede Wi-Fi.
const char* password = "";                 // Substitua pela senha da sua rede Wi-Fi.
const char* mqtt_server = "BROKER_IP";     // Substitua pelo IP do seu broker MQTT.
const int mqtt_port = 1883;                // Porta padrão do MQTT.

2. Componentes e Conexões

    Conecte o DHT22 ao pino 14 do ESP32.
    Conecte os LEDs aos pinos 13 (Ventilador) e 15 (Aquecedor).

3. Configuração do Broker MQTT

Configure um broker MQTT local (ex.: Mosquitto) ou utilize um broker público. Certifique-se de que o broker esteja acessível no endereço especificado no código.
4. Carregamento do Código

Utilize a Arduino IDE para compilar e carregar o código no ESP32. Instale as bibliotecas necessárias, como:

    PubSubClient
    Adafruit SSD1306
    DHT

5. Testando o Sistema

Após carregar o código no ESP32, ele tentará se conectar à rede Wi-Fi. O display exibirá a temperatura, umidade e status da conexão. Verifique os tópicos MQTT para visualizar os dados enviados.
Arquitetura do Sistema

Exemplos de Tópicos MQTT:

    /monitor/temperature: 24.50
    /monitor/humidity: 55.00
    /monitor/status: "Ventilador Ligado"

## Autores

# João Victor Oliveira dos Santos - RM: 557948
