# L690-Employee_Importance

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: list["Employee"], id: int) -> int:
        employee_dict = {}
        for employee in employees:
            employee_dict[employee.id] = employee

        def add_importance(employee):
            if not employee:
                return 0
            importances = employee_dict[employee].importance
            for worker in employee_dict[employee].subordinates:
                importances += add_importance(worker)
            return importances

        total_importance = add_importance(id)
        return total_importance


# time O(N) - go through list of employees to generate dictionary
# space O(N) - function stack space of subordinates + dictionary
