def arithmetic_arranger(problems):

  problem_length = len(problems)

  if problem_length > 5:
    return "Error: Too many problems."
  
  for problem in problems:
    problem = problem.split()
    
    operand_one = problem[0]
    operand_two = problem[2]
    operator = problem[1]

    if operator != "+" and operator != "-":
      return "Error: Operator must be '+' or '-'."

    if len(operand_one) > 4 or len(operand_two) > 4:
      return "Error: Numbers cannot be more than four digits."

    if not operand_one.isdigit() or not operand_two.isdigit():
      return "Error: Numbers must only contain digits."
    
    print("still working on it...")

  # return arranged_problems