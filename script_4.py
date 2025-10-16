# Create the visualization module
visualization_code = '''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import random
from collections import Counter

class PasswordVisualizer:
    def __init__(self):
        self.color_palette = [
            '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', 
            '#FFEAA7', '#DDA0DD', '#98D8C8', '#F7DC6F'
        ]
    
    def generate_sample_data(self, n_samples=1000):
        """Generate sample password data for visualization"""
        np.random.seed(42)
        random.seed(42)
        
        # Generate realistic password length distribution
        length_weights = {4: 5, 5: 8, 6: 15, 7: 20, 8: 25, 9: 12, 10: 8, 11: 4, 12: 2, 13: 1}
        lengths = []
        for length, weight in length_weights.items():
            lengths.extend([length] * weight)
        
        sample_lengths = np.random.choice(lengths, size=n_samples)
        
        # Generate character composition data
        sample_data = []
        for i in range(n_samples):
            length = sample_lengths[i]
            
            # Determine character composition based on realistic patterns
            has_upper = np.random.choice([True, False], p=[0.3, 0.7])
            has_lower = np.random.choice([True, False], p=[0.8, 0.2])
            has_digit = np.random.choice([True, False], p=[0.6, 0.4])
            has_special = np.random.choice([True, False], p=[0.2, 0.8])
            
            # Calculate strength score
            strength = self._calculate_sample_strength(length, has_upper, has_lower, has_digit, has_special)
            
            # Determine if password is breached (realistic distribution)
            is_breached = np.random.choice([True, False], p=[0.15, 0.85])
            
            sample_data.append({
                'id': i + 1,
                'length': length,
                'has_uppercase': has_upper,
                'has_lowercase': has_lower,
                'has_digits': has_digit,
                'has_special': has_special,
                'strength_score': strength,
                'is_breached': is_breached,
                'category': self._get_strength_category(strength)
            })
        
        return pd.DataFrame(sample_data)
    
    def _calculate_sample_strength(self, length, has_upper, has_lower, has_digit, has_special):
        """Calculate sample strength score"""
        score = 0
        
        # Length component
        if length >= 12:
            score += 30
        elif length >= 8:
            score += 20
        elif length >= 6:
            score += 10
        
        # Character diversity
        char_types = sum([has_upper, has_lower, has_digit, has_special])
        score += char_types * 15
        
        # Add some randomness
        score += np.random.randint(-10, 11)
        
        return max(0, min(100, score))
    
    def _get_strength_category(self, score):
        """Get strength category from score"""
        if score >= 80:
            return "Strong"
        elif score >= 60:
            return "Medium"
        else:
            return "Weak"
    
    def plot_length_distribution(self, data):
        """Create password length distribution plot"""
        length_counts = data['length'].value_counts().sort_index()
        
        fig = px.bar(
            x=length_counts.index,
            y=length_counts.values,
            title="Password Length Distribution",
            labels={'x': 'Password Length (characters)', 'y': 'Frequency'},
            color=length_counts.values,
            color_continuous_scale='viridis'
        )
        
        fig.update_layout(
            title_font_size=20,
            title_x=0.5,
            showlegend=False,
            height=400
        )
        
        return fig
    
    def plot_character_patterns(self, data):
        """Create character pattern analysis plot"""
        # Calculate percentages
        patterns = {
            'Uppercase Letters': data['has_uppercase'].mean() * 100,
            'Lowercase Letters': data['has_lowercase'].mean() * 100,
            'Digits': data['has_digits'].mean() * 100,
            'Special Characters': data['has_special'].mean() * 100
        }
        
        fig = px.bar(
            x=list(patterns.keys()),
            y=list(patterns.values()),
            title="Character Type Usage in Passwords",
            labels={'x': 'Character Type', 'y': 'Usage Percentage (%)'},
            color=list(patterns.values()),
            color_continuous_scale='RdYlBu_r'
        )
        
        fig.update_layout(
            title_font_size=20,
            title_x=0.5,
            showlegend=False,
            height=400
        )
        
        # Add percentage labels on bars
        fig.update_traces(
            texttemplate='%{y:.1f}%',
            textposition='outside'
        )
        
        return fig
    
    def plot_character_composition(self):
        """Create character composition pie chart"""
        # Sample composition data
        composition_data = {
            'Letters Only': 25,
            'Letters + Numbers': 45,
            'Letters + Special': 15,
            'All Character Types': 15
        }
        
        fig = px.pie(
            values=list(composition_data.values()),
            names=list(composition_data.keys()),
            title="Password Character Composition",
            color_discrete_sequence=self.color_palette
        )
        
        fig.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=400
        )
        
        return fig
    
    def plot_strength_distribution(self, data):
        """Create password strength distribution plot"""
        # Create strength categories
        strength_counts = data['category'].value_counts()
        
        # Define colors for each category
        color_map = {'Strong': '#2ECC71', 'Medium': '#F39C12', 'Weak': '#E74C3C'}
        colors = [color_map[cat] for cat in strength_counts.index]
        
        fig = px.pie(
            values=strength_counts.values,
            names=strength_counts.index,
            title="Password Strength Distribution",
            color_discrete_sequence=colors
        )
        
        fig.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=400
        )
        
        # Add percentage annotations
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            textfont_size=12
        )
        
        return fig
    
    def plot_strength_vs_length(self, data):
        """Create strength vs length scatter plot"""
        fig = px.scatter(
            data,
            x='length',
            y='strength_score',
            color='category',
            title="Password Strength vs Length",
            labels={'length': 'Password Length', 'strength_score': 'Strength Score'},
            color_discrete_map={'Strong': '#2ECC71', 'Medium': '#F39C12', 'Weak': '#E74C3C'}
        )
        
        fig.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=500
        )
        
        return fig
    
    def plot_breach_analysis(self, data):
        """Create breach analysis visualization"""
        # Create subplots
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Breach Status by Strength', 'Breach Rate by Length'),
            specs=[[{'type': 'bar'}, {'type': 'bar'}]]
        )
        
        # Breach status by strength
        breach_by_strength = data.groupby(['category', 'is_breached']).size().unstack(fill_value=0)
        breach_by_strength_pct = breach_by_strength.div(breach_by_strength.sum(axis=1), axis=0) * 100
        
        fig.add_trace(
            go.Bar(
                name='Not Breached',
                x=breach_by_strength_pct.index,
                y=breach_by_strength_pct[False],
                marker_color='#2ECC71'
            ),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Bar(
                name='Breached',
                x=breach_by_strength_pct.index,
                y=breach_by_strength_pct[True],
                marker_color='#E74C3C'
            ),
            row=1, col=1
        )
        
        # Breach rate by length
        breach_by_length = data.groupby('length')['is_breached'].mean() * 100
        
        fig.add_trace(
            go.Bar(
                name='Breach Rate (%)',
                x=breach_by_length.index,
                y=breach_by_length.values,
                marker_color='#3498DB',
                showlegend=False
            ),
            row=1, col=2
        )
        
        fig.update_layout(
            title_text="Password Breach Analysis",
            title_font_size=20,
            title_x=0.5,
            height=500
        )
        
        return fig
    
    def plot_entropy_distribution(self, sample_entropies):
        """Create entropy distribution plot"""
        fig = px.histogram(
            x=sample_entropies,
            nbins=20,
            title="Password Entropy Distribution",
            labels={'x': 'Entropy (bits)', 'y': 'Frequency'},
            color_discrete_sequence=['#9B59B6']
        )
        
        fig.add_vline(
            x=np.mean(sample_entropies),
            line_dash="dash",
            line_color="red",
            annotation_text=f"Mean: {np.mean(sample_entropies):.1f} bits"
        )
        
        fig.update_layout(
            title_font_size=20,
            title_x=0.5,
            height=400
        )
        
        return fig
    
    def create_dashboard_summary(self, data):
        """Create summary statistics for dashboard"""
        total_passwords = len(data)
        weak_passwords = len(data[data['category'] == 'Weak'])
        breached_passwords = len(data[data['is_breached'] == True])
        avg_length = data['length'].mean()
        avg_strength = data['strength_score'].mean()
        
        return {
            'total_passwords': total_passwords,
            'weak_passwords': weak_passwords,
            'weak_percentage': (weak_passwords / total_passwords) * 100,
            'breached_passwords': breached_passwords,
            'breach_percentage': (breached_passwords / total_passwords) * 100,
            'avg_length': round(avg_length, 1),
            'avg_strength': round(avg_strength, 1),
            'most_common_length': data['length'].mode()[0],
            'strongest_passwords': len(data[data['category'] == 'Strong'])
        }
    
    def generate_heatmap_data(self):
        """Generate data for password pattern heatmap"""
        # Create sample data for common password patterns
        patterns = [
            'Sequential (123, abc)', 'Repetitive (aaa, 111)', 'Dictionary Words',
            'Keyboard Patterns', 'Personal Info', 'Common Substitutions',
            'Years/Dates', 'Names + Numbers', 'Simple Patterns', 'Random Characters'
        ]
        
        categories = ['Weak', 'Medium', 'Strong']
        
        # Generate realistic distribution
        np.random.seed(42)
        heatmap_data = []
        
        for pattern in patterns:
            for category in categories:
                if pattern == 'Random Characters':
                    # Random chars more common in strong passwords
                    if category == 'Strong':
                        value = np.random.randint(60, 90)
                    elif category == 'Medium':
                        value = np.random.randint(20, 40)
                    else:
                        value = np.random.randint(5, 20)
                elif pattern in ['Sequential (123, abc)', 'Repetitive (aaa, 111)']:
                    # These patterns more common in weak passwords
                    if category == 'Weak':
                        value = np.random.randint(50, 80)
                    elif category == 'Medium':
                        value = np.random.randint(20, 40)
                    else:
                        value = np.random.randint(5, 15)
                else:
                    # Other patterns have varied distributions
                    if category == 'Weak':
                        value = np.random.randint(30, 60)
                    elif category == 'Medium':
                        value = np.random.randint(25, 45)
                    else:
                        value = np.random.randint(15, 35)
                
                heatmap_data.append({
                    'Pattern': pattern,
                    'Strength': category,
                    'Frequency': value
                })
        
        return pd.DataFrame(heatmap_data)
'''

print("Password Visualization Module Created!")
print("=" * 50)
print("Features implemented:")
print("• Length distribution plots")
print("• Character pattern analysis")
print("• Strength distribution charts")
print("• Breach analysis visualizations")
print("• Interactive Plotly charts")
print("• Dashboard summary statistics")