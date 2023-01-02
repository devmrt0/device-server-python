"""
Uygulama Çalıştırma Dosyası
"""
import sys
from app import app

sys.dont_write_bytecode = True
app.run(host='127.0.0.1', port=8080, debug=True)
