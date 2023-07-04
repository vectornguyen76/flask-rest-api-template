# Installing Anaconda or Miniconda on Ubuntu:
## Step 1: Update and download wget
- Update OS:
    ```shell
    sudo apt-get update
    ```
- Move to the /tmp directory:
    ```shell
    cd /tmp
    ```
- Install the wget command:
    ```shell
    apt-get install wget
    ```
## Step 2: Install Anaconda or Miniconda
### Install Anaconda
- Download the Anaconda installer - check version here [Anaconda](https://repo.anaconda.com/archive/):
    ```shell
    https://repo.anaconda.com/archive/
    ```
- Once the download is complete, verify the hash code integrity of the package:
    ```shell
    sha256sum Anaconda3-2022.05-Linux-x86_64.sh
    ```
- The output will notify if any errors occurred. If there are no errors, move on to the actual installation step. To continue, run the Anaconda bash shell script:
    ```shell
    bash Anaconda3-2022.05-Linux-x86_64.sh
    ```
### Install Miniconda - use the following commands consecutively
```shell
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
```shell
sha256sum Miniconda3-latest-Linux-x86_64.sh
```
```shell
bash Miniconda3-latest-Linux-x86_64.sh
```
## Step 3: Test the Connection
- With the installation done, the next step is to activate the added environment settings using the following command:
    ```shell
    source ~/.bashrc
    ```
- Then, test out the connection:
    ```shell
    conda info
    ```
## Uninstalling Anaconda
- In order to uninstall Anaconda, install the following anaconda-clean package:
    ```shell
    conda install anaconda-clean
    ```
- Lastly, remove all Anaconda-related files and directories:
    ```shell
    anaconda-clean
    ```

