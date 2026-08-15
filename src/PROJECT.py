from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "cell_culture_secret_key"

# Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Enter your MySQL password here if set
app.config['MYSQL_DB'] = 'CellCultureDB'

mysql = MySQL(app)

# ==============================================================================
# 1. RESEARCHERS (RESEARCHER)
# ==============================================================================
@app.route('/')
@app.route('/researchers')
def researchers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT ResearcherID, FirstName, LastName, EmailAddress, OfficePhone FROM RESEARCHER")
    researchers_data = cur.fetchall()
    cur.close()
    return render_template('researchers.html', researchers=researchers_data)

@app.route('/researcher/insert', methods=['POST'])
def researcher_insert():
    if request.method == "POST":
        researcher_id = request.form['ResearcherID']
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        email = request.form['EmailAddress']
        phone = request.form['OfficePhone']

        cur = mysql.connection.cursor()

        # Check if ResearcherID already exists
        cur.execute("SELECT ResearcherID FROM RESEARCHER WHERE ResearcherID = %s", (researcher_id,))
        existing_record = cur.fetchone()

        if existing_record:
            flash(f"Error: Researcher ID {researcher_id} already exists. Please choose a different ID.", "danger")
            cur.close()
            return redirect(url_for('researchers'))

        cur.execute(
            "INSERT INTO RESEARCHER (ResearcherID, FirstName, LastName, EmailAddress, OfficePhone) VALUES (%s, %s, %s, %s, %s)",
            (researcher_id, first_name, last_name, email, phone)
        )
        mysql.connection.commit()
        cur.close()
        flash("Researcher Registered Successfully", "success")
        return redirect(url_for('researchers'))

@app.route('/researcher/update', methods=['POST'])
def researcher_update():
    if request.method == 'POST':
        researcher_id = request.form['ResearcherID']
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        email = request.form['EmailAddress']
        phone = request.form['OfficePhone']

        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE RESEARCHER SET FirstName=%s, LastName=%s, EmailAddress=%s, OfficePhone=%s WHERE ResearcherID=%s",
            (first_name, last_name, email, phone, researcher_id)
        )
        mysql.connection.commit()
        cur.close()
        flash("Researcher Updated Successfully", "success")
        return redirect(url_for('researchers'))

@app.route('/researcher/delete/<int:researcher_id>', methods=['GET'])
def researcher_delete(researcher_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM RESEARCHER WHERE ResearcherID=%s", (researcher_id,))
    mysql.connection.commit()
    cur.close()
    flash("Researcher Deleted Successfully", "success")
    return redirect(url_for('researchers'))


# ==============================================================================
# 2. CELL LINES (CELL_LINE)
# ==============================================================================
@app.route('/cell_lines')
def cell_lines():
    cur = mysql.connection.cursor()
    cur.execute("SELECT CellLineID, LineName, Organism, TissueOrigin, BiosafetyLevel FROM CELL_LINE")
    lines_data = cur.fetchall()
    cur.close()
    return render_template('cell_lines.html', cell_lines=lines_data)

@app.route('/cell_line/insert', methods=['POST'])
def cell_line_insert():
    if request.method == "POST":
        line_id = request.form['CellLineID']
        line_name = request.form['LineName']
        organism = request.form['Organism']
        tissue = request.form['TissueOrigin']
        bsl = request.form['BiosafetyLevel']

        cur = mysql.connection.cursor()

        # Check if CellLineID already exists
        cur.execute("SELECT CellLineID FROM CELL_LINE WHERE CellLineID = %s", (line_id,))
        existing_record = cur.fetchone()

        if existing_record:
            flash(f"Error: Cell Line ID {line_id} already exists. Please enter a unique ID.", "danger")
            cur.close()
            return redirect(url_for('cell_lines'))

        cur.execute(
            "INSERT INTO CELL_LINE (CellLineID, LineName, Organism, TissueOrigin, BiosafetyLevel) VALUES (%s, %s, %s, %s, %s)",
            (line_id, line_name, organism, tissue, bsl)
        )
        mysql.connection.commit()
        cur.close()
        flash("Cell Line Added Successfully", "success")
        return redirect(url_for('cell_lines'))

@app.route('/cell_line/update', methods=['POST'])
def cell_line_update():
    if request.method == 'POST':
        line_id = request.form['CellLineID']
        line_name = request.form['LineName']
        organism = request.form['Organism']
        tissue = request.form['TissueOrigin']
        bsl = request.form['BiosafetyLevel']

        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE CELL_LINE SET LineName=%s, Organism=%s, TissueOrigin=%s, BiosafetyLevel=%s WHERE CellLineID=%s",
            (line_name, organism, tissue, bsl, line_id)
        )
        mysql.connection.commit()
        cur.close()
        flash("Cell Line Updated Successfully", "success")
        return redirect(url_for('cell_lines'))

@app.route('/cell_line/delete/<int:line_id>', methods=['GET'])
def cell_line_delete(line_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM CELL_LINE WHERE CellLineID=%s", (line_id,))
    mysql.connection.commit()
    cur.close()
    flash("Cell Line Deleted Successfully", "success")
    return redirect(url_for('cell_lines'))


# ==============================================================================
# 3. EXPERIMENTS (EXPERIMENT)
# ==============================================================================
@app.route('/experiments')
def experiments():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT E.ExperimentID, E.Title, E.StartDate, E.Status, E.CellLineID, C.LineName
        FROM EXPERIMENT E
        LEFT JOIN CELL_LINE C ON E.CellLineID = C.CellLineID
    """)
    experiment_data = cur.fetchall()

    cur.execute("SELECT CellLineID, LineName FROM CELL_LINE")
    cell_line_options = cur.fetchall()
    cur.close()

    return render_template('experiments.html', experiments=experiment_data, cell_lines=cell_line_options)

@app.route('/experiment/insert', methods=['POST'])
def experiment_insert():
    if request.method == "POST":
        exp_id = request.form['ExperimentID']
        title = request.form['Title']
        start_date = request.form['StartDate']
        status = request.form['Status']
        cell_line_id = request.form['CellLineID']

        cur = mysql.connection.cursor()

        # Check if ExperimentID already exists
        cur.execute("SELECT ExperimentID FROM EXPERIMENT WHERE ExperimentID = %s", (exp_id,))
        existing_record = cur.fetchone()

        if existing_record:
            flash(f"Error: Experiment ID {exp_id} already exists. Please use a unique ID.", "danger")
            cur.close()
            return redirect(url_for('experiments'))

        cur.execute(
            "INSERT INTO EXPERIMENT (ExperimentID, Title, StartDate, Status, CellLineID) VALUES (%s, %s, %s, %s, %s)",
            (exp_id, title, start_date, status, cell_line_id)
        )
        mysql.connection.commit()
        cur.close()
        flash("Experiment Created Successfully", "success")
        return redirect(url_for('experiments'))

@app.route('/experiment/update', methods=['POST'])
def experiment_update():
    if request.method == 'POST':
        exp_id = request.form['ExperimentID']
        title = request.form['Title']
        start_date = request.form['StartDate']
        status = request.form['Status']
        cell_line_id = request.form['CellLineID']

        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE EXPERIMENT SET Title=%s, StartDate=%s, Status=%s, CellLineID=%s WHERE ExperimentID=%s",
            (title, start_date, status, cell_line_id, exp_id)
        )
        mysql.connection.commit()
        cur.close()
        flash("Experiment Updated Successfully", "success")
        return redirect(url_for('experiments'))

@app.route('/experiment/delete/<int:exp_id>', methods=['GET'])
def experiment_delete(exp_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM EXPERIMENT WHERE ExperimentID=%s", (exp_id,))
    mysql.connection.commit()
    cur.close()
    flash("Experiment Deleted Successfully", "success")
    return redirect(url_for('experiments'))


# ==============================================================================
# 4. CRYOSTOCKS (CRYOSTOCK)
# ==============================================================================
@app.route('/cryostocks')
def cryostocks():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT CS.StockID, CS.VialCount, CS.FreezerLocation, CS.FreezeDate, CS.CellLineID, C.LineName
        FROM CRYOSTOCK CS
        LEFT JOIN CELL_LINE C ON CS.CellLineID = C.CellLineID
    """)
    cryostock_data = cur.fetchall()

    cur.execute("SELECT CellLineID, LineName FROM CELL_LINE")
    cell_line_options = cur.fetchall()
    cur.close()

    return render_template('cryostocks.html', cryostocks=cryostock_data, cell_lines=cell_line_options)

@app.route('/cryostock/insert', methods=['POST'])
def cryostock_insert():
    if request.method == "POST":
        stock_id = request.form['StockID']
        vial_count = request.form['VialCount']
        location = request.form['FreezerLocation']
        freeze_date = request.form['FreezeDate']
        cell_line_id = request.form['CellLineID']

        cur = mysql.connection.cursor()

        # Check if StockID already exists
        cur.execute("SELECT StockID FROM CRYOSTOCK WHERE StockID = %s", (stock_id,))
        existing_record = cur.fetchone()

        if existing_record:
            flash(f"Error: Stock ID {stock_id} already exists. Please choose another ID.", "danger")
            cur.close()
            return redirect(url_for('cryostocks'))

        try:
            cur.execute(
                "INSERT INTO CRYOSTOCK (StockID, VialCount, FreezerLocation, FreezeDate, CellLineID) VALUES (%s, %s, %s, %s, %s)",
                (stock_id, vial_count, location, freeze_date, cell_line_id)
            )
            mysql.connection.commit()
            flash("Cryostock Sample Registered Successfully", "success")
        except Exception as e:
            flash(f"Database Error: {str(e)}", "danger")
        finally:
            cur.close()

        return redirect(url_for('cryostocks'))

@app.route('/cryostock/update', methods=['POST'])
def cryostock_update():
    if request.method == 'POST':
        stock_id = request.form['StockID']
        vial_count = request.form['VialCount']
        location = request.form['FreezerLocation']
        freeze_date = request.form['FreezeDate']
        cell_line_id = request.form['CellLineID']

        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE CRYOSTOCK SET VialCount=%s, FreezerLocation=%s, FreezeDate=%s, CellLineID=%s WHERE StockID=%s",
            (vial_count, location, freeze_date, cell_line_id, stock_id)
        )
        mysql.connection.commit()
        cur.close()
        flash("Cryostock Record Updated Successfully", "success")
        return redirect(url_for('cryostocks'))

@app.route('/cryostock/delete/<int:stock_id>', methods=['GET'])
def cryostock_delete(stock_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM CRYOSTOCK WHERE StockID=%s", (stock_id,))
    mysql.connection.commit()
    cur.close()
    flash("Cryostock Record Deleted Successfully", "success")
    return redirect(url_for('cryostocks'))


if __name__ == '__main__':
    app.run(debug=True)