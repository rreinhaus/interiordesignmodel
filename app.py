from flask import Flask,render_template, request

import pickle

modern = """
Modern design is an interior design style characterized
by a monochromatic color palette, clean lines, minimalism, natural materials, and natural light. 
It refers specifically to a historical aesthetic movement that took place during the early to mid-twentieth century.
The 5 key elements are - clean lines, minimal home decor, neutral colors, open floor plan and low and long furniture."""
contemporary = """
Fundamentally, a contemporary style of decorating is defined by simplicity, subtle sophistication, deliberate use of texture, and clean lines.
Interiors tend to showcase space rather than things."""
rustic = """
Rustic interiors are defined by ruggedness and letting natural beauty shine.
The focus is to create a relaxing atmosphere by highlighting the use of wood, stone, leaves, and other organic elements. Rather than worry about perfect lines, rustic allows the character of each piece to stand out. 
From knots in the wood to rust on metal, this style celebrates character in a big way.
The entire goal of rustic interior styles is to be as natural as possible.
"""
minimal = """
Minimalist interior design is very similar to modern interior design and involves using the bare essentials to create a simple and uncluttered space. 
It’s characterised by simplicity, clean lines, and a monochromatic palette with colour used as an accent. 
It usually combines an open floor plan, lots of light, and functional furniture, and it focuses on the shape, colour and texture of just a handful of essential elements.
"""
industrial = """
Industrial interiors are defined by the architectural elements within a space.
Other styles hide the piping and ductwork, but industrial embraces those elements, making them a focal point. Industrial interior design is raw, almost unfinished, providing a casual atmosphere that's relaxing to live in. 
By keeping the space practical and uncluttered, this style is welcoming and laidback.
At its core, the industrial style relies on incorporating building materials into the room.
"""
scandinavian = """
Scandinavian interior design is a minimalistic style using a blend of textures and soft hues to make sleek, modern décor feel warm and inviting. 
It emphasizes clean lines, utility, and simple furnishings that are functional, beautiful, and cozy.
"""


#Initialize Flask and set the template folder to "template"
app = Flask(__name__, template_folder = 'templates')

# Open our model
model = pickle.load(open('model_sgd.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/", methods=['POST','GET'])


def predict():
    if request.method == "POST":
        style_2 = request.form.values()
        pred = model.predict([str(style_2)])
        output = pred[0]
        if output == 'modern interior':
            return render_template("index.html", prediction_text = f'Your home style is {output} and below is small desricption about it:', prediction_text_2 = f'{modern}')
        elif output == 'industrial interior':
            return render_template("index.html", prediction_text = f'Your home style is {output} and below is small desricption about it:', prediction_text_2 = f'{industrial}')
        elif output == 'minimalist interior':
            return render_template("index.html", prediction_text = f'Your home style is {output} and below is small desricption about it:', prediction_text_2 = f'{minimal}')
        elif output == 'contemporary interior':
            return render_template("index.html", prediction_text = f'Your home style is {output} and below is small desricption about it:', prediction_text_2 = f'{contemporary}')
        elif output == 'rustic interior':
            return render_template("index.html", prediction_text = f'Your home style is {output} and below is small desricption about it:', prediction_text_2 = f'{rustic}')
        elif output == 'scandinavian interior':
            return render_template("index.html", prediction_text = f'Your home style is {output} and below is small desricption about it:', prediction_text_2 = f'{scandinavian}')
    return render_template("index.html", prediction_text = f'Something went wrong, please refresh and try again')

if __name__ == "__main__":
    app.run(debug=True)