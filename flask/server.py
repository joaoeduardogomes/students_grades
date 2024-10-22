from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from dataframes import get_students_status, get_highest_grade, get_lowest_grade, get_average_grade, passed_students_count,  failed_students_count
from plots import plot_pie_chart, plot_histogram

app = Flask(__name__)
Bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("index.html", error="No file selected")
        file = request.files["file"]

        if file.filename == "":
            return render_template("index.html", error="No file selected")

        if file:
            if not file.filename.endswith(".csv"):
                return render_template("index.html", error="Only CSV files are allowed")
            try:
                file.save("static/docs/students_scores.csv")
                return redirect(url_for('result'))
            except Exception:
                return render_template("index.html", error="Error uploading file")
    return render_template("index.html")


@app.route("/result")
def result():
    #* The pandas data:
    df = get_students_status()
    table_html = df.to_html(index=False, classes="table table-striped table-bordered rounded")

    passed_students_num = passed_students_count()
    failed_students_num = failed_students_count()
    average_grade = get_average_grade()
    highest_grade = get_highest_grade()
    lowest_grade = get_lowest_grade()

    #* The matplotlib data:
    pie_chart_path = plot_pie_chart()
    histogram_path = plot_histogram()

    return render_template("result.html", table=table_html, passed_students_num=passed_students_num, failed_students_num=failed_students_num, average_grade=average_grade, highest_grade=highest_grade, lowest_grade=lowest_grade, pie_chart=pie_chart_path, histogram=histogram_path)

@app.route("/download")
def download_file():
    return send_from_directory("static/output", "students_result.csv", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)