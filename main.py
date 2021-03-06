import markdown
from pygments.formatters import HtmlFormatter
from flask import Flask, render_template, redirect
app = Flask('app')


@app.route('/')
def hello_world():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"])
    # Generate Css for syntax highlighting
    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"

    md_template = md_css_string + md_template_string

    return md_template_string


@app.route('/doom')
def doom():
    return render_template('doom.html')


@app.route('/doom2')
def doom2():
    return render_template('doom2.html')


@app.route('/mortalKombat')
def mortalKombat():
    return render_template('mortalKombat.html')


@app.route('/quake')
def quake():
    return render_template('quake.html')


@app.route('/wolfenstein')
def Wolf3D():
    return render_template('wolfenstein.html')


@app.route('/v86')
def v86():
    return render_template('v86.html')


@app.errorhandler(404)
def page_not_found(e):
    print("user trying to connect to nonexistent page, redirecting")
    return redirect("https://dospy-2.legionnorth.repl.co/", code=404)


app.run(host='0.0.0.0', port=8080, debug=True)
