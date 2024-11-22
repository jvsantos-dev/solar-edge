## Dashboard IoT - Wokwi

# Este é um aplicativo de monitoramento em tempo real de dados de temperatura, umidade e luminosidade utilizando a plataforma Dash e MQTT.
# Funcionalidades

    Gráficos em tempo real para monitoramento da temperatura, umidade e luminosidade.
    Atualização dinâmica dos gráficos a cada 2 segundos.
    Exibição do status atual, aguardando dados de sensores conectados via MQTT.

# Tecnologias Utilizadas

    Dash: Framework para criação de interfaces interativas em Python.
    Plotly: Biblioteca para visualização gráfica.
    Paho MQTT: Cliente MQTT para comunicação em tempo real.
    MQTT Broker: Comunicação entre dispositivos e o servidor.

# Instalação e Execução

    Clone o repositório:

git clone https://github.com/fabiocabrini/fiware
cd repository

# Instale as dependências:

pip install -r requirements.txt

# Execute o servidor:

    python app.py

    O dashboard estará disponível em http://127.0.0.1:8050/ (ou http://<seu-ip>:8050/ para acesso remoto).

# Configuração do MQTT

    O aplicativo se conecta a um broker MQTT no endereço 74.163.88.61 na porta 1883. Certifique-se de que seu broker MQTT esteja ativo e enviando dados nos tópicos:
        /monitor/temperature
        /monitor/humidity
        /monitor/lux
        /monitor/status

# Licença

Este projeto está licenciado sob a MIT License.
