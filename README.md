Plataforma de Previsão e Gerenciamento de Energia com Otimização para Armazenamento e Veículos Elétricos

A Plataforma de Previsão e Gerenciamento de Energia é uma solução unificada que integra dados meteorológicos em tempo real e históricos para otimizar o uso de energia renovável, sistemas de armazenamento (como baterias) e veículos elétricos. A plataforma prevê a geração de energia renovável (solar e eólica), sugere os melhores momentos para armazenar ou consumir energia e permite o controle automatizado do carregamento de veículos elétricos e baterias, maximizando a eficiência e reduzindo os custos.
Objetivo

O objetivo deste projeto é permitir que os usuários maximizem o uso de energia renovável, reduzam a dependência da rede elétrica, diminuam os custos e contribuam para a redução da pegada de carbono, ao mesmo tempo em que otimizam o uso de sistemas de armazenamento de energia e veículos elétricos.
Arquitetura do Sistema
Hardware

    Sensores Meteorológicos (Opcional): Para coleta de dados climáticos em tempo real.
    Sistema de Armazenamento de Energia: Baterias ou outros sistemas para armazenar a energia gerada.
    Veículos Elétricos: Integrados para otimizar o consumo e carregamento de energia.
    Dispositivos de Automação Doméstica/Empresarial (Opcional): Para ajuste automático no consumo de energia e carregamento de baterias.

Software

    Plataforma de Previsão e Gerenciamento: Sistema central que coleta e processa os dados meteorológicos e de energia, além de sugerir ações de armazenamento e consumo.
    Interface de Usuário: Painel interativo para visualização das previsões de energia, status dos sistemas e gráficos em tempo real.
    Integrações MQTT: Comunicação entre sistemas de geração de energia, armazenamento e veículos elétricos.

Fluxo de Dados

    Previsão de Geração de Energia: A plataforma coleta dados meteorológicos e históricos para prever a geração de energia renovável (solar e eólica) nas próximas horas/dias.
    Sugestões de Armazenamento e Consumo: A plataforma sugere os melhores horários para armazenar energia (em baterias ou veículos elétricos) ou consumi-la (quando a geração for baixa).
    Automatização de Carga e Descarga: Caso a plataforma seja integrada com sistemas de automação, ela ajusta automaticamente o carregamento das baterias e veículos elétricos, com base nas previsões de geração e consumo.
    Dashboard de Monitoramento: Painel interativo que exibe dados de temperatura, geração de energia, status de armazenamento e veículos, além de gráficos em tempo real.

Funcionalidades

    Previsão de Geração de Energia: Análise detalhada da produção de energia renovável com base nas condições climáticas.
    Otimização de Armazenamento e Consumo: Sugestões de quando armazenar ou consumir energia para reduzir custos.
    Gerenciamento Automático de Carga e Descarga: Controle automatizado de carga de baterias e veículos elétricos com base nas previsões de energia e demanda.
    Dashboard Interativo: Visualização em tempo real dos dados de energia, geração, consumo e status dos dispositivos conectados.
    Alertas de Consumo Ideal: Notificações sobre os melhores momentos para usar energia armazenada, evitando horários de pico.

Como Usar
1. Configuração da Plataforma
Configuração de Hardware

    Instale os sensores meteorológicos (se necessário) e dispositivos de armazenamento (baterias, veículos elétricos).
    Configure os dispositivos de automação (se desejado) para integração com a plataforma.

Configuração de Software

Instale as dependências necessárias para a plataforma de previsão:

pip install pandas numpy plotly dash paho-mqtt

Configuração da Conexão MQTT

Configure o acesso ao broker MQTT na plataforma.
Configuração de APIs Meteorológicas (Opcional)

Se você deseja usar dados meteorológicos em tempo real, insira as chaves de API apropriadas.
Inicie o Serviço

Execute o script principal da plataforma:

python plataforma_energia.py

Acesse o painel interativo no navegador, normalmente em http://localhost:8050.
2. Uso do Dashboard

    Visualização em Tempo Real: Visualize gráficos de geração de energia, status dos sistemas de armazenamento e veículos elétricos.
    Interações: O usuário pode interagir com o painel para visualizar as previsões de energia para os próximos dias e semanas. Também pode configurar a automação, como a programação de carregamento de veículos elétricos.

Exemplo de Saída

    Previsão de Geração de Energia:
        Geração Solar Estimada: 4.5 kWh (para o dia de hoje).

    Sugestão de Armazenamento:
        Armazenar energia de 14h às 16h (alta geração prevista).

    Dashboard:
        Gráfico de Temperatura e Umidade da região.
        Gráfico de Produção de Energia Solar/Eólica.
        Status em tempo real: "Armazenamento em Bateria: 70%".
        Notificação: "Recarregar veículo elétrico entre 22h e 23h para aproveitar a baixa tarifa."

Requisitos e Dependências
Requisitos de Software

    Python 3.x
    Bibliotecas Python:
        numpy
        pandas
        plotly
        dash
        paho-mqtt
    Broker MQTT (ex: Mosquitto ou similar) para comunicação entre a plataforma e dispositivos IoT.
    API de Previsão Climática (opcional): Ex: OpenWeather, WeatherAPI.

Arquitetura

A plataforma segue a arquitetura de Microserviços:

    Frontend: Desenvolvido com Dash e Plotly para visualização interativa.
    Backend: Processamento de dados de energia, previsão de geração e otimização de consumo.
    Comunicação: MQTT para troca de dados em tempo real entre dispositivos.

Autores

    João Victor Oliveira dos Santos - RM: 557948
