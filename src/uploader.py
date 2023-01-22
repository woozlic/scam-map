import requests
import tarfile
from src.settings import SRC_PATH, FILES_PATH


def download_phishing_domains():
    res = requests.get('https://github.com/mitchellkrogza/Phishing.Database/raw/master/ALL-phishing-domains.tar.gz',
                       stream=True)
    file = tarfile.open(fileobj=res.raw, mode="r|gz")
    file.extractall(path=FILES_PATH)


if __name__ == '__main__':
    download_phishing_domains()
