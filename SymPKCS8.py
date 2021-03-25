import click
from wrapper.wrap import wrap
from decrypt.decrypt import decrypt


class OptionRequiredIf(click.Option):
    def full_process_value(self, ctx, value):
        value = super(OptionRequiredIf, self).full_process_value(ctx, value)

        if value is None and ctx.params['mode'] == 'decode':
            msg = 'Required with decode mode'
            raise click.MissingParameter(ctx=ctx, param=self, message=msg)
        return value


@click.command()
@click.argument('mode',
                type=click.Choice(['wrap', 'decode'], case_sensitive=False))
@click.option('--keyfile', type=click.File('r'), required=True,
              help='The symmetric key to wrap or decode (PKCS8 required for decode).')
@click.option('--ciphertext', type=click.File('rb'), cls=OptionRequiredIf,
              help='The ciphertext to decode.  [required for decode]')
@click.option('--out', required=True,
              help='The PKCS8 wrapped key or the decoded plaintext.')
def select_mode(mode, keyfile, ciphertext, out):
    """
    WRAP: Wrap symmetric key in a PKCS8 container.\n
    DECODE: Decodes a symmetric ciphertext wrapped in a PKCS8 container.
    """
    if mode == "wrap":
        pem_key = wrap(keyfile)
        with open(out, "w") as out_file:
            out_file.writelines(pem_key)
        print("Key correctly wrapped in " + out)
    elif mode == "decode":
        plaintext = decrypt(keyfile, ciphertext.read())
        with open(out, "wb") as out_file:
            out_file.write(plaintext)
        print("Plaintext decrypted in " + out)


if __name__ == '__main__':
    select_mode()
