import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import paho.mqtt.client as mqtt
from collections import deque
import json

# Variáveis globais para armazenar os dados
temperatures = deque(maxlen=50)
humidities = deque(maxlen=50)
luminosities = deque(maxlen=50)
timestamps = deque(maxlen=50)

# Configuração do Broker MQTT
BROKER = "74.163.88.61"  # Endereço do broker MQTT
PORT = 1883               # Porta padrão MQTT
TOPIC_TEMP = "/monitor/temperature"
TOPIC_HUM = "/monitor/humidity"
TOPIC_LUX = "/monitor/lux"
TOPIC_STATUS = "/monitor/status"

# Callback quando uma mensagem é recebida
def on_message(client, userdata, msg):
    global temperatures, humidities, luminosities, timestamps
    topic = msg.topic
    payload = msg.payload.decode()
    current_time = len(timestamps)  # Exemplo simples de timestamp

    if topic == TOPIC_TEMP:
        temperatures.append(float(payload))
        timestamps.append(current_time)
    elif topic == TOPIC_HUM:
        humidities.append(float(payload))
    elif topic == TOPIC_LUX:
        luminosities.append(float(payload))
    elif topic == TOPIC_STATUS:
        # Status pode ser uma string, então não é necessário adicionar ao gráfico
        pass

# Inicializando cliente MQTT
mqtt_client = mqtt.Client(protocol=mqtt.MQTTv311)
mqtt_client.on_message = on_message
mqtt_client.connect(BROKER, PORT, 60)
mqtt_client.subscribe([(TOPIC_TEMP, 0), (TOPIC_HUM, 0), (TOPIC_LUX, 0), (TOPIC_STATUS, 0)])
mqtt_client.loop_start()

# Inicializando o app Dash
app = dash.Dash(__name__)
app.title = "Dashboard IoT - Wokwi"

app.layout = html.Div([
    html.H1("Monitoramento IoT - Wokwi", style={'text-align': 'center', 'color': '#4F8A8B', 'margin-top': '20px'}),
    
    # Gráfico de Temperatura
    dcc.Graph(id='temp-graph', style={'height': '50vh'}),
    
    # Gráfico de Umidade
    dcc.Graph(id='hum-graph', style={'height': '50vh'}),
    
    # Gráfico de Luminosidade
    dcc.Graph(id='lux-graph', style={'height': '50vh'}),
    
    # Status Atual
    html.Div(id='status-display', style={'text-align': 'center', 'font-size': '20px', 'margin-top': '20px', 'color': '#4F8A8B'}),
    
    # Intervalo de atualização
    dcc.Interval(
        id='update-interval',
        interval=2000,  # Atualizar a cada 2 segundos
        n_intervals=0
    )
])

# Estilo dos gráficos
def get_graph_style():
    return {
        'plot_bgcolor': '#f7f7f7',  # Fundo claro
        'paper_bgcolor': '#f7f7f7',  # Fundo do gráfico
        'font': {
            'family': 'Arial, sans-serif',  # Fonte
            'size': 12,  # Tamanho da fonte
            'color': '#4F8A8B',  # Cor do texto
        },
        'xaxis': {
            'title': 'Tempo',
            'titlefont': {'size': 14, 'color': '#4F8A8B'},
            'showgrid': True,
            'gridcolor': '#e1e1e1',
        },
        'yaxis': {
            'title': 'Valor',
            'titlefont': {'size': 14, 'color': '#4F8A8B'},
            'showgrid': True,
            'gridcolor': '#e1e1e1',
        }
    }

# Callback para atualizar o gráfico de temperatura
@app.callback(
    Output('temp-graph', 'figure'),
    Input('update-interval', 'n_intervals')
)
def update_temp_graph(n):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(timestamps), 
        y=list(temperatures), 
        mode='lines+markers', 
        name='Temperatura',
        line=dict(color='royalblue', width=3),
        marker=dict(size=6, color='lightblue', symbol='circle')
    ))
    fig.update_layout(title="Temperatura ao longo do tempo", **get_graph_style())
    return fig

# Callback para atualizar o gráfico de umidade
@app.callback(
    Output('hum-graph', 'figure'),
    Input('update-interval', 'n_intervals')
)
def update_hum_graph(n):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(timestamps), 
        y=list(humidities), 
        mode='lines+markers', 
        name='Umidade',
        line=dict(color='seagreen', width=3),
        marker=dict(size=6, color='lightgreen', symbol='circle')
    ))
    fig.update_layout(title="Umidade ao longo do tempo", **get_graph_style())
    return fig

# Callback para atualizar o gráfico de luminosidade
@app.callback(
    Output('lux-graph', 'figure'),
    Input('update-interval', 'n_intervals')
)
def update_lux_graph(n):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(timestamps), 
        y=list(luminosities), 
        mode='lines+markers', 
        name='Luminosidade',
        line=dict(color='orange', width=3),
        marker=dict(size=6, color='gold', symbol='circle')
    ))
    fig.update_layout(title="Luminosidade ao longo do tempo", **get_graph_style())
    return fig

# Callback para exibir o status atual
@app.callback(
    Output('status-display', 'children'),
    Input('update-interval', 'n_intervals')
)
def update_status(n):
    # Aqui você pode adicionar o código para capturar o status
    # Se você não estiver recebendo o status via MQTT, pode exibir uma mensagem padrão
    return "Status Atual: Aguardando dados..."

# Iniciando o servidor Dash
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
