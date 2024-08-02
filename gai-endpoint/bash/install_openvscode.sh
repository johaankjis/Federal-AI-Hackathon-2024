OSS_VSCODE_VERSION="1.91.1"
cd /opt && mkdir -p openvscode-server
wget https://github.com/gitpod-io/openvscode-server/releases/download/openvscode-server-v1.91.1/openvscode-server-v${OSS_VSCODE_VERSION}-linux-x64.tar.gz
tar -xzf openvscode-server-v${OSS_VSCODE_VERSION}-linux-x64.tar.gz
mv openvscode-server-v${OSS_VSCODE_VERSION}-linux-x64 openvscode-server
cd openvscode-server
touch ~/.VSCODE_TOKEN_FILE
echo "123456789" > ~/.VSCODE_TOKEN_FILE

# start the server
./bin/openvscode-server --host 0.0.0.0  --port 9001 --connection-token-file ~/.VSCODE_TOKEN_FILE
