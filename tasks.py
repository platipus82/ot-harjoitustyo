from invoke import task
import os
@task
def start(ctx):
    #ctx.run("python src\\flashcards.py", pty=False )                                       # pty=True doesnt work for windows
    pth = "src\\flashcards.py"
    if not os.path.isfile(pth):
        pth = "src/flashcards.py"
    cmnd = "python " + pth
    ctx.run(cmnd, pty=False)

@task
def test(ctx): 
    #ctx.run("python src\\tests\\flashcards_test.py", pty=False )  
    ctx.run("pytest -s src", pty=False )  

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest -s src", pty=False) 

@task
def coverage_report(ctx):
    #ctx.run("coverage run --branch -m pytest -s src", pty=False) 
    ctx.run("coverage run --branch -m pytest -s src", pty=False) 
    ctx.run("coverage report -m", pty=False)  
    ctx.run("coverage html", pty=False)  

@task
def lint(ctx):
    ctx.run("pylint src", pty=False)