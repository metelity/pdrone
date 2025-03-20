from rich.console import Console
from rich.text import Text
from rich.panel import Panel

def print_banner():
    console = Console()

    banner_text = """
    
  _____  _____          
 |  __ \|  __ \          
 | |__) | |  | |_ __ ___  _ __   ___           
 |  ___/| |  | | '__/ _ \| '_ \ / _ \          
 | |    | |__| | | | (_) | | | |  __/          
 |_|    |_____/|_|  \___/|_| |_|\___|         

"""

    text = Text()
    for i, line in enumerate(banner_text.split("\n")):
        gradient_factor = i / 6  
        red = int(255 * (1 - gradient_factor))
        green = int(255 * gradient_factor)
        blue = int(255 * gradient_factor)
        color = f"\n#{red:02X}{green:02X}{blue:02X}"
        text.append(line + "\n", style=color)

    console.print(Panel(text, title="[bold red]Phone Drone Information", border_style="red"))
