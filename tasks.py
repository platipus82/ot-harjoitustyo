from invoke import task

@task
def start(ctx):
    ctx.run("python src\\flashcards.py", pty=False )  # pty=True doesnt work for windows

@task
def test(ctx): 
    ctx.run("python src\tests\flashcards_test.py", pty=False )  # pty=True doesnt work for windows

@task
def coverage_report(ctx):
    ctx.run("coverage report -m", pty=False )  # pty=True doesnt work for windows
    ctx.run("coverage html", pty=False )  # pty=True doesnt work for windows