import logging
import os
from datetime import datetime

# logs klasörünü oluştur
os.makedirs("logs", exist_ok=True)

# Log dosyasının adı
LOG_FILE = f"logs/app_{datetime.now().strftime('%Y%m%d')}.log"

# Logger oluştur
logger = logging.getLogger("notep_api")
logger.setLevel(logging.DEBUG)

# Dosya handler
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Format
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Handler'ları ekle
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)