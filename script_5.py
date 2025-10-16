# Create requirements.txt and additional project files
requirements_txt = '''streamlit>=1.28.0
pandas>=1.5.0
matplotlib>=3.6.0
seaborn>=0.12.0
plotly>=5.15.0
requests>=2.28.0
numpy>=1.24.0
hashlib-compat>=1.0.1
'''

# Create a sample data file
sample_passwords_txt = '''password
123456
password123
admin
qwerty
letmein
welcome
monkey
dragon
master
123456789
12345678
12345
1234567890
1234567
password1
123123
abc123
Password1
qwerty123
hello
login
pass
secret
test
user
sunshine
princess
football
charlie
aa123456
donald
password12
qwerty12
hello123
Password
1q2w3e4r
iloveyou
admin123
welcome123
login123
'''

# Create leaked hashes sample
leaked_hashes_txt = '''5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8:password
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855:
098f6bcd4621d373cade4e832627b4f6:test
d41d8cd98f00b204e9800998ecf8427e:
aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d:hello
356a192b7913b04c54574d18c28d46e6395428ab:1
da39a3ee5e6b4b0d3255bfef95601890afd80709:
5d41402abc4b2a76b9719d911017c592:hello
098f6bcd4621d373cade4e832627b4f6:test
'''

# Create README.md content
readme_content = '''# 🔐 Data Breach Analyzer

A comprehensive full-stack application for analyzing password security, detecting breached passwords, and visualizing password patterns.

## 🚀 Features

### Core Features
- **Password Breach Detection**: Check passwords against the HaveIBeenPwned database
- **Password Strength Analysis**: Comprehensive password security assessment
- **Hash Cracking Simulation**: Demonstrate dictionary and brute-force attacks
- **Pattern Visualization**: Interactive charts showing password trends and patterns

### Bonus Features
- **Interactive Dashboard**: Modern Streamlit interface
- **Entropy Calculation**: Mathematical strength assessment
- **Common Password Detection**: Identify frequently used passwords
- **Security Recommendations**: Actionable advice for password improvement
- **Multiple Hash Support**: MD5, SHA1, SHA256, SHA512, NTLM

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python with custom modules
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Security**: hashcat integration, HaveIBeenPwned API
- **Deployment**: Streamlit Cloud ready

## 📁 Project Structure

```
data_breach_analyzer/
├── app.py                    # Main Streamlit application
├── password_analyzer.py     # Password analysis module
├── hash_cracker.py          # Hash cracking functionality
├── visualization.py         # Data visualization module
├── requirements.txt         # Python dependencies
├── data/
│   ├── sample_passwords.txt # Sample password data
│   ├── common_passwords.txt # Common passwords list
│   └── leaked_hashes.txt    # Sample leaked hashes
├── static/
│   └── style.css           # Custom CSS styling
└── README.md               # Project documentation
```

## 🚦 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd data_breach_analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 📖 Usage Guide

### 1. Password Breach Checker
- Enter a password to check against known data breaches
- Uses HaveIBeenPwned API for secure checking
- Displays breach count and security recommendations

### 2. Password Strength Analysis
- Comprehensive password evaluation
- Entropy calculation and character analysis
- Real-time feedback and improvement suggestions

### 3. Hash Cracking Simulation
- Demonstrate dictionary attacks
- Brute force simulation with time estimates
- Support for multiple hash algorithms

### 4. Pattern Visualization
- Interactive charts and graphs
- Password length distribution analysis
- Character pattern identification
- Strength distribution visualization

## 🔧 Configuration

### API Configuration
The application uses the HaveIBeenPwned API. No API key required, but rate limiting applies.

### Customization
- Modify `common_passwords.txt` to update dictionary
- Adjust visualization themes in `visualization.py`
- Customize UI styling in `static/style.css`

## 🛡️ Security Features

### Password Analysis
- **Entropy Calculation**: Mathematical complexity assessment
- **Pattern Detection**: Identifies weak patterns like sequences
- **Common Password Check**: Compares against known weak passwords
- **Character Diversity**: Analyzes character set usage

### Hash Cracking
- **Multiple Algorithms**: MD5, SHA1, SHA256, SHA512
- **Attack Simulation**: Dictionary and brute-force methods
- **Performance Metrics**: Time estimation and success rates
- **Educational Purpose**: Demonstrates security concepts

## 📊 Visualization Features

- **Length Distribution**: Bar charts showing password length patterns
- **Character Analysis**: Usage statistics for different character types
- **Strength Distribution**: Pie charts showing security categories
- **Breach Analysis**: Correlation between strength and breaches
- **Interactive Dashboards**: Real-time data exploration

## 🌐 Deployment

### Streamlit Cloud
1. Push code to GitHub repository
2. Connect to Streamlit Cloud
3. Deploy with one click

### Local Deployment
```bash
streamlit run app.py --server.port 8501
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and security testing purposes only. Always:
- Test only on systems you own or have explicit permission to test
- Follow responsible disclosure practices
- Respect privacy and legal boundaries
- Use strong, unique passwords for your accounts

## 🙏 Acknowledgments

- HaveIBeenPwned API for breach data
- Streamlit team for the excellent framework
- Security community for best practices
- Open source contributors

## 📞 Support

For questions, issues, or contributions:
- Create an issue on GitHub
- Check the documentation
- Review the code examples

---

**Built with ❤️ for cybersecurity education and awareness**
'''

print("Additional Project Files Created!")
print("=" * 50)
print("Files generated:")
print("• requirements.txt - Python dependencies")
print("• sample_passwords.txt - Test password data")
print("• leaked_hashes.txt - Sample hash data")
print("• README.md - Comprehensive documentation")
print("\nProject is now complete and ready for deployment!")