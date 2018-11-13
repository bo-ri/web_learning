FROM jupyter/datascience-notebook
MAINTAINER TatsuyaKITABORI

RUN pip install tensorflow
RUN pip install pydotplus

USER root

RUN apt-get update
RUN apt-get install -y graphviz

RUN jupyter serverextension enable --py jupyterlab
