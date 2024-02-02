FROM jupyter/datascience-notebook:latest

RUN pip3 install -U transformers
RUN pip3 install -U pillow
RUN pip3 install -U torch
RUN pip3 install -U datasets
RUN pip3 install -U pip install pydot==2.0.0
RUN pip3 install seaborn

ENV DISPLAY=:99

USER root
RUN sudo apt-get update -y
RUN apt-get install graphviz -y