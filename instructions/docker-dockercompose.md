# Install Docker Engine on Ubuntu

## Set up the repository

- Update the apt package index and install packages to allow apt to use a repository over HTTPS:
  ```shell
  sudo apt-get update
  sudo apt-get install ca-certificates curl gnupg
  ```
- Add Docker’s official GPG key:
  ```shell
  sudo install -m 0755 -d /etc/apt/keyrings
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  sudo chmod a+r /etc/apt/keyrings/docker.gpg
  ```
- Use the following command to set up the repository:
  ```shell
  echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```

## Install Docker Engine

- Update the apt package index:
  ```shell
  sudo apt-get update
  ```
- Install Docker Engine:
  ```shell
  sudo apt install docker-ce
  ```
- Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it’s running:
  ```shell
  sudo systemctl status docker
  ```

## Executing the Docker Command Without Sudo

- If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group:
  ```shell
  sudo usermod -aG docker ${USER}
  ```
- To apply the new group membership, log out of the server and back in, or type the following:
  ```shell
  su - ${USER}
  ```
  You will be prompted to enter your user’s password to continue.
- Confirm that your user is now added to the docker group by typing:
  ```shell
  id -nG
  ```

## Installing Docker Compose

- Check the [current release](https://github.com/docker/compose/releases) and if necessary, update it in the command below:
  ```shell
  sudo curl -L https://github.com/docker/compose/releases/download/v2.10.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
  ```
- Next set the permissions:
  ```shell
  sudo chmod +x /usr/local/bin/docker-compose
  ```
- Then you’ll verify that the installation was successful by checking the version:
  ```shell
  docker-compose --version
  ```

## Reference

- [Docker](https://docs.docker.com/engine/install/ubuntu/)
