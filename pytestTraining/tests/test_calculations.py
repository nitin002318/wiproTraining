import pytest
from source.calculations import Calulations
class TestCalculations:
    calc=Calulations()

    @pytest.mark.parametrize("n1,n2,r",[
        (1,2,3),
        (2,3,5),
        (4,5,9)

    ])
    # def test_add(self,n1,n2):
    #     re=self.calc.add(3,5)
    #     assert  re==8
    #
    def test_add(self,n1,n2,r):
        res = self.calc.add(n1,n2)
        assert res == r, "Addition Error"

    def test_sub(self):
        res = self.calc.sub(10, 5)
        assert res == 5, "Subtraction Error"

    def test_mul(self):
        res = self.calc.mul(10, 5)
        assert res == 50, "Multiplication Error"

    def test_div(self):
        res = self.calc.div(10, 5)
        assert res == 2.0, "Division Error"

    @pytest.mark.skip(reason="Not important")
    def test_ne(self):
        res = self.calc.ne(2, 2)
        assert res, "test failed"
