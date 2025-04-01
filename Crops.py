from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
print("Flask app initialized!")
my_dictionary = {
    "Alliums": ["Onions", "Garlic", "Chives", "Shallots"],
    "Brassicas": ["Broccoli", "Cauliflower", "Cabbage",
                 "Chinese_Cabbage", "Mustard_Greens",
                 "Collards"],
    "Cucurbits": ["Zucchini","Cucumbers", "Squash", "Pumpkins", "Melons"],
    "Legumes": ['Soybeans', 'Peas'],
    "Nightshades": ['Tomatoes', 'Potatoes', 'Peppers'],
    "Umbellifers": ['Carrots', 'Parsnips', 'Fennel', 'Parsley']
}
rotation_dictionary = {
    "Alliums": ["Legumes", "Brassicas", "Nightshades", "Cucurbits", "Umbellifers"],
    "Legumes": ["Brassicas", "Nightshades", "Cucurbits", "Umbellifers", "Alliums"],
    "Brassicas": ["Nightshades", "Cucurbits", "Umbellifers", "Alliums", "Legumes"],
    "Nightshades": ["Cucurbits", "Umbellifers", "Alliums", "Legumes", "Brassicas"],
    "Cucurbits": ["Umbellifers", "Alliums", "Legumes", "Brassicas", "Nightshades"],
    "Umbellifers": ["Alliums", "Legumes", "Brassicas", "Nightshades", "Cucurbits"]
}
def get_crops_for_given_family(dictionary_name, family_name):
    if family_name in dictionary_name:
        return dictionary_name[family_name]
    else:
        return None
def get_crop_family_for_given_crop(dictionary_name, selected_crop):
    for key, val_list in dictionary_name.items():
        if selected_crop in val_list:
            return key
    return None
@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/process_data', methods = ['POST'])
def crop():
    selected_crop = request.form['crop']
    print(f"Selected crop: '{selected_crop}'")
    family_name = get_crop_family_for_given_crop(my_dictionary, selected_crop)
    print(f"Family name: '{family_name}'")
    if family_name:
        rotation_families = rotation_dictionary[family_name]
        print(f"Rotation families: {rotation_families}")
        return render_template('inter.html', rotation_crop_families=rotation_families)
    else:
        return "Error: Could not find the family for the selected crop."

@app.route('/crops/<family_name>')
def get_crops_for_family(family_name):
    crops_list = get_crops_for_given_family(my_dictionary, family_name)
    return jsonify(crops_list)
@app.route('/show_summary', methods = ['POST'])
def get_show_summary():
    crop1 = request.form.get('cropDropdown_1')
    crop2 = request.form.get('cropDropdown_2')
    crop3 = request.form.get('cropDropdown_3')
    crop4 = request.form.get('cropDropdown_4')
    crop5 = request.form.get('cropDropdown_5')
    print(crop1)
    print(crop2)
    print(crop3)
    print(crop4)
    print(crop5)
    return render_template('summary.html', year1=crop1, year2=crop2, year3=crop3, year4=crop4, year5=crop5)
if __name__ == "__main__":
    app.run(debug=True)