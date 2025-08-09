# Deploy de API para Geração de Texto a Partir de Imagens com LLM

Este projeto descreve o processo de deploy de uma API que utiliza um modelo de linguagem de grande escala (LLM) para gerar texto a partir de imagens. As instruções a seguir detalham como configurar o ambiente, construir e executar a aplicação utilizando o Docker, além de executar o cliente para interagir com a API.

## Pré-requisitos

Antes de iniciar, certifique-se de que você possui as seguintes ferramentas instaladas:

- **Docker**: Utilizado para criar, gerenciar e executar contêineres que isolam a aplicação e suas dependências.
- **Python**: Necessário para executar o script cliente (`cliente.py`). Recomenda-se a versão 3.8 ou superior.
- **Git** (opcional): Para clonar o repositório do projeto, caso esteja hospedado em um controle de versão.

### Sobre o Docker

O Docker é uma plataforma de contêinerização que permite empacotar uma aplicação e suas dependências em uma unidade isolada chamada contêiner. Isso garante consistência entre diferentes ambientes (desenvolvimento, teste e produção). As principais ferramentas do Docker utilizadas neste projeto são:

- **Docker CLI**: Interface de linha de comando para interagir com o Docker, usada para construir imagens, executar contêineres e visualizar logs.
- **Dockerfile**: Arquivo de configuração que define como a imagem da aplicação será construída.
- **Docker Engine**: O motor que gerencia a criação e execução de contêineres.

### Instalação do Docker

Para instalar o Docker, siga as instruções abaixo conforme seu sistema operacional:

#### Linux (Ubuntu/Debian)
1. Atualize os pacotes do sistema:
   ```bash
   sudo apt update
   sudo apt install -y docker.io
   ```
2. Inicie e habilite o serviço do Docker:
   ```bash
   sudo systemctl start docker
   sudo systemctl enable docker
   ```
3. Adicione seu usuário ao grupo Docker para executar comandos sem `sudo` (opcional):
   ```bash
   sudo usermod -aG docker $USER
   ```
   Após isso, faça logout e login novamente.

#### Windows
1. Baixe o instalador do **Docker Desktop** no site oficial: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).
2. Execute o instalador e siga as instruções na tela.
3. Certifique-se de que o Docker Desktop está rodando e que o Docker CLI está acessível via terminal (PowerShell ou CMD).

#### macOS
1. Baixe o **Docker Desktop** no site oficial: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).
2. Instale o aplicativo e inicie o Docker Desktop.
3. Verifique se o Docker CLI está disponível no terminal.

#### Verificação da Instalação
Para confirmar que o Docker está instalado corretamente, execute:
```bash
docker --version
```
Você deve ver a versão instalada, por exemplo: `Docker version 24.x.x`.

## Instruções para Execução do Projeto

Siga os passos abaixo para configurar e executar a API:

1. **Navegue até o diretório do projeto**:
   Abra o terminal ou prompt de comando e vá até a pasta onde os arquivos do projeto estão localizados. Por exemplo:
   ```bash
   cd /caminho/para/o/projeto
   ```

2. **Crie a imagem Docker**:
   Execute o comando abaixo para construir a imagem Docker a partir do `Dockerfile` presente no diretório:
   ```bash
   docker build -t deploy:p4 .
   ```
   - O parâmetro `-t deploy:p4` nomeia a imagem como `deploy` com a tag `p4`.
   - O ponto (`.`) indica que o `Dockerfile` está no diretório atual.

3. **Crie e inicie o contêiner Docker**:
   Execute o comando abaixo para criar e iniciar um contêiner a partir da imagem construída:
   ```bash
   docker run -dit --name p4 -p 3000:3000 deploy:p4
   ```
   - `--name p4`: Nomeia o contêiner como `p4`.
   - `-p 3000:3000`: Mapeia a porta 3000 do contêiner para a porta 3000 do host, permitindo acesso à API.
   - `-dit`: Executa o contêiner em modo interativo, detached e com um terminal.

4. **Verifique os logs da API**:
   Para confirmar que a API foi inicializada corretamente, visualize os logs do contêiner:
   ```bash
   docker logs p4
   ```
   Procure por mensagens que indiquem que o servidor está ativo, como "Server running on port 3000" ou similar.

5. **Execute o cliente**:
   Com a API rodando, execute o script cliente para interagir com ela:
   ```bash
   python cliente.py
   ```
   - Certifique-se de que o Python está instalado e que o script `cliente.py` está no diretório atual.
   - Caso necessário, instale dependências do script com `pip install -r requirements.txt` (se um arquivo `requirements.txt` estiver presente).

## Solução de Problemas

- **Erro: "Docker: command not found"**:
  Verifique se o Docker está instalado e se o comando `docker` está disponível no PATH do sistema.
- **Erro ao executar `python cliente.py`**:
  Confirme que o Python está instalado (`python --version`) e que as dependências necessárias estão instaladas.
- **API não responde na porta 3000**:
  Verifique se o contêiner está rodando com `docker ps` e se a porta está mapeada corretamente. Certifique-se de que não há outro serviço utilizando a porta 3000.
- **Logs mostram erros**:
  Analise os logs com `docker logs p4` para identificar a causa do problema, como dependências ausentes ou configurações incorretas no `Dockerfile`.

## Notas Adicionais

- **Dockerfile**: Certifique-se de que o `Dockerfile` está configurado corretamente para instalar todas as dependências da API e expor a porta 3000.
- **Segurança**: Evite expor a porta 3000 publicamente em ambientes de produção sem configurações de segurança adequadas, como firewalls ou autenticação.
- **Limpeza**: Para remover o contêiner após o uso, execute:
  ```bash
  docker rm -f p4
  ```
  Para remover a imagem:
  ```bash
  docker rmi deploy:p4
  ```

Se precisar de assistência adicional ou ajustes no projeto, entre em contato comigo: **m.marques.professional@gmail.com**