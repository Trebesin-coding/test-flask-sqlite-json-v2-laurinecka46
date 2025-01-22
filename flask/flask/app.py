# Z následujících si vyber kód a sestav funkční flask aplikaci (není třeba použít vše, vyber si pouze ty části kódu, které potřebuješ)
# Kód je funkční, pouze místo dotazníků je potřeba doplnit podle potřeby


app = Flask(__name__)
from flask import Flask, render_template, request, redirect, url_for

# Hodnocení: import je vždy první řádek kódu, nemůžete vytvořit flaskovou aplikaci a až poté importovat


@app.route("/")
def vitej():
    return render_template("vitej.html")


@app.route("/form")
def form():
    odpoved = request.args.get(
        "form.html"
    )  # údaj získáváte podle atributu name z formuláře, ne podle názvu souboru
    if odpoved == "nic":
        return render_template(
            "form.html", jinja="uživatel byl příliš líný na napsání recenze"
        )
    else:
        return render_template("form.html", jinja=odpoved)


if __name__ == "__main__":
    app.run(debug=True)
