# build with the following command
# sudo docker build -t paramak .

# Run with the follwoing command
# sudo docker run -it paramak

# We will use an Ubuntu based binder and jupyter compatable base image
# FROM jupyter/minimal-notebook
FROM continuumio/anaconda3

# USER $NB_USER
# USER root
RUN conda config --add channels conda-forge
# RUN conda update --all
# RUN conda update -n base conda
RUN conda install --quiet --yes -c conda-forge -c cadquery cadquery=2
# RUN conda install  numpy
# RUN conda install  plotly
# RUN conda install  tqdm
# RUN conda install  matplotlib
# RUN conda install  trimesh
# RUN conda install  pandas
# RUN conda install  pyrender
# RUN conda install  uncertainties
# RUN conda install  importlib_resources
RUN conda install  git


RUN git clone --branch binder https://github.com/ukaea/paramak

# WORKDIR paramak