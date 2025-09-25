from pytest import CaptureFixture

from uv_project_template.__main__ import main


class TestMain:
    """测试 main 函数的测试类"""

    def test_main_output(self, capsys: CaptureFixture[str]) -> None:
        """测试 main 函数的输出结果"""
        # 调用 main 函数
        main()

        # 使用 capsys 捕获标准输出
        captured = capsys.readouterr()

        # 验证输出内容
        assert captured.out.strip() == "Hello from python-uv-project-template!"
