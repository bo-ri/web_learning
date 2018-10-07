FROM jupyter/datascience-notebook
MAINTAINER TatsuyaKITABORI

RUN pip install tensorflow
RUN jupyter serverextension enable --py jupyterlab
