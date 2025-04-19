from flask import Flask, request, jsonify

app = Flask(__name__)

distances = {
    'C1': {'L1': 10, 'C2': 20, 'C3': 30},
    'C2': {'L1': 15, 'C1': 20, 'C3': 25},
    'C3': {'L1': 20, 'C1': 30, 'C2': 25}
}

cost_per_km = 5 

def calculate_cost(order):
    return 100 

@app.route('/calculate_cost', methods=['POST'])
def calculate_cost_endpoint():
    order = request.json
    cost = calculate_cost(order)
    return jsonify({'cost': cost})

if __name__ == '__main__':
    app.run(debug=True)

def calculate_cost(order):
    total_cost = 0
    for product, quantity in order.items():
        total_cost += distances['C1']['L1'] * cost_per_km * quantity
    return total_cost
