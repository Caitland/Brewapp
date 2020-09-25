import unittest
from unittest.mock import Mock, patch
from brewapp2 import handle_favourite_names

#def handle_favourite_names(new_name, people):
 #   while new_name in people:
  #      new_name = input(f'\'{new_name}\' already exists on our system\n\nPlease type in name:\n').title()
   # if new_name not in people:
    #    people.append(new_name)

class Test_Methods(unittest.TestCase):
    @patch('builtins.input')
   

    def test_check_name_in_list(self, name_input):
  #Arrange
        data = ['name1', 'name2', 'name3']

        name_input.return_value = 'name4'

        actual = data.append(name_input)
        
  # Act
        actual = data.append(name_input)    
        expecting = ['name1', 'name2', 'name3', 'name4']

  # Assert
        self.assertEqual(actual, expecting)


if __name__ == "__main__":
    unittest.main()