
def start_cli():
    import fire
    from .cli import CLI

    return fire.Fire(CLI())
