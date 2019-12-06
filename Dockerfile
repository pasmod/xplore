FROM jupyter/minimal-notebook:7a0c7325e470


# Define working directory
RUN mkdir -p /opt/app
WORKDIR /opt/app

# Install requirements
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install widget extension for notebooks
RUN jupyter nbextension enable --py widgetsnbextension
#RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager

# Set Python path
ENV PYTHONPATH /opt/app
