import os

# Configuration for storage directories

STORAGE_DIR = 'storage/'
ANALYSIS_CACHE_DIR = os.path.join(STORAGE_DIR, 'cache/')

# Ensure storage directories exist

def ensure_storage_dirs():
    os.makedirs(STORAGE_DIR, exist_ok=True)
    os.makedirs(ANALYSIS_CACHE_DIR, exist_ok=True)