from prettytable import PrettyTable  
  
# Creating a new table   
newTable = PrettyTable(["Student Name", "Class", "Subject", "Makrs"])  
  
# Add rows  
newTable.add_row(["Camron", "X", "English", "91"])  
newTable.add_row(["Haris", "X", "Math", "63"])  
newTable.add_row(["Jenny", "X", "Science", "90"])  
newTable.add_row(["Bernald", "X", "Art", "92"])  
newTable.add_row(["Jackson", "X", "Science", "98"])  
newTable.add_row(["Samual", "X", "English", "88"])  
newTable.add_row(["Stark", "X", "English", "95"])  
  
print(newTable)  