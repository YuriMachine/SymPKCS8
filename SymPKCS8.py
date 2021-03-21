import click
from wrapper.wrap import wrap
from decrypt.decrypt import decrypt


@click.command()
@click.argument('mode',
                type=click.Choice(['wrap', 'decode'], case_sensitive=False))
@click.option('--input', type=click.File('rb'), required=True,
              help='WRAP: Symmetric key to wrap. DECODE: PKCS8 wrapped symmetric key.')
@click.option('--output', type=click.File('w'), required=True,
              help='WRAP: PKCS8 wrapped symmetric key. DECODE: Decoded plaintext.')
def select_mode(mode, input, output):
    """
    WRAP: Wrap symmetric key in a PKCS8 container.\n
    DECODE: Decodes a symmetric ciphertext wrapped in a PKCS8 container.
    """
    if mode == "wrap":
        wrap(input, output)
    elif mode == "decode":
        decrypt(input, output)


if __name__ == '__main__':
    select_mode()
