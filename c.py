from rich import print
from rich.console import group
from rich.panel import Panel

@group()
def get_panels():
    yield Panel("Hello", style="on blue")
    yield Panel("World", style="on red")

print(Panel(get_panels()))


from rich.console import Console
from rich.syntax import Syntax

console = Console()
with open("c.py", "rt") as code_file:
    syntax = Syntax(code_file.read(), "python")
console.print(syntax)