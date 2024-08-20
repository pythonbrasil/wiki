FROM ubuntu:24.04

RUN mkdir -p /home/wiki
COPY . /home/wiki
WORKDIR /home/wiki
RUN bash install_os_dependencies.sh install
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/python3 -m pip install -r requirements.txt
ENV PATH="/opt/venv/bin:$PATH"
CMD ["/bin/bash", "develop_server.sh", "docker_start"]
