import allure
import pytest


class Test_Abc:
    @allure.step(title='第一个测试.')
    def test_abc_001(self):
        assert 1

    @pytest.mark.parametrize('a', [0, 1, 2])
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step(title='第二个测试.')
    def test_abc_002(self, a):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert a != 2


if __name__ == '__main__':
    pytest.main("-s --alluredir report test_001.py")
