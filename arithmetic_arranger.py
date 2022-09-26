def arithmetic_arranger(problems):

  line_one = ""
  line_two = ""
  line_three = ""
  
  num_of_problems = len(problems)
  
  if num_of_problems > 5:
    return "Error: Too many problems."
  
  for problem in problems:
    problem_parts = problem.split()
    
    operand_one = problem_parts[0]
    operand_two = problem_parts[2]
    operator = problem_parts[1]

    operand_one_len = len(operand_one)
    operand_two_len = len(operand_two)

    if operator != "+" and operator != "-":
      return "Error: Operator must be '+' or '-'."

    if operand_one_len > 4 or operand_two_len > 4:
      return "Error: Numbers cannot be more than four digits."

    if not operand_one.isdigit() or not operand_two.isdigit():
      return "Error: Numbers must only contain digits."

    if operand_one_len > operand_two_len:
      problem_length = operand_one_len + 2
      operand_len_diff = operand_one_len - operand_two_len
      
      line_one_text = (" " * 2) + operand_one
      line_two_text = operator + " " + (" " * operand_len_diff) + operand_two
      line_three_text = ("-" * problem_length)
    else:
      problem_length = operand_two_len + 2
      operand_len_diff = operand_two_len - operand_one_len
      
      line_one_text = (" " * 2) + (" " * operand_len_diff) + operand_one
      line_two_text = operator + " " + operand_two
      line_three_text = ("-" * problem_length)
    
    if problem != problems[-1]:
      spacing = " " * 4
      line_one_text += spacing
      line_two_text += spacing
      line_three_text += spacing
    
    line_one += line_one_text
    line_two += line_two_text
    line_three += line_three_text

  problems_text = [line_one, line_two, line_three]
  
  arranged_problems = '\n'.join(problems_text)

  return arranged_problems