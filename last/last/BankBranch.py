class BankBranch:
    def __init__(self):
        self.branch = []

    def add_branch(self, branch):
        self.branch.append(branch)

    def remove_branch(self, branch):
        self.branch.remove(branch)

    def get_branch(self):
        return self.branch
    
    def __str__(self):
        return f'All branches: {self.get_branch()}'
