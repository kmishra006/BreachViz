# Create a clean data flow diagram for the Data Breach Analyzer
import plotly.graph_objects as go

# Create figure
fig = go.Figure()

# Define nodes with better spacing and organization (top-to-bottom flow)
nodes = [
    # Input layer
    {"id": "input", "name": "User Password<br>Input", "x": 4, "y": 10, "type": "input"},
    
    # Validation layer
    {"id": "validate", "name": "Password<br>Validation<br>(~10ms)", "x": 4, "y": 8.5, "type": "process"},
    {"id": "length_check", "name": "Length >= 6?", "x": 4, "y": 7, "type": "decision"},
    
    # Error path
    {"id": "error", "name": "Error Output<br>Too Short", "x": 1, "y": 5.5, "type": "error"},
    
    # Main processing path
    {"id": "strength", "name": "Calculate<br>Strength<br>(~5ms)", "x": 7, "y": 5.5, "type": "process"},
    {"id": "diversity", "name": "Check Character<br>Diversity<br>(~3ms)", "x": 7, "y": 4, "type": "process"},
    {"id": "entropy", "name": "Calculate<br>Entropy<br>(~2ms)", "x": 7, "y": 2.5, "type": "process"},
    
    # Breach checking
    {"id": "breach_api", "name": "Query HIBP<br>API<br>(~200ms)", "x": 4, "y": 1, "type": "process"},
    {"id": "breach_check", "name": "Breached?", "x": 4, "y": -0.5, "type": "decision"},
    
    # Breach paths
    {"id": "flag_breach", "name": "Flag as<br>Compromised", "x": 1, "y": -2, "type": "process"},
    {"id": "mark_safe", "name": "Mark as<br>Safe", "x": 7, "y": -2, "type": "process"},
    
    # Final processing
    {"id": "hash", "name": "Generate Hash<br>(~1ms)", "x": 4, "y": -3.5, "type": "process"},
    {"id": "crack", "name": "Simulate Crack<br>(~50ms)", "x": 4, "y": -5, "type": "process"},
    {"id": "recommend", "name": "Generate<br>Recommendations", "x": 4, "y": -6.5, "type": "process"},
    
    # Outputs
    {"id": "out1", "name": "Strength<br>Score", "x": 0, "y": -8, "type": "output"},
    {"id": "out2", "name": "Breach<br>Status", "x": 2, "y": -8, "type": "output"},
    {"id": "out3", "name": "Recommendations", "x": 4, "y": -8, "type": "output"},
    {"id": "out4", "name": "Visualizations", "x": 6, "y": -8, "type": "output"},
    {"id": "out5", "name": "Security<br>Analysis", "x": 8, "y": -8, "type": "output"}
]

# Define connections with labels
connections = [
    {"from": "input", "to": "validate", "label": ""},
    {"from": "validate", "to": "length_check", "label": ""},
    {"from": "length_check", "to": "error", "label": "No", "color": "#DB4545"},
    {"from": "length_check", "to": "strength", "label": "Yes", "color": "#2E8B57"},
    {"from": "strength", "to": "diversity", "label": ""},
    {"from": "diversity", "to": "entropy", "label": ""},
    {"from": "entropy", "to": "breach_api", "label": ""},
    {"from": "breach_api", "to": "breach_check", "label": ""},
    {"from": "breach_check", "to": "flag_breach", "label": "Yes", "color": "#DB4545"},
    {"from": "breach_check", "to": "mark_safe", "label": "No", "color": "#2E8B57"},
    {"from": "flag_breach", "to": "hash", "label": ""},
    {"from": "mark_safe", "to": "hash", "label": ""},
    {"from": "hash", "to": "crack", "label": ""},
    {"from": "crack", "to": "recommend", "label": ""},
    {"from": "recommend", "to": "out1", "label": ""},
    {"from": "recommend", "to": "out2", "label": ""},
    {"from": "recommend", "to": "out3", "label": ""},
    {"from": "recommend", "to": "out4", "label": ""},
    {"from": "recommend", "to": "out5", "label": ""}
]

# Color and shape mapping
node_styles = {
    "input": {"color": "#1FB8CD", "symbol": "circle", "size": 25},
    "process": {"color": "#2E8B57", "symbol": "square", "size": 30},
    "decision": {"color": "#D2BA4C", "symbol": "diamond", "size": 25},
    "error": {"color": "#DB4545", "symbol": "square", "size": 25},
    "output": {"color": "#5D878F", "symbol": "circle", "size": 25}
}

# Add nodes
node_dict = {node["id"]: node for node in nodes}
for node in nodes:
    style = node_styles[node["type"]]
    
    fig.add_trace(go.Scatter(
        x=[node["x"]], 
        y=[node["y"]],
        mode='markers+text',
        marker=dict(
            size=style["size"],
            color=style["color"],
            symbol=style["symbol"],
            line=dict(width=2, color='white')
        ),
        text=node["name"],
        textposition="middle center",
        textfont=dict(size=11, color='white'),
        showlegend=False,
        hovertemplate=f"<b>{node['name']}</b><br>Type: {node['type'].title()}<extra></extra>"
    ))

# Add connections
for conn in connections:
    start = node_dict[conn["from"]]
    end = node_dict[conn["to"]]
    line_color = conn.get("color", "#333333")
    
    # Add connection line
    fig.add_trace(go.Scatter(
        x=[start["x"], end["x"]],
        y=[start["y"], end["y"]],
        mode='lines',
        line=dict(color=line_color, width=2),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Add arrow annotation
    fig.add_annotation(
        x=end["x"], y=end["y"],
        ax=start["x"], ay=start["y"],
        xref="x", yref="y",
        axref="x", ayref="y",
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=2,
        arrowcolor=line_color,
        showarrow=True
    )
    
    # Add edge labels for decision branches
    if conn["label"]:
        mid_x = (start["x"] + end["x"]) / 2
        mid_y = (start["y"] + end["y"]) / 2
        fig.add_annotation(
            x=mid_x, y=mid_y,
            text=conn["label"],
            showarrow=False,
            font=dict(size=10, color=line_color),
            bgcolor="white",
            bordercolor=line_color,
            borderwidth=1
        )

# Update layout
fig.update_layout(
    title="Password Analyzer Data Flow",
    xaxis=dict(
        range=[-1, 9], 
        showgrid=False, 
        showticklabels=False, 
        zeroline=False,
        scaleanchor="y",
        scaleratio=1
    ),
    yaxis=dict(
        range=[-9, 11], 
        showgrid=False, 
        showticklabels=False, 
        zeroline=False
    ),
    plot_bgcolor='white',
    paper_bgcolor='white',
    showlegend=False
)

# Save the chart
fig.write_image("password_flow_chart.png")
fig.write_image("password_flow_chart.svg", format="svg")
print("Clean chart saved successfully")