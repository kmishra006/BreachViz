import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Create a comprehensive architecture diagram using Plotly
fig = go.Figure()

# Define layers and their components
layers = {
    'Frontend': {
        'y': 0.8,
        'components': ['Streamlit Dashboard', 'Password Breach Check', 'Strength Analysis', 'Hash Cracking', 'Visualization'],
        'color': '#1FB8CD'
    },
    'Backend': {
        'y': 0.6,
        'components': ['password_analyzer.py', 'hash_cracker.py', 'visualization.py'],
        'color': '#2E8B57'
    },
    'Data': {
        'y': 0.4,
        'components': ['sample_passwords.txt', 'leaked_hashes.txt', 'common_passwords.txt'],
        'color': '#D2BA4C'
    },
    'External/Tools': {
        'y': 0.2,
        'components': ['HaveIBeenPwned API', 'Matplotlib/Seaborn/Plotly', 'hashcat integration'],
        'color': '#DB4545'
    }
}

# Add layer backgrounds
for layer_name, layer_info in layers.items():
    fig.add_shape(
        type="rect",
        x0=-0.1, y0=layer_info['y']-0.08,
        x1=1.1, y1=layer_info['y']+0.08,
        fillcolor=layer_info['color'],
        opacity=0.1,
        line=dict(width=0)
    )

# Add components as nodes
x_positions = []
y_positions = []
component_names = []
colors = []
sizes = []

for layer_name, layer_info in layers.items():
    num_components = len(layer_info['components'])
    for i, component in enumerate(layer_info['components']):
        x = (i + 1) / (num_components + 1)
        y = layer_info['y']
        
        x_positions.append(x)
        y_positions.append(y)
        component_names.append(component)
        colors.append(layer_info['color'])
        
        # Adjust size based on component importance
        if 'Dashboard' in component:
            sizes.append(60)
        elif any(ext in component for ext in ['.py', 'API', 'hashcat']):
            sizes.append(45)
        else:
            sizes.append(35)

# Add nodes
fig.add_trace(go.Scatter(
    x=x_positions,
    y=y_positions,
    mode='markers+text',
    marker=dict(
        size=sizes,
        color=colors,
        line=dict(width=2, color='white'),
        opacity=0.8
    ),
    text=component_names,
    textposition='middle center',
    textfont=dict(size=9, color='white'),
    hovertemplate='<b>%{text}</b><extra></extra>',
    showlegend=False
))

# Define connections between components
connections = [
    # Frontend to Backend
    ('Streamlit Dashboard', 'password_analyzer.py'),
    ('Password Breach Check', 'password_analyzer.py'),
    ('Strength Analysis', 'password_analyzer.py'),
    ('Hash Cracking', 'hash_cracker.py'),
    ('Visualization', 'visualization.py'),
    
    # Backend to Data
    ('password_analyzer.py', 'sample_passwords.txt'),
    ('password_analyzer.py', 'common_passwords.txt'),
    ('hash_cracker.py', 'leaked_hashes.txt'),
    
    # Backend to External/Tools
    ('password_analyzer.py', 'HaveIBeenPwned API'),
    ('visualization.py', 'Matplotlib/Seaborn/Plotly'),
    ('hash_cracker.py', 'hashcat integration')
]

# Add connection lines
for start_comp, end_comp in connections:
    start_idx = component_names.index(start_comp)
    end_idx = component_names.index(end_comp)
    
    fig.add_trace(go.Scatter(
        x=[x_positions[start_idx], x_positions[end_idx]],
        y=[y_positions[start_idx], y_positions[end_idx]],
        mode='lines',
        line=dict(width=2, color='#5D878F', dash='solid'),
        hoverinfo='skip',
        showlegend=False
    ))
    
    # Add arrowhead
    mid_x = (x_positions[start_idx] + x_positions[end_idx]) / 2
    mid_y = (y_positions[start_idx] + y_positions[end_idx]) / 2
    
    fig.add_annotation(
        x=x_positions[end_idx],
        y=y_positions[end_idx],
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor='#5D878F',
        ax=mid_x,
        ay=mid_y,
        text=""
    )

# Add layer labels
for layer_name, layer_info in layers.items():
    fig.add_annotation(
        x=-0.05,
        y=layer_info['y'],
        text=f"<b>{layer_name}</b>",
        showarrow=False,
        font=dict(size=12, color=layer_info['color']),
        textangle=-90
    )

# Update layout
fig.update_layout(
    title="Data Breach Analyzer Architecture",
    xaxis=dict(
        range=[-0.15, 1.15],
        showgrid=False,
        showticklabels=False,
        zeroline=False
    ),
    yaxis=dict(
        range=[0.1, 0.9],
        showgrid=False,
        showticklabels=False,
        zeroline=False
    ),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Save the chart
fig.write_image('architecture_diagram.png')
fig.write_image('architecture_diagram.svg', format='svg')
print("Architecture diagram created successfully!")