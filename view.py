import click
from standup.storage import load_entries


def run_view(limit: int = 7):
    entries = load_entries()

    if not entries:
        click.echo(click.style("\n  No standup entries yet!", fg="yellow"))
        click.echo(click.style("  Run 'standup log' to add your first entry.\n", dim=True))
        return

    recent = list(reversed(entries))[:limit]
    click.echo(click.style(f"\n📋 Last {len(recent)} standup entries:\n", bold=True))

    for entry in recent:
        is_blocked = entry["blockers"].lower() not in ["none", "no", "n/a", "-", ""]
        blocker_color = "red" if is_blocked else "green"
        blocker_icon = "🚫" if is_blocked else "✅"

        click.echo(click.style("┌" + "─" * 48 + "┐", fg="cyan"))
        click.echo(click.style(f"│  {entry['day']}, {entry['date']}  @{entry['time']}", fg="cyan", bold=True))
        click.echo(click.style("├" + "─" * 48 + "┤", fg="cyan"))
        click.echo(f"│  {click.style('Yesterday:', bold=True)} {entry['yesterday']}")
        click.echo(f"│  {click.style('Today:', bold=True)}     {entry['today']}")
        click.echo(f"│  {click.style('Blockers:', bold=True)}  " + click.style(f"{blocker_icon} {entry['blockers']}", fg=blocker_color))
        click.echo(click.style("└" + "─" * 48 + "┘", fg="cyan"))
        click.echo()

    if len(entries) > limit:
        click.echo(click.style(f"  Showing {limit} of {len(entries)} entries. Use --limit N to see more.\n", dim=True))
