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

Instalação das Dependências

Para instalar as dependências necessárias, execute o seguinte comando:

pip install pandas numpy plotly dash paho-mqtt

Configuração da Conexão MQTT

Para configurar a comunicação entre os dispositivos da plataforma (como sensores de energia, baterias e veículos elétricos) e a plataforma de gerenciamento, é necessário configurar o broker MQTT. A plataforma utiliza MQTT para garantir a troca de dados em tempo real.
Passos para Configuração:

    Escolha um Broker MQTT:
    Você pode usar brokers como Mosquitto ou qualquer outro broker MQTT de sua escolha.
    Caso utilize o Mosquitto, instale-o no seu servidor ou utilize um serviço MQTT em nuvem.

    Configuração de Conexão:
    Após configurar o broker, adicione as informações de acesso (host, porta, usuário e senha) ao arquivo de configuração da plataforma.

    Exemplo de Configuração MQTT:

mqtt_host = "mqtt.exemplo.com"
mqtt_port = 1883
mqtt_user = "usuario_mqtt"
mqtt_password = "senha_mqtt"
mqtt_topic = "energia/plataforma"

Uso do Dashboard
Visualização em Tempo Real:

    O dashboard exibe gráficos de geração de energia renovável, status dos sistemas de armazenamento (baterias e veículos elétricos) e alertas sobre os melhores momentos para armazenar ou consumir energia.

Interações:

    O usuário pode interagir com o painel para visualizar as previsões de energia para os próximos dias e semanas. Além disso, o painel permite ajustar configurações de automação, como a programação de carregamento dos veículos elétricos.

Exemplo de Saída:

    Previsão de Geração de Energia: Geração Solar Estimada: 4.5 kWh (para o dia de hoje).
    Sugestão de Armazenamento: Armazenar energia de 14h às 16h (alta geração prevista).

Dashboard:

    Gráfico de Temperatura e Umidade da região.
    Gráfico de Produção de Energia Solar/Eólica.
    Status em tempo real: "Armazenamento em Bateria: 70%".
    Notificação: "Recarregar veículo elétrico entre 22h e 23h para aproveitar baixa tarifa."

Requisitos e Dependências
Python 3.x

    Certifique-se de ter uma versão do Python compatível.

Bibliotecas Python

    numpy
    pandas
    plotly
    dash
    paho-mqtt

Broker MQTT (ex: Mosquitto ou similar)

    Necessário para a comunicação entre a plataforma e os dispositivos IoT.

API de Previsão Climática (opcional)

    Ex: OpenWeather, WeatherAPI.

Arquitetura (para a turma de fevereiro)

A plataforma segue a arquitetura de Microserviços:

    Frontend (Dashboard): Interface interativa desenvolvida com Dash, Plotly e gráficos em tempo real.
    Backend: Processamento dos dados de energia, previsão de geração e otimização de consumo, utilizando Python.
    Comunicação entre Dispositivos: MQTT para garantir a troca de dados em tempo real entre dispositivos de geração, armazenamento e veículos elétricos.

A comunicação entre componentes segue o modelo client-server, onde o ESP32 (ou dispositivo similar) atua como cliente e a plataforma de gerenciamento funciona como servidor.
Autores

João Victor Oliveira dos Santos RM: 557948
