# SmartTrendAI_Python314

## Overview
AI-Powered Market Trend Analyzer compatible with Python 3.14.
Streamlit web interface and console demo included.
This build removes the 'wordcloud' dependency and uses matplotlib-only visuals to avoid build errors on latest Python.

## Run locally
1. Create and activate a virtual environment using your Python 3.14 interpreter
2. Install dependencies
   pip install --upgrade pip
   pip install -r requirements.txt
3. Run console demo
   python src/main.py
4. Run the web app
   streamlit run app.py

## Run on Google Colab
1. Upload the project files to Colab or mount Google Drive.
2. Install requirements
   !pip install --upgrade pip
   !pip install -r requirements.txt
3. Run demo
   !python src/main.py
4. Running Streamlit in Colab requires extra steps (use Ngrok or localtunnel); easiest is to run Streamlit locally.

## Notes
This version avoids packages that need compiled C extensions (like pyarrow) to ensure smooth installs on Python 3.14.