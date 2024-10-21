from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from dataframes import get_students_status, get_highest_grade, get_lowest_grade, get_average_grade, passed_students, passed_students_count, failed_students, failed_students_count

app = Flask(__name__)
Bootstrap = Bootstrap5(app)

@app.route("/")
def index():
    df = get_students_status()
    table_html = df.to_html(index=False, classes="table table-striped table-bordered rounded")

    passed_students_table = passed_students()
    failed_students_table = failed_students()
    passed_students_num = passed_students_count()
    failed_students_num = failed_students_count()
    average_grade = get_average_grade()
    highest_grade = get_highest_grade()
    lowest_grade = get_lowest_grade()


    return render_template("index.html", table=table_html, passed_students=passed_students_table, failed_students=failed_students_table, passed_students_num=passed_students_num, failed_students_num=failed_students_num, average_grade=average_grade, highest_grade=highest_grade, lowest_grade=lowest_grade)


if __name__ == "__main__":
    app.run(debug=True)