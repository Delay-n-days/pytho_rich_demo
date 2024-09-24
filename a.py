import logging
import os
import sys
import time
from typing import Tuple
import rich
from rich.logging import RichHandler
FORMAT = "%(message)s"
logging.basicConfig(level=logging.WARNING, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])
log = logging.getLogger("janim")
# 
from dataclasses import dataclass, asdict
log.setLevel("DEBUG")

def main():
    print("Hello from mytcp!")
    log.debug("qw")

main()


from rich.console import Console
console = rich.console.Console(color_system='truecolor')
console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
# console.print(locals())
console.print("FOO", style="white on blue")
console.print("FOO", style="white on green")
console.print_json('[false, true, null, "foo"]')

from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
    grade: str
@dataclass
class Point:
    x: int
    y: int
    student: Student

p = Point(1, 2,  Student("John", 20, "A"))

console.print(p)
# 转json
import json
p_dict = asdict(p)

json_p = json.dumps(p_dict)
a = [ 0x20,0x30]
console.print(a,width=20)
# 创建一个numpy数组
import numpy as np

a = np.array([1, 2, 3])
console.print(a)
# 二维数组
b = np.array([[1, 2, 3], [4, 5, 6]])
console.print(b)
# 三维数组
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
console.print(c)
# numpy 数组只能存数字么 ？ A: 是的，numpy数组只能存数字
# 但是可以存字符串
d = np.array(["Hello", "World"])
console.print(d)
# 对象呢
# 可以存对象，但是会被转成字符串
e = np.array([Student("John", 20, "A"), Student("Alice", 21, "B")])
console.print(e)
# 存对象有啥用啊
console.rule("[bold red]Chapter 2")

console.print_json(json_p)
# print(json_p)
# console.out("Locals", locals())
console = Console(width=20)

style = "bold white on blue"
# with console.status("Monkeying around..."):
#     console.print("Rich", style=style)
#     time.sleep(0.3)
#     console.print("Rich", style=style, justify="left")
#     time.sleep(0.3)
#     console.print("Rich", style=style, justify="center")
#     time.sleep(0.3)
#     console.print("Rich", style=style, justify="right")
#     time.sleep(0.3)


supercali = "supercalifragilisticexpialidocious"

from rich.console import Console, OverflowMethod
from typing import List
overflow_methods: List[OverflowMethod] = ["fold", "crop", "ellipsis"]
for overflow in overflow_methods:
    console.rule(overflow)
    console.print(supercali, overflow=overflow, style="bold blue")
    console.print()
blue_console = Console(style="white on blue")
blue_console.print("I'm blue. Da ba dee da ba di.")

# console.input("What is [i]your[/i] [bold red]name[/]? :smiley: ")


from rich.tree import Tree
tree = Tree("Rich Tree")
tree.add("foo")
tree.add("bar")
console.print(tree)

from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)

import time

from rich.live import Live
from rich.table import Table

table = Table()
table.add_column("Row ID")
table.add_column("Description")
table.add_column("Level")

# with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
#     for row in range(3):
#         time.sleep(0.4)  # arbitrary delay
#         # update the renderable internally
#         table.add_row(f"{row}", f"description {row}", "[red]ERROR")

import random
def generate_table() -> Table:
    """Make a new table."""
    table = Table()
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    for row in range(random.randint(2, 6)):
        value = random.random() * 100
        table.add_row(
            f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
        )
    return table


# with Live(generate_table(), refresh_per_second=4) as live:
#     for _ in range(3):
#         time.sleep(0.4)
#         live.update(generate_table())

from rich import print
from rich.layout import Layout

layout = Layout()
layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)
print(layout)
time.sleep(1)
layout['upper'].update("Hello, [bold magenta]upper[/bold magenta]!")

import time
from rich.progress import track

# for i in track(range(20), description="Processing..."):
#     time.sleep(1)  # Simulate work being done

from rich.progress import Progress

# with Progress() as progress:

#     task1 = progress.add_task("[red]Downloading...", total=1000)
#     task2 = progress.add_task("[green]Processing...", total=1000)
#     task3 = progress.add_task("[cyan]Cooking...", total=1000)

#     while not progress.finished:
#         progress.update(task1, advance=0.5)
#         progress.update(task2, advance=0.3)
#         progress.update(task3, advance=0.9)
#         time.sleep(0.02)

from rich.panel import Panel
print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))

MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""
from rich.console import Console
from rich.markdown import Markdown

console = Console()
md = Markdown(MARKDOWN)
console.print(md)
from rich import print
from rich.padding import Padding
test = Padding("Hello", (2, 4))
print(test)


from rich import print
from rich.columns import Columns


directory = os.listdir("./")
columns = Columns(directory, equal=True, expand=True)
print(columns)

# from rich.prompt import Prompt
# name = Prompt.ask("Enter your name", default="Paul Atreides")
# # from rich.prompt import Prompt
# name = Prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul")
# from rich.prompt import Confirm
# is_rich_great = Confirm.ask("Do you like rich?")
# assert is_rich_great


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
    syntax = Syntax(code_file.read(), "python", line_numbers=True)
console.print(syntax)

from rich.pretty import pprint
pprint({"foo": "bar"})

pprint(json_p)


from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme

class EmailHighlighter(RegexHighlighter):
    """Apply style to anything that looks like an email."""

    base_style = "example."
    highlights = [r"(?P<email>[\w-]+@([\w-]+\.)+[\w-]+)"]


theme = Theme({"example.email": "bold magenta"})
console = Console(highlighter=EmailHighlighter(), theme=theme)
console.print("Send funds to money@example.org")


from random import randint

from rich import print
from rich.highlighter import Highlighter


class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(f"color({randint(16, 255)})", index, index + 1)


rainbow = RainbowHighlighter()
print(rainbow("I must not fear. Fear is the mind-killer."))