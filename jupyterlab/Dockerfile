FROM jupyter/scipy-notebook

# If R and Julia needed:
# FROM jupyter/datascience-notebook

COPY pip-requirements.txt /tmp/
RUN pip install --requirement /tmp/pip-requirements.txt && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

COPY conda-requirements.txt /tmp/
RUN conda install --yes --file /tmp/conda-requirements.txt && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER