import click


@click.group()
def cli():
    """
    \b
    🗓️  Standup Bot — Daily standup logger for developers
    ──────────────────────────────────────────────────────
    Log your daily standups, view history, and get weekly
    summaries right from your terminal.
    """
    pass


@cli.command()
def log():
    """Log today's standup (yesterday, today, blockers)."""
    from standup.commands.log import run_log
    run_log()


@cli.command()
@click.option("--limit", default=7, help="Number of entries to show (default: 7)")
def view(limit):
    """View recent standup entries."""
    from standup.commands.view import run_view
    run_view(limit=limit)


@cli.command()
@click.option("--days", default=7, help="Number of days to summarize (default: 7)")
def summary(days):
    """Generate a summary of recent standups."""
    from standup.commands.summary import run_summary
    run_summary(days=days)


@cli.command("config")
@click.option("--show", is_flag=True, help="Show current config")
def config_cmd(show):
    """Set up your name and team preferences."""
    if show:
        from standup.commands.config import run_config_show
        run_config_show()
    else:
        from standup.commands.config import run_config
        run_config()


if __name__ == "__main__":
    cli()
