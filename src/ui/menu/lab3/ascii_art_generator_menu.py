"""
Module docstring for ui.menu.lab3.ascii_art_generator_menu

Module for implementing a simple menu for an ASCII art generator.

This module contains the `AsciiArtGeneratorMenu` class, providing a menu for an ASCII art generator.
Users can run the program to generate ASCII art based on the provided text.

Example:
```python
ascii_art_menu = AsciiArtGeneratorMenu()
ascii_art_menu.run()
"""
from service.lab3.ascii_art_generator_service import AsciiArtGeneratorService
from ui.menu_builder import Menu


class AsciiArtGeneratorMenu(Menu):
    """A simple menu for an ASCII art generator."""

    def run(self):
        """Run the ASCII art generator program."""
        ascii_art_generator_service = AsciiArtGeneratorService()
        ascii_art_generator_service.display_text()
