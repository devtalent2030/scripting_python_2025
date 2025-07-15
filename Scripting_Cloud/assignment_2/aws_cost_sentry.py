# INPUT STAGE
import argparse           # Get CLI arguments like --file
import os                 # File path checks
import pandas as pd       # Load AWS CSV

# PROCESS STAGE
import math               # Optional: for rounding %
import datetime           # Optional: for date parsing/formatting

# OUTPUT STAGE
from rich.console import Console   # For pretty printing
from rich.table import Table       # For output tables
import smtplib            # To send emails
import ssl                # Secure email transport
from email.mime.text import MIMEText  # Format email body



print(dir(argparse))