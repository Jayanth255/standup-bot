import click
from datetime import datetime, timedelta
from standup.storage import load_entries


def run_summary(days: int = 7):
    entries = load_entries()

    if not entries:
        click.echo(click.style("\n  No entries found. Run 'standup log' first.\n", fg="yellow"))
        return

    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    recent = [e for e in entries if e["date"] >= cutoff]

    if not recent:
        click.echo(click.style(f"\n  No entries in the last {days} days.\n", fg="yellow"))
        return

    click.echo("")
    click.echo(click.style("━" * 50, fg="yellow"))
    click.echo(click.style(f"  📊 Weekly Summary  ({len(recent)} standups)", fg="yellow", bold=True))
    click.echo(click.style(f"  {recent[0]['date']} → {recent[-1]['date']}", fg="yellow"))
    click.echo(click.style("━" * 50, fg="yellow"))

    click.echo(click.style("\n✅ What got done:", fg="green", bold=True))
    for e in recent:
        click.echo(f"   {click.style(e['date'], fg='cyan')}: {e['yesterday']}")

    click.echo(click.style("\n📌 Planned work:", fg="blue", bold=True))
    for e in recent:
        click.echo(f"   {click.style(e['date'], fg='cyan')}: {e['today']}")

    blockers = [e for e in recent if e["blockers"].lower() not in ["none", "no", "n/a", "-", ""]]
    if blockers:
        click.echo(click.style("\n🚫 Blockers encountered:", fg="red", bold=True))
        for e in blockers:
            click.echo(f"   {click.style(e['date'], fg='cyan')}: {e['blockers']}")
    else:
        click.echo(click.style("\n🚀 No blockers this week!", fg="green", bold=True))

    click.echo("")
