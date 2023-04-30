test:
	pytest -n 3

test_chrome:
	pytest --browser chrome

rerun:
	pytest --reruns 2