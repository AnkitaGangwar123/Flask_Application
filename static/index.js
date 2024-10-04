// console.log("Column 1: ", parameters_col_1);
// console.log("Column 2: ", parameters_col_2);

// Function to populate the tables after file selection
document.getElementById('dbc_file').addEventListener('change', function(event) {
    if (event.target.files.length > 0) {

        // Clear previous content in the parameters table
        const parametersTableBody = document.getElementById('parameters_table_body');
        parametersTableBody.innerHTML = '';

        // Determine the length of the shorter column
        const parameter_row_count = parameters_col_1.length; 

        // Populate the parameters table with data from parameters_col_1 and parameters_col_2
        for (let i = 0; i < parameter_row_count; i++) {
            parametersTableBody.innerHTML += `
                <tr>
                    <td>${parameters_col_1[i]}</td>
                    <td></td> <!-- Placeholder for value -->
                    <td>${parameters_col_2[i]}</td>
                    <td></td> <!-- Placeholder for value -->
                </tr>
            `;
        }

        // Clear previous content in the cell_voltages table
        const cellVoltageTableBody = document.getElementById('cell_voltages_table_body');
        cellVoltageTableBody.innerHTML = '';

        // Determine the length of the shorter column
        const cv_row_count = cv_col_1.length;

        // Populate the cell_voltages table with data from cv_col_1 and cv_col_2
        for (let i = 0; i < cv_row_count; i++) {
            cellVoltageTableBody.innerHTML += `
                <tr>
                    <td>${cv_col_1[i]}</td>
                    <td></td> <!-- Placeholder for value -->
                    <td>${cv_col_2[i]}</td>
                    <td></td> <!-- Placeholder for value -->
                </tr>
            `;
        }

        // Clear previous content in the cell_temperatures table
        const cellTemperatureTableBody = document.getElementById('cell_temperatures_table_body');
        cellTemperatureTableBody.innerHTML = '';

        // Determine the length of the shorter column
        const ct_row_count = ct_col_1.length;

        // Populate the cell_temperatures table with data from ct_col_1
        for (let i = 0; i < ct_row_count; i++) {
            cellTemperatureTableBody.innerHTML += `
                <tr>
                    <td>${ct_col_1[i]}</td>
                    <td></td> <!-- Placeholder for value -->
                </tr>
            `;
        }

        // Clear previous content in the errors table
        const errorsTableBody = document.getElementById('errors_table_body');
        errorsTableBody.innerHTML = '';

        // Determine the length of the shorter column
        const error_row_count = errors_col_1.length;

        // Populate the errors table with data from errors_col_1 and ct_col_2
        for (let i = 0; i < error_row_count; i++) {
            errorsTableBody.innerHTML += `
                <tr>
                    <td>${errors_col_1[i]}</td>
                    <td>${errors_col_2[i]}</td>
                    <td>${errors_col_3[i]}</td>
                    <td>${errors_col_4[i]}</td>
                    <td>${errors_col_5[i]}</td>
                    <td>${errors_col_6[i]}</td>
                    <td>${errors_col_7[i]}</td>
                    <td>${errors_col_8[i]}</td>
                </tr>
            `;
        }
    }
});
