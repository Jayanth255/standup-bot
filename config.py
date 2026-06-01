import click
from standup.storage import load_config, save_config


def run_config():
    config = load_config()
    click.echo(click.style("\n⚙️  Let's personalize your standup bot!\n", bold=True, fg="blue"))

    name = click.prompt("  Your name", default=config.get("name", ""))
    team = click.prompt("  Your team", default=config.get("team", ""))

    config["name"] = name
    config["team"] = team
    save_config(config)

    click.echo(click.style(f"\n✅ Config saved! Hello, {name} from team {team}!\n", fg="green"))


def run_config_show():
    config = load_config()
    if not config:
        click.echo(click.style("\n  No config set. Run 'standup config' to set it up.\n", fg="yellow"))
        return
    click.echo(click.style("\n⚙️  Current Config:\n", bold=True, fg="blue"))
    for k, v in config.items():
        click.echo(f"   {click.style(k + ':', bold=True)} {v}")
    click.echo()
