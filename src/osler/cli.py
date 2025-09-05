import typer
import subprocess

app = typer.Typer(
    name="osler",
    help="osler CLI: Initialize Tuva Health Demo in DuckDB",
    add_completion=False,
    rich_markup_mode="markdown",
)

@app.command()
def init(project_name: str):
      """Run dbt build on Tuva Health Demo in DuckDB"""
      typer.echo(f"Initializing project: {project_name}")

      try:
          result = subprocess.run(["dbt", "build"], 
                                  cwd="tuva-health-demo",
                                  check=True,
                                  text=True)
          typer.echo("✅ dbt build completed successfully")
          typer.echo(result.stdout)
      except subprocess.CalledProcessError as e:
          typer.echo(f"❌ dbt build failed with exit code {e.returncode}")
          typer.echo(e.stderr)
          raise typer.Exit(1)
      except FileNotFoundError:
          typer.echo("❌ dbt command not found. Please ensure dbt is installed.")
          raise typer.Exit(1)

if __name__ == "__main__":
    app()