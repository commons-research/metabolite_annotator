import click

import click

@click.command()
@click.argument('text')
def main(text):
    print(text)

if __name__ == '__main__':
    main()