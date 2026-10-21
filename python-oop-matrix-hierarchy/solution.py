import copy
class Matrix:
    """
    A rectangular grid of numbers.

    Class attribute:
        instances_created = 0   (define it in the class body)

    __init__(self, rows):
        `rows` is a non-empty list of equal-length lists of
        numbers. Store an INDEPENDENT deep copy of it in the
        attribute `rows`, so later changes to the caller's
        lists never affect this matrix. Increase
        Matrix.instances_created by 1 (through the class).

    shape(self):
        Return a tuple (number_of_rows, number_of_columns).

    __repr__(self):
        Return "Matrix(" followed by the repr of the rows list
        and ")". Example: "Matrix([[1, 2], [3, 4]])"

    __eq__(self, other):
        Return NotImplemented if `other` is not a Matrix.
        Otherwise True if the rows are equal, else False.

    __len__(self):
        Return the number of rows.

    __getitem__(self, index):
        Return a NEW list that is a copy of the row at `index`
        (an int, negative allowed). Changing the returned list
        must not change the matrix.

    transpose(self):
        Return a NEW Matrix that is the transpose of this one.

    scale(self, k):
        Return a NEW Matrix in which every entry is multiplied
        by `k`. This matrix is unchanged.
    """
    instances_created = 0
    
    def __init__(self, rows):
        self.rows= copy.deepcopy(rows)
        Matrix.instances_created+=1
        

    def shape(self):
        return (len(self.rows), len(self.rows[0]))

    def __repr__(self):
        # return f'Matrix( [{", ".join(map(str,self.rows))})'
        return f"Matrix({self.rows!r})" 

    def __eq__(self, other):
        if not isinstance(other ,Matrix):
            return NotImplemented
        return self.rows==other.rows

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, index):
        return list(self.rows[index])
        

    def transpose(self):
        r,c= self.shape()
        return Matrix([[self.rows[j][i] for j in range(r)] for i in range(c)])
                        

    def scale(self, k): 
        return Matrix([[x*k for x in row] for row in self.rows])
        


class IdentityMatrix(Matrix):
    """
    An n-by-n identity matrix (1 on the diagonal, 0 elsewhere).

    __init__(self, n):
        Build the rows of the identity matrix as a list of
        lists, then call the parent's __init__ through super()
        with those rows. Do not repeat the parent's storing or
        counting logic here.

    Inherit every other method unchanged.
    """

    def __init__(self, n):
        identity=[[1 if i==j else 0 for i in range(n) ] for j in range(n)]
        super().__init__(identity)
