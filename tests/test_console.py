#!/usr/bin/python3
"""Module for testing the HBNBCommand Class"""
import unittest
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Test case class for testing the HBNBCommand Console."""

    def test_help(self):
        """Tests the help command."""
        with self.assertLogs() as log:
            HBNBCommand().onecmd("help")
        expected_output = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update\n
"""
        self.assertEqual(expected_output, log.output[0])

    def test_do_quit(self):
        """Tests the quit command."""
        with self.assertLogs() as log:
            HBNBCommand().onecmd("quit")
        self.assertEqual([], log.output)

        with self.assertLogs() as log:
            HBNBCommand().onecmd("quit garbage")
        self.assertEqual([], log.output)

    def test_do_EOF(self):
        """Tests the EOF command."""
        with self.assertLogs() as log:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(['\n'], log.output)

        with self.assertLogs() as log:
            HBNBCommand().onecmd("EOF garbage")
        self.assertEqual(['\n'], log.output)

    def test_do_emptyline(self):
        """Tests the emptyline command."""
        with self.assertLogs() as log:
            HBNBCommand().onecmd("\n")
        self.assertEqual([], log.output)

        with self.assertLogs() as log:
            HBNBCommand().onecmd("                     \n")
        self.assertEqual([], log.output)

    def test_do_all(self):
        """Tests the do_all command."""
        with self.assertLogs() as log:
            HBNBCommand().onecmd("all")

if __name__ == "__main__":
    unittest.main()
