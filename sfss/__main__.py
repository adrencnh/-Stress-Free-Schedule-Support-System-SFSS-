from sfss import *
from sfss.courses_database_conversion import *

FLASK_PORT = 8081

app.run(debug=True, port=FLASK_PORT, host='0.0.0.0')