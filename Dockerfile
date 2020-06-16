# build with the following command
# sudo docker build -t paramak .

# Run with the follwoing command
# sudo docker run -it paramak

# We will use an Ubuntu based binder and jupyter compatable base image
FROM jupyter/minimal-notebook:1386e2046833

USER root

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y libgl1-mesa-glx libglu1-mesa && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

RUN conda install --yes \
      -c pythonocc \
      -c oce \
      -c dlr-sc \
      -c conda-forge \
      -c cadquery \
      -c defaults \
      oce=0.18.3 \
      pythonocc-core=0.18.2 \
    && fix-permissions $CONDA_DIR \
    && fix-permissions /home/$NB_USER

RUN pip install \
      dataclasses \
      git+https://github.com/CadQuery/cadquery.git \
      pythreejs==2.1.1

# RUN git clone https://github.com/bernhard-42/jupyter-cadquery.git \
#     && pip install ./jupyter-cadquery \
#     && jupyter-labextension install ./jupyter-cadquery/js

# Make sure the contents of our repo are in ${HOME}
RUN cd paramak && python setup.py install

COPY . ${HOME}


# RUN git clone --branch binder https://github.com/ukaea/paramak

# RUN conda install -c conda-forge notebook

# WORKDIR paramak