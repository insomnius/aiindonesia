# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Tentukan berapa hasil dari operasi +, -, *, /, %, // dan ** dari kedua variable di bawah!
# Lalu bandingkan hasil yang ada dengan nilai 30 dengan perbandingan >, <, ==, !=, >=, <=

iterations = [
  {
    "x": 0.25,
    "y": 20,
    "operation": "addition",
  },
  {
    "x": 0.25,
    "y": 20,
    "operation": "substraction",
  },
  {
    "x": 0.25,
    "y": 20,
    "operation": "multiplication",
  },
  {
    "x": 0.25,
    "y": 20,
    "operation": "division",
  },
  {
    "x": 0.25,
    "y": 20,
    "operation": "modulo",
  },
  {
    "x": 0.25,
    "y": 20,
    "operation": "floor_division",
  },
  {
    "x": 0.25,
    "y": 20,
    "operation": "exponentiation",
  },
]

# Hasil-hasil operasi

for itr in iterations:
  print("Operation:", itr["operation"])

  result = 0

  match itr["operation"]:
    case "addition":
      result = itr["x"] + itr["y"]
    case "substraction":
      result = itr["x"] - itr["y"]
    case "multiplication":
      result = itr["x"] * itr["y"]
    case "division":
      result = itr["x"] / itr["y"]
    case "modulo":
      result = itr["x"] % itr["y"]
    case "floor_division":
      result = itr["x"] // itr["y"]
    case "exponentiation":
      result = itr["x"] ** itr["y"]

  print("Result:", result)
  print("Comparisons with 30")
  print("Result > 30:", result > 30)
  print("Result < 30:", result < 30)
  print("Result == 30:", result == 30)
  print("Result != 30:", result != 30)
  print("Result >= 30:", result >= 30)
  print("Result <= 30:", result <= 30)
  print("Result > 30:", result > 30)
  print("----------------------------------------")