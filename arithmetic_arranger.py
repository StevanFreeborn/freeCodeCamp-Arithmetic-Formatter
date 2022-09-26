def arithmetic_arranger(problems, includeSolution=False):

  # define the four lines of the final arranged problem text as empty strings
  line_one = ""
  line_two = ""
  line_three = ""
  line_four = ""

  # get the number of problems passed
  num_of_problems = len(problems)

  # check if the number of problems exceeds the allowed limit
  if num_of_problems > 5:
    return "Error: Too many problems."

  # iterate over each problem passed to begin building 
  # each line of the final arranged problem text
  for problem in problems:

    # split the problem up into it's individual parts
    problem_parts = problem.split()

    # assign the problems parts to individual variables
    operand_one = problem_parts[0]
    operand_two = problem_parts[2]
    operator = problem_parts[1]

    # get the length of each operand in the problem
    operand_one_len = len(operand_one)
    operand_two_len = len(operand_two)

    # check if the problems operator is supported
    if operator != "+" and operator != "-":
      return "Error: Operator must be '+' or '-'."

    # check if the problems operands exceed the supported size
    if operand_one_len > 4 or operand_two_len > 4:
      return "Error: Numbers cannot be more than four digits."

    # check if the problems operands are valid numbers
    if not operand_one.isdigit() or not operand_two.isdigit():
      return "Error: Numbers must only contain digits."

    # cast the operands to integers to calculate the problems solution
    operand_one_as_int = int(operand_one)
    operand_two_as_int = int(operand_two)

    # calculate the problems solution based on problems operator
    if operator == "+":
      solution = operand_one_as_int + operand_two_as_int
    else:
      solution = operand_one_as_int - operand_two_as_int

    # cast the solution to a string so it can be manipulated as text
    # when working to put it in the final arranged problem text
    solution = str(solution)

    # get the length of the solution
    solution_len = len(solution)

    # check which operand is the longest and build up the strings
    # that will need to be appended the lines of the final arranged problems text
    if operand_one_len > operand_two_len:
      problem_length = operand_one_len + 2
      operand_len_diff = operand_one_len - operand_two_len
      solution_len_diff = problem_length - solution_len
      
      line_one_text = (" " * 2) + operand_one
      line_two_text = operator + " " + (" " * operand_len_diff) + operand_two
      line_three_text = ("-" * problem_length)
      line_four_text = (" " * solution_len_diff) + solution
    else:
      problem_length = operand_two_len + 2
      operand_len_diff = operand_two_len - operand_one_len
      solution_len_diff = problem_length - solution_len
      
      line_one_text = (" " * 2) + (" " * operand_len_diff) + operand_one
      line_two_text = operator + " " + operand_two
      line_three_text = ("-" * problem_length)
      line_four_text = (" " * solution_len_diff) + solution

    # check if the current problem is the final problem in the list
    # if it isn't add the correct about of spacing between it and the next problem
    if problem != problems[-1]:
      spacing = " " * 4
      line_one_text += spacing
      line_two_text += spacing
      line_three_text += spacing
      line_four_text += spacing

    # add this problems text to the final arranged problems text
    line_one += line_one_text
    line_two += line_two_text
    line_three += line_three_text
    line_four += line_four_text

  # check whether the solution text should be included in the final
  # arranged problem text
  if includeSolution:
    problems_text = [line_one, line_two, line_three, line_four]
  else:
    problems_text = [line_one, line_two, line_three]

  # join the lines of the final arranged problems text by new lines
  arranged_problems = '\n'.join(problems_text)

  # return the final arranged problems text
  return arranged_problems