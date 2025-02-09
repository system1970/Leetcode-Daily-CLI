import click
import webbrowser
from leetdaily.leetcode_api import get_daily_problem
from rich.console import Console
from rich.text import Text
from rich.markdown import Markdown
import re
import html

def clean_html(html_content):
    """
    Convert HTML content into a format suitable for rendering with `rich`.

    This function processes HTML content by removing HTML tags, converting certain
    HTML elements to their text equivalents, and handling special cases like
    superscripts and subscripts.

    Args:
        html_content (str): The HTML content to be cleaned.

    Returns:
        str: The cleaned text, suitable for rendering with the `rich` library.
    """
    # Step 1: Unescape HTML entities (e.g., <, >, &nbsp;)
    clean_text = html.unescape(html_content)

    # Step 2: Replace <ul> and <li> with bullet points
    clean_text = re.sub(r'<ul>', '', clean_text)
    clean_text = re.sub(r'</ul>', '\n', clean_text)
    clean_text = re.sub(r'<li>', '• ', clean_text)
    clean_text = re.sub(r'</li>', '\n', clean_text)

    # Step 3: Convert <code> blocks into Markdown-style backticks
    clean_text = re.sub(r'<code>(.*?)</code>', lambda match: f'{match.group(1)}', clean_text)

    # Step 4: Handle <sup> and <sub> using Unicode superscripts/subscripts
    sup_map = {'1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '0': '⁰'}
    sub_map = {'1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉', '0': '₀'}

    def replace_sup(match):
        return ''.join(sup_map[char] for char in match.group(1))

    def replace_sub(match):
        return ''.join(sub_map[char] for char in match.group(1))

    clean_text = re.sub(r'<sup>(\d+)</sup>', replace_sup, clean_text)
    clean_text = re.sub(r'<sub>(\d+)</sub>', replace_sub, clean_text)

    # Step 5: Remove any remaining HTML tags
    clean_text = re.sub(r'<[^>]+>', '', clean_text)


    return clean_text


console = Console()

@click.group()
def cli():
    pass


@cli.command()
def daily():
    """Show today's LeetCode daily challenge."""
    try:
        problem = get_daily_problem()
        console.print(f"[bold green]Title:[/] {problem['question']['title']}")
        console.print(f"[bold green]Difficulty:[/] {problem['question']['difficulty']}")
        console.print(f"[bold green]Link:[/] https://leetcode.com{problem['link']}")

        # Display the problem description
        description = clean_html(problem['question']['content'])
        console.print("\n[bold green]Description:[/]")
        console.print(Markdown(description))  # Render as Markdown
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e}")

@cli.command()
def submit():
    """Open the daily problem in your web browser."""
    try:
        problem = get_daily_problem()
        problem_url = f"https://leetcode.com{problem['link']}"
        click.echo(f"Opening problem in browser: {problem_url}")
        webbrowser.open(problem_url)
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == "__main__":
    cli()
