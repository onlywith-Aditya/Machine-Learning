from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial Data - To Do List
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome To The Sample To Do List App"

# GET: Retrieve all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# GET: Retrieve specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])  # Fixed: removed space after colon
def get_item(item_id):  # Fixed: parameter name consistency
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404  # Added status code
    return jsonify(item)  # Added return statement

#--------------------|


# POST: Create a new task- API {Using POSTMAN}
@app.route("/items", methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "Name is required"}), 400  # Better error message
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json.get("description", "")  # Use get() for optional field
    }
    items.append(new_item)
    return jsonify(new_item), 201  # Added 201 Created status

# PUT: Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])  # Fixed: removed space
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item Not Found"}), 404
    if not request.json:
        return jsonify({"error": "No data provided"}), 400
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# DELETE: Delete an item
@app.route("/items/<int:item_id>", methods=["DELETE"])  # Fixed: removed space
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item Deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)