import pandas as pd
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import os
from datetime import datetime

console = Console()

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        console.print("[green]CSV file loaded successfully.[/green]")
        return df
    except FileNotFoundError:
        console.print(f"[red]File not found:[/red] {file_path}")
        return None
    except Exception as e:
        console.print(f"[red]Error loading CSV:[/red] {e}")
        return None

def clean_data(df):
    original_shape = df.shape
    df_cleaned = df.drop_duplicates()
    df_cleaned = df_cleaned.dropna(how='all')  # remove fully empty rows
    cleaned_shape = df_cleaned.shape
    return df_cleaned, original_shape, cleaned_shape

def generate_report(df, original_shape, cleaned_shape):
    table = Table(title="CSV Data Report", box=box.SIMPLE)
    
    table.add_column("Metric", style="bold cyan")
    table.add_column("Value", style="bold yellow")

    table.add_row("Original Rows", str(original_shape[0]))
    table.add_row("Original Columns", str(original_shape[1]))
    table.add_row("Cleaned Rows", str(cleaned_shape[0]))
    table.add_row("Cleaned Columns", str(cleaned_shape[1]))
    table.add_row("Missing Values", str(df.isnull().sum().sum()))
    table.add_row("Duplicate Rows Removed", str(original_shape[0] - cleaned_shape[0]))
    table.add_row("Columns with Most Nulls", str(df.isnull().sum().idxmax()))
    table.add_row("Column with Most Unique", str(df.nunique().idxmax()))

    console.print(table)

    # Show sample data
    console.print(Panel(df.head().to_string(), title="Top 5 Rows", border_style="blue"))

def save_cleaned_file(df, original_path):
    base_name = os.path.basename(original_path)
    name, ext = os.path.splitext(base_name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"cleaned_{name}_{timestamp}.csv"
    df.to_csv(output_file, index=False)
    console.print(f"[bold green]Cleaned file saved as:[/bold green] {output_file}")

def main():
    console.print("[bold blue]=== CSV Cleaner & Reporter Tool ===[/bold blue]")
    file_path = console.input("Enter CSV file path (or drag-drop): ").strip()

    df = load_csv(file_path)
    if df is None:
        return

    df_cleaned, original_shape, cleaned_shape = clean_data(df)
    generate_report(df_cleaned, original_shape, cleaned_shape)
    save_cleaned_file(df_cleaned, file_path)

if __name__ == "__main__":
    main()


