from src.settings import FILES_PATH


def get_all_phishing_domains():
    with open(FILES_PATH / 'ALL-phishing-domains.txt', 'r') as f:
        fread = f.read()
        return list(filter(None, fread.split('\n')))
