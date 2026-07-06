import os
import subprocess

# Read the port assigned by Google Cloud Run dynamically
port = os.environ.get("PORT", "8080")

# Force Streamlit to run using that exact port string
subprocess.run([
    "streamlit", "run", "app.py",
    "--server.port", port,
    "--server.address", "0.0.0.0",
    "--server.enableCORS", "false",
    "--server.enableXsrfProtection", "false"
])
