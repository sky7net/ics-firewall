from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import config_manager, log_reader


app = Flask(__name__)
app.secret_key = 'supersecretkey'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Mock user database
users = {"admin": {"password": "admin123"}}
# Değiştirilemez kural ID'leri
IMMUTABLE_RULE_IDS = ["block_nmap_scan", "another_fixed_rule_id"]

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username]["password"] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash("Login failed. Check your username and password.")
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def dashboard():
    logs = log_reader.get_latest_logs()
    return render_template('dashboard.html', logs=logs)

@app.route('/config', methods=['GET', 'POST'])
@login_required
def config():
    if request.method == 'POST':
        # Tüm kuralları yükle
        rules = config_manager.load_rules()
        
        # Her kuralı güncelle (değiştirilemez kurallar dışında)
        for i, rule in enumerate(rules):
            # Eğer kural ID'si değiştirilemez listesinde varsa güncellemeyi geç
            if rule.get('rule_id') in IMMUTABLE_RULE_IDS:
                continue

            # Güncellenebilir kuralları form verileri ile güncelle
            rule['source'] = request.form.get(f'source_{i+1}')
            rule['destination'] = request.form.get(f'destination_{i+1}')
            rule['protocol'] = request.form.get(f'protocol_{i+1}')
            rule['action'] = request.form.get(f'action_{i+1}')

        # Güncellenen kuralları kaydet
        config_manager.save_rules(rules)
        flash("Kurallar başarıyla güncellendi.")
        return redirect(url_for('config'))

    # GET isteği için mevcut yapılandırma ve kuralları yükle
    current_config = config_manager.load_config()
    all_rules = config_manager.load_rules()
    # Sadece düzenlenebilir kuralları şablona gönder
    editable_rules = [rule for rule in all_rules if rule.get('rule_id') not in IMMUTABLE_RULE_IDS]
    return render_template('config.html', config=current_config, rules=editable_rules)
if __name__ == '__main__':
    app.run(debug=True)
