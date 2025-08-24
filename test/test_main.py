from pytest_mock import MockerFixture, MockType

from main import main


class TestMain:
    def test_main_output(self, mocker: MockerFixture) -> None:
        """测试 main 函数的输出结果"""
        mock_print: MockType = mocker.patch("builtins.print")
        main()
        mock_print.assert_called_once_with("Hello from python-uv-project-template!")
