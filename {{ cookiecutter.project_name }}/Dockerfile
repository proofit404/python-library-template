FROM ubuntu:rolling

RUN apt update

RUN <<EOF
set -e
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get --no-install-recommends install -y ca-certificates curl git libatomic1 python3 python3-venv
rm -rf /var/lib/apt/lists/*
EOF

RUN mkdir /src

USER ubuntu

WORKDIR /home/ubuntu

ENV NVM_DIR="/home/ubuntu/.nvm"

RUN <<EOF
set -e
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh | bash
. "$NVM_DIR/nvm.sh"
nvm install 26
EOF

WORKDIR /src
