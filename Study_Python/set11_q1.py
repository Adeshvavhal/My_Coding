class C2dVec:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return F"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return F"{self.icap}i + {self.jcap}j + {self.kcap}k"


def main():
    c2d =C2dVec(1,3)
    c3d =C3dVec(1,9,7)


    print(c2d)
    print(c3d)




if __name__=="__main__":
    main()
