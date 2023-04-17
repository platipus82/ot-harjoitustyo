from invoke import task

@task
def start(ctx):
    ctx.run("python src\\Flashcards.py", pty=False )                                       # pty=True doesnt work for windows

@task
def test(ctx): 
    #ctx.run("python src\\tests\\flashcards_test.py", pty=False )  
    ctx.run("pytest -s src", pty=False )  



@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest -s src", pty=False ) 

@task
def coverage_report(ctx):
    #ctx.run("coverage run --branch -m pytest -s src", pty=False ) 
    ctx.run("coverage report -m", pty=False )  
    ctx.run("coverage html", pty=False )  