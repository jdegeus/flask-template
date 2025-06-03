from flask import Flask, render_template, request, send_file, redirect, url_for
import pandas as pd
import io

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file:
        return redirect(url_for("home"))

    # Read the uploaded Excel file into a DataFrame
    df = pd.read_excel(file)

    # Example processing: add a new column with row numbers
    df["RowNumber"] = range(1, len(df) + 1)

    # Save the processed DataFrame to a new Excel file in memory
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False)
    output.seek(0)

    # Send the processed file back to the user
    return send_file(
        output,
        as_attachment=True,
        download_name="processed.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

@app.route("/shutdown", methods=["POST"])
def shutdown():
    shutdown_func = request.environ.get("werkzeug.server.shutdown")
    if shutdown_func is not None:
        shutdown_func()
        return "Server shutting down..."
    else:
        import os
        os._exit(0)
        return "Forced exit."

if __name__ == "__main__":
    import webbrowser
    from threading import Timer

    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000/")

    Timer(1, open_browser).start()
    app.run()