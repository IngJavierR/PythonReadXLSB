from pyxlsb import open_workbook
from flask import Flask, Response, json, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def createResponse(data, http_status):
    return Response(
        response=json.dumps(data),
        status=http_status,
        mimetype='application/json')

@app.route('/rows', methods=['POST'])
def getRows():
    body = json.loads(request.data)
    fileName = body['fileName']
    sheet = body['sheet']
    cells = body['cells']
    return createResponse(readxslb(fileName, sheet, cells), 200)

def readxslb(fileName, sheet, cells):
    columnsRow = []
    response = []
    with open_workbook(fileName) as wb:
        with wb.get_sheet(sheet) as sheet:
            for row in sheet.rows():
                for r in row:
                    cellRow = {
                        "row": r.r,
                        "column": r.c,
                        "value": r.v
                    }
                    columnsRow.append(cellRow)
            for cell in cells:
                print(cell)
                findCell = list(filter(lambda cellRow: (cellRow['row'] == cell['row'] and cellRow['column'] == cell['column']), columnsRow))
                response.append(findCell[0])
    return response
                

def __main__():
    print('Start Service')
    app.run(host= '0.0.0.0')

__main__()