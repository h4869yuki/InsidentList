from flask import Flask, render_template, make_response, jsonify
from flask import request
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from werkzeug.utils import redirect
from models.read_csv import withdraw
from models.read_csv import table_count

# インスタンスの生成
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/top')

@app.route('/top')
def show_top():
    d_records = withdraw()
    df_db_count =  table_count()
    
    return render_template('index.html', d_records=d_records, df_db_count=df_db_count)
	
# @app.route('/top', methods=['POST'])
# def post():
#     name = request.form['name']
#     return render_template('index.html')
#     print(name)
# post()

@app.route('/graph1.png')
def graph1():
    # データからグラフをプロットする
    plt.rcParams["font.family"] = "MS Gothic"
    x = ['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月'] 
    y = [10, 14, 17, 9, 11, 3, 5, 17, 21, 16, 18, 12] 
    fig, ax = plt.subplots()
    ax.bar(x, y, width=0.8) 
    plt.title("Infrastructure",)
    
    # canvasにプロットした画像を出力
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()
    # HTML側に渡すレスポンスを生成する
    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)
    return response

if __name__ == "__main__":
    app.run(debug=True)