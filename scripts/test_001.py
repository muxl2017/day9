import pytest,allure

class Test_001():
    @allure.step(title="这是第一个用例")
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_001(self):
        assert 1

    @allure.step(title="这是第二个用例")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_002(self):
        assert 0

