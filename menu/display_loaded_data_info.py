# -*- coding: utf-8 -*-
"""
Created on Mon May  1 13:58:31 2023

@author: Marc
"""

from rich import print as rprint
from rich.panel import Panel

# =============================================================================
# Using rich library panel to make beautiful layout for our mainscript, 
# to show which data was loaded and how corrupted data is handled
# =============================================================================

def display_loaded_data_info(filename, corrupted_data_method):
    print()
    info_text = f"The file [bold cyan]{filename}[/bold cyan] has been loaded.\nCorrupted data has been handled using [bold cyan]{corrupted_data_method}[/bold cyan] method."
    panel = Panel(info_text, title="Data Loaded", expand=False, border_style="green")
    
    # Using rprint, to utilize another way of using color
    rprint(panel)