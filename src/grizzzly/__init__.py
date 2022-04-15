from grizzzly.client.download import download_dataset


def start_cli():
    import fire
    from .cli import CLI

    return fire.Fire(CLI())
