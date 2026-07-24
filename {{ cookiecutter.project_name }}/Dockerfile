FROM ubuntu:rolling

RUN apt update

RUN <<EOF
set -e
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get --no-install-recommends install -y git python3 python3-venv
rm -rf /var/lib/apt/lists/*
EOF

RUN mkdir /src

USER ubuntu

RUN <<EOF
set -e
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh | bash
. "$HOME/.nvm/nvm.sh"
nvm install 26
EOF

WORKDIR /src
