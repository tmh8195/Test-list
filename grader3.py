import sys
import re
import json

def test_101():
    response = {}
    response['tasks'] = [{'1':True},{'2':True},{'3':False}]
    response['feedback'] = 'Incorrect: This is what you should do'
    print(json.dumps(response))
	# try:
	#     hours_array, "Please assign a value to the variable hours_array."
	#     assert isinstance(hours_array, np.ndarray), "Use the np.array() function to make hours_array a NumPy array."
	#     assert len(hours_array) == 7, "hours_array should have the same number of elements as hours_list."
	#     assert np.max(hours_array) == 45.0 and np.min(hours_array) == 25.0, "Input hours_list into the array() function to generate hours_array."
	#     print("K44: Great job!")
	# except (AssertionError, NameError) as e:
	#     print(e.args[0])

def test_102():
	search = re.search("type\(hours_array", M12)
	if not search:
	    print("Check the type of hours_array.")
	else:
	    print("K44: Good! The type ndarray stands for n-dimensional array.")

def test_103():
	search = re.search("set\(\[\s*?type\(\s*?x\s*?\)\s+?for\s+?x\s+?in\s+?hours_list", M12)
	if not search:
	    print("Run the given code to see the data types contained in hours_list.")
	else:
	    print("K44: Very good. You can see that hours_list contains both floats and integers.")

def test_104():
	search = re.search("set\(\[\s*?type\(\s*?x\s*?\)\s+?for\s+?x\s+?in\s+?hours_array", M12)
	if not search:
	    print("Run the given code to see the data types contained in hours_array.")
	else:
	    print("K44: Very good. You can see that hours_array contains only elements of type numpy.float64.")

def test_201():
	try:
	    earnings_array
	    assert isinstance(earnings_array, np.ndarray), "Create earnings_array, a new NumPy array."
	    assert max(earnings_array) == 911.25, "earnings_array must be the product of pay_array and hours_array."
	    print("K44: Very good!")
	except (AssertionError, NameError) as e:
	    print(e.args[0])

def test_202():
	try:
	    pay_array
	    assert not max(pay_array) == 33.75, "Use addition to increase each hourly wage by $1.50."
	    assert max(pay_array) == 24.0, "It doesn't look like you calculated the raise correctly."
	    print("K44: Great job! You should notice that each element of the array has increased by 1.5.")
	except (AssertionError, NameError) as e:
	    print(e.args[0])

def test_203():
	search = re.search("witholdings", M12)
	if search:
	    print("Built-in spelling lesson: withholdings has 2 h's!\n")
	try:
	    withholdings
	    assert isinstance(withholdings, np.ndarray), "Create the withholdings array."
	    assert (max(withholdings) == 60.682499999999997 and min(withholdings) == 37.200000000000003) or (min(withholdings) == 34.875 and max(withholdings) ==56.497500000000002), "Double check your math for withholdings."
	    print("K44: Excellent.")
	except (AssertionError, NameError) as e:
	    print(e.args[0])

def test_301():
	search1 = re.search("pay_array.shape", M12)
	search2 = re.search("hours_array.shape", M12)
	if not (search1 or search2):
	    print("Use the .shape attribute to check the dimensions of pay_array and hours_array.")
	if search1 or search2:
	    print("K44: Great! You can see that each array contains seven elements, which will correspond to seven rows in a 2d array.")

def test_302():
	try:
	    payroll
	    assert isinstance(payroll, np.ndarray)
	    assert not payroll.shape == (7, 1), "The payroll array must have two columns, not just one."
	    assert payroll.shape == (7, 2), "It doesn't look like you created payroll correctly."
	    assert not payroll[0][0] == payroll[0][1], "Careful! Don't stack the same column twice."
	    assert not payroll[0][0] == 18. and not payroll[0][0] == 19.5, "Change the order of pay_array and hours_array in the input tuple for the column_stack() function."
	    print("K44: Excellent work!")
	except (AssertionError, NameError) as e:
	    print(e.args[0])

def test_303():
	search = re.search("payroll.shape", M12)
	if not search:
	    print("Check the shape of the payroll array.")
	else:
	    print("K44: Good. You can see that the array has 7 rows and 2 columns.")

def test_304():
	try:
	    my_array
	    assert isinstance(my_array, np.ndarray), "Create a NumPy array called my_array."
	    assert not len(my_array.shape) == 1, "Make my_array have at least two dimensions."
	    print("K44: Cool! What a lovely array.")
	except (AssertionError, NameError) as e:
	    print(e.args[0])

def test_305():
	search = re.search("my_array.shape", M12)
	if not search:
	    print("Check the shape of my_array.")
	else:
	    print("K44: That's right!")

def test_401():
	search1 = re.search("hours_array\[\s*?1\s*?\]", M12)
	if search1:
	    print("The first element of an array has index 0, not index 1.")

	search2 = re.search("pay_array\[", M12)
	if search2:
	    print("Get the first element of hours_array, not pay_array.")

	search3 = re.search("pay_roll\[", M12)
	if search3:
	    print("Get the first element of hours_array, not payroll.")

	search4 = re.search("hours_array\[\s*?0\s*?\]", M12)
	if not search4 and not search2 and not search1 and not search3:
	    print("Select the first element of hours_array.")

	if search4 and not search1 and not search2 and not search3:
	    print("K44: Great job! Indexing of 1d arrays is the same as for lists.")

def test_402():
	search1 = re.search("pay_array\[", M12)
	if search1:
	    print("Get the first row of payroll, not pay_array.")

	search2 = re.search("payroll\[\s*?1\s*?\]", M12)
	if search2:
	    print("The first row of payroll has index 0, not index 1.")

	search3 = re.search("payroll\[\s*?0\s*?\]\[", M12)
	if search3:
	    print("Access the entire first row, not an element in that row.")

	search4 = re.search("payroll\[\s*?0\s*?\]", M12)
	if not search4:
	    print("Get the first row of payroll.")

	if search4 and not search1 and not search2 and not search3:
	    print("K44: You got it!")

def test_403():
	search = re.search("payroll\[\s*?0(.+){1,5}0\s*?\]", M12)
	if not search:
	    print("Access the first element of the first row of payroll.")
	else:
	    print("K44: Very good!")

def test_404():
	search1 = re.search("payroll\[\s*?[013456]\s*?\]\[\s*?1\s*?\]", M12)
	if search1:
	    print("The row index doesn't look quite right.")
	search2 = re.search("payroll\[\s*?2\s*?\]\[\s*?0\s*?\]", M12)
	if search2:
	    print("The column index doesn't look quite right.")
	search3 = re.search("payroll\[\s*?2(.){1,5}1\s*?\]", M12)
	if not search3 and not search1 and not search2:
	    print("That's not the right element.")
	if search3:
	    print("K44: Nailed it!")

def test_405():
	search1 = re.search("payroll\[\s*?3\s*?\]", M12)
	if search1:
	    print("Select the element using a comma to separate row and column indices.")
	search2 = re.search("payroll\[\s*?3\s*?,\s*?0\s*?\]", M12)
	if not search2 and not search1:
	    print("That's not the right element.")
	if search2 and not search1:
	    print("K44: You got it!")

def test_501():
	search1 = re.search("pay_array\[", M12)
	if search1:
	    print("Select the first three elements of hours_array, not pay_array.")
	search2 = re.search("payroll\[(.){1,2}3", M12)
	if search2:
	    print("Select the first three elements of hours_array, not payroll.")
	search3 = re.search("hours_array\[\s*?0?\s*?:\s*?3\s*?\]", M12)
	if not search3:
	    print("Select the first three elements of hours_array.")
	if search3:
	    print("K44: That's right!")

def test_502():
	try:
	    first_two_employees
	    assert isinstance(first_two_employees, np.ndarray), "Please create the array first_two_employees."
	    assert first_two_employees.shape[0] == 2, "You should select only two rows."
	    assert first_two_employees.shape[1] == 2, "You should select both columns."
	    assert first_two_employees[0][0] == payroll[0][0], "This is not the correct range."
	    print("K44: Great job! You made a 2x2 array containing hours and earnings for two employees.")
	except (AssertionError, NameError) as e:
	    print(e.args[0])

def test_503():
	try:
	    third_fourth_hours
	    assert isinstance(third_fourth_hours, np.ndarray), "Please create the array third_fourth_hours."
	    assert not third_fourth_hours.shape == (2,1), "The third_fourth_hours array should only be one-dimensional."
	    assert len(third_fourth_hours) == 2, "The third_fourth_hours array should contain 2 rows."
	    assert third_fourth_hours[0] == 35.0, "The third_fourth_hours array does not contain the correct values."
	    assert third_fourth_hours.shape == (2,), "The third_fourth_hours_array does not have the correct dimensions."
	    print("K44: Great job! That was tricky!")
	except (AssertionError, NameError) as e:
	    print(e.args[0])

def test_504():
	try:
	    pay_only
	    assert isinstance(pay_only, np.ndarray), "Please create the array pay_only."
	    assert not pay_only.shape == (7,1), "The pay_only array should have only one dimension."
	    assert pay_only.shape[0] == 7, "Select all the rows from payroll."
	    assert pay_only.shape == (7,), "The pay_only array does not have the correct dimensions."
	    assert pay_only[0] == payroll[0][1], "The pay_only array does not contain the correct data."
	    print("K44: Excellent work!")
	except (AssertionError, NameError) as e:
	    print(e.args[0])

def test_601():
	search1 = re.search("hours_array\s*?>\s*?40", M12)
	if search1:
	    print("Be careful with the direction of the inequality!")
	search2 = re.search("hours_array\s*?<\s*?40", M12)
	search3 = re.search("hours_array\s*?\[\s*?hours_array", M12)
	if search3:
	    print("Don't use square brackets to subset the array just yet! Print the Boolean array first.")
	if search2 and not search3:
	    print("K44: Great job! Notice that the True and False values align with whether the values in hours_array are greater or less than 40.")

def test_602():
	search1 = re.search("payroll\[\s*?hours_", M12)
	search2 = re.search("pay_array\[\s*?hours_", M12)
	if search1 or search2:
	    print("You should be indexing hours_array.")
	try:
	    less_than_40
	    assert isinstance(less_than_40, np.ndarray), "Please create the array less_than_40."
	    assert less_than_40[0] == 38.5, "The values of less_than_40 have not been assigned correctly."
	    print("K44: Very good! Notice that the less_than_40 array contains only 3 values, and they're all less than 40!")
	except (NameError, AssertionError) as e:
	    print(e.args[0])

def test_603():
	try:
	    assert isinstance(greater_than_20, np.ndarray), "Please create the array greater_than_20."
	    assert not True in greater_than_20, "greater_than_20 should contain actual values, not Booleans."
	    assert greater_than_20.shape[0] == 2, "The array greater_than_20 should contain 2 rows."
	    assert greater_than_20.shape[1] == 2, "The array greater_than_20 should contain both columns."
	    print("K44: You got it! Check out the second column to see that the values there are both greater than 20.")
	except (NameError, AssertionError) as e:
	    print(e.args[0])

def test_604():
	try:
	    multiple_of_10
	    assert isinstance(multiple_of_10, np.ndarray), "Please create the array multiple_of_10."
	    assert not multiple_of_10.shape[0] < 2, "You haven't selected enough rows."
	    assert not multiple_of_10.shape[1] > 2, "You've selected too many rows."
	    assert multiple_of_10.shape[1] == 2, "The array multiple_of_10 should contain both columns."
	    assert multiple_of_10[0][0] == 40.0 and multiple_of_10[0][1] == 19.25, "The values in multiple_of_10 are not correct."
	    print("K44: Great work!")
	except (NameError, AssertionError) as e:
	    print(e.args[0])

def main(test_id):
	if test_id == 1.01:
        #response = {}
        #response['tasks'] = [{'1':True},{'2':True},{'3':False}]
        #response['feedback'] = 'Incorrect: This is what you should do'
        #print(hi)
		test_101()
	elif test_id == 1.02:
		test_102()
	elif test_id == 1.03:
		test_103()
	elif test_id == 1.04:
		test_104()
	elif test_id == 2.01:
		test_201()
	elif test_id == 2.02:
		test_202()
	elif test_id == 2.03:
		test_203()
	elif test_id == 3.01:
		test_301()
	elif test_id == 3.02:
		test_302()
	elif test_id == 3.03:
		test_303()
	elif test_id == 3.04:
		test_304()
	elif test_id == 3.05:
		test_305()
	elif test_id == 4.01:
		test_401()
	elif test_id == 4.02:
		test_402()
	elif test_id == 4.03:
		test_403()
	elif test_id == 4.04:
		test_404()
	elif test_id == 4.05:
		test_405()
	elif test_id == 5.01:
		test_501()
	elif test_id == 5.02:
		test_502()
	elif test_id == 5.03:
		test_503()
	elif test_id == 5.04:
		test_504()
	elif test_id == 6.01:
		test_601()
	elif test_id == 6.02:
		test_602()
	elif test_id == 6.03:
		test_603()
	elif test_id == 6.04:
		test_604()

if __name__ == "__main__":
	test_id = float(sys.argv[1])
	main(test_id)
