class Branch:
    def __init__(self, name):
        self.name = name
        self.branches = []
        
    def add_branch(self, branch):
        self.branches.append(branch)
        
    def get_depth(self):
        if not self.branches:
            return 1
        else:
            return 1 + max(branch.get_depth() for branch in self.branches)

# create the root branch
root = Branch("A")

# create the child branches and add them to the root
branch_b = Branch("B")
branch_c = Branch("C")
root.add_branch(branch_b)
root.add_branch(branch_c)

# create the grandchild branches and add them to the child branches
branch_d = Branch("D")
branch_e = Branch("E")
branch_f = Branch("F")
branch_b.add_branch(branch_d)
branch_c.add_branch(branch_e)
branch_c.add_branch(branch_f)

# get the depth of the structure
depth = root.get_depth()
print(f"The depth of the structure is {depth}")
