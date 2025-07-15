# 1. Simple strings ➜ strings
book = {"title": "Dune", "author": "Frank Herbert"}

# 2. String keys ➜ int & float values
measurements = {"length_cm": 12, "weight_kg": 3.5}

# 3. Int keys ➜ string values
fingers = {1: "thumb", 2: "index", 3: "middle"}

# 4. Mixed key types ➜ bool values
status_flags = {"is_admin": True, 404: False}

# 5. Tuple key (immutable) ➜ float value
coordinates = {(43.7, -79.4): 250.0}     # (lat, lon) ➜ elevation

# 6. String key ➜ list value
student_grades = {"alice": [85, 90, 92]}

# 7. String key ➜ another dictionary (nesting)
api_response = {
    "data": {"fact": "Cats purr at 25 Hz", "length": 19},
    "success": True
}

# 8. String key ➜ None value (placeholder)
invoice = {"id": 5551, "paid_at": None}

# 9. String key ➜ function value (rare but allowed)
def greet(name): return f"Hello {name}"
callbacks = {"on_start": greet}

# 10. Boolean keys ➜ sets as values
truth_table = {True: {"yes", "1"}, False: {"no", "0"}}
