from flask import Flask, request, session, redirect, render_template, url_for
from flask import current_app as app

from application.read_can import pack_can_data

@app.route("/", methods=["GET","POST"])
def landing_page():

    baudrate = session.get('baudrate', 500000)

    if request.method == "POST":
        # Get and validate baudrate from the form
        selected_baudrate = request.form.get("baudrate")
        try:
            baudrate = int(selected_baudrate)
            session['baudrate'] = baudrate
        except ValueError:
            baudrate = 500000  # Fallback to default
            session['baudrate'] = baudrate


    if request.method == "GET":

        filepath = "MLRPhase2_DBC_06.dbc"

        can_bus = pack_can_data(baudrate)
        can_bus.database_file(filepath)

        parameters_col_1 = can_bus.parameters[0:8]
        parameters_col_2 = can_bus.parameters[8:16]
        cv_col_1 = can_bus.cell_voltages[0:8]
        cv_col_2 = can_bus.cell_voltages[8:16]
        ct_col_1 = can_bus.cell_temperatures[0:8]
        errors_col_1 = can_bus.errors_events[0:8]
        errors_col_2 = can_bus.errors_events[8:16]
        errors_col_3 = can_bus.errors_events[16:24]
        errors_col_4 = can_bus.errors_events[24:32]
        errors_col_5 = can_bus.errors_events[32:40]
        errors_col_6 = can_bus.errors_events[40:48]
        errors_col_7 = can_bus.errors_events[48:56]
        errors_col_8 = can_bus.errors_events[56:64]
        data_dict = ""

        return render_template("index.html", parameters_col_1 = parameters_col_1, parameters_col_2 = parameters_col_2, cv_col_1 = cv_col_1, cv_col_2 = cv_col_2, ct_col_1 = ct_col_1, 
                                errors_col_1 = errors_col_1, errors_col_2 = errors_col_2, errors_col_3 = errors_col_3, errors_col_4 = errors_col_4,
                                errors_col_5 = errors_col_5, errors_col_6 = errors_col_6, errors_col_7 = errors_col_7, errors_col_8 = errors_col_8, data_dict = data_dict)

     
