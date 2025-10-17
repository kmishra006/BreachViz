# Let's create a comprehensive Data Breach Analyzer project structure
import os
import json

# Load breached passwords once
with open("breached_passwords.txt", "r", encoding="utf-8") as file:
    breached_passwords = set(line.strip() for line in file)

def check_password_risk(password):
    """
    Returns True if password is found in breached dataset, else False
    """
    return password in breached_passwords


# Define the project structure
project_structure = {
    "data_breach_analyzer/": {
        "app.py": "Main Streamlit application",
        "requirements.txt": "Project dependencies",
        "password_analyzer.py": "Core password analysis module",
        "hash_cracker.py": "Hash cracking functionality",
        "visualization.py": "Password pattern visualization",
        "data/": {
            "sample_passwords.txt": "Sample password data",
            "common_passwords.txt": "Common passwords list",
            "leaked_hashes.txt": "Sample leaked hashes"
        },
        "static/": {
            "style.css": "Custom CSS styling"
        },
        "templates/": {
            "README.md": "Project documentation"
        }
    }
}

# Create a detailed plan for the project
project_plan = {
    "tech_stack": ["Python", "Streamlit", "hashcat", "matplotlib", "seaborn", "pandas", "requests"],
    "core_features": [
        "Password breach checking using HaveIBeenPwned API",
        "Password strength analysis",
        "Hash cracking simulation",
        "Password pattern visualization",
        "Statistical analysis of password data"
    ],
    "bonus_features": [
        "Interactive dashboard",
        "Password entropy calculation", 
        "Common password detection",
        "Breach timeline visualization",
        "Password improvement suggestions"
    ],
    "modules": {
        "password_analyzer.py": [
            "Password strength calculation",
            "Entropy analysis",
            "Common password checking",
            "HaveIBeenPwned API integration"
        ],
        "hash_cracker.py": [
            "Hash type detection",
            "Dictionary attack simulation",
            "Brute force simulation",
            "Hashcat integration wrapper"
        ],
        "visualization.py": [
            "Password pattern charts",
            "Strength distribution plots",
            "Breach statistics visualization",
            "Interactive dashboards"
        ]
    }
}

print("Data Breach Analyzer Project Structure:")
print("=" * 50)
for item, description in project_structure["data_breach_analyzer/"].items():
    if isinstance(description, dict):
        print(f"📁 {item}")
        for subitem, subdesc in description.items():
            print(f"   📄 {subitem} - {subdesc}")
    else:
        print(f"📄 {item} - {description}")

print("\n\nProject Plan:")
print("=" * 50)
print("Tech Stack:", ", ".join(project_plan["tech_stack"]))
print("\nCore Features:")
for feature in project_plan["core_features"]:
    print(f"  • {feature}")
print("\nBonus Features:")  
for feature in project_plan["bonus_features"]:
    print(f"  • {feature}")
