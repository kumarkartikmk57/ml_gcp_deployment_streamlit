FROM python:3.9-slim

EXPOSE 8501

WORKDIR /app
COPY streamlit_app.py /app
COPY laptop_pred.pkl /app 
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install streamlit
RUN pip3 install sklearn
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]


