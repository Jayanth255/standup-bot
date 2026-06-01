import click
from datetime import datetime
from standup.storage import get_today_entry, save_entry, load_config


def run_log():
    now = datetime.now()
    config = load_config()
    name = config.get("name", "")

    greeting = f"Good morning{', ' + name if name else ''}! 👋"
    click.echo("")
    click.echo(click.style("━" * 50, fg="yellow"))
    click.echo(click.style(f"  🗓️  Daily Standup — {now.strftime('%A, %B %d %Y')}", fg="yellow", bold=True))
    click.echo(click.style(f"  {greeting}", fg="yellow"))
    click.echo(click.style("━" * 50, fg="yellow"))

    existing = get_today_entry()
    if existing:
        click.echo(click.style("\n⚠️  You've already logged today!", fg="yellow"))
        overwrite = click.prompt("Overwrite it?", type=click.Choice(["y", "n"]), default="n")
        if overwrite == "n":
            click.echo(click.style("No changes made. Have a great day! 👋\n", fg="dim"))
            return

    click.echo("\n" + click.style("Answer these 3 quick questions:\n", bold=True))

    click.echo(click.style("1️⃣  What did you work on yesterday?", fg="cyan", bold=True))
    yesterday = click.prompt(click.style("  →", fg="cyan"))

    click.echo(click.style("\n2️⃣  What will you work on today?", fg="cyan", bold=True))
    today = click.prompt(click.style("  →", fg="cyan"))

    click.echo(click.style("\n3️⃣  Any blockers?", fg="cyan", bold=True) + click.style(" (Enter to skip)", fg="white", dim=True))
    blockers = click.prompt(click.style("  →", fg="cyan"), default="None")

    entry = save_entry(yesterday, today, blockers)

    click.echo("")
    click.echo(click.style("━" * 50, fg="green"))
    click.echo(click.style(f"  ✅ Standup logged at {entry['time']}!", fg="green", bold=True))
    click.echo(click.style("━" * 50, fg="green"))
    click.echo(f"  {click.style('Yesterday:', bold=True)} {yesterday}")
    click.echo(f"  {click.style('Today:', bold=True)}     {today}")
    click.echo(f"  {click.style('Blockers:', bold=True)}  {blockers}")
    click.echo(click.style("━" * 50, fg="green"))
    click.echo(click.style("\n  Run 'standup view' to see all past entries.\n", dim=True))
