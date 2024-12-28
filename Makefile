PYTEST = poetry run pytest
ALLURE = allure
RESULT_DIR = allure-results
REPORT_DIR = allure-report

.PHONY: test
test:
	@echo "Запуск тестов с генерацией отчета Allure..."
	@$(PYTEST) -v -s --alluredir=$(RESULT_DIR)
	@echo "Генерация HTML-отчета Allure..."
	@$(ALLURE) generate $(RESULT_DIR) -o $(REPORT_DIR) --clean
	@echo "Открытие отчета Allure..."
	@$(ALLURE) open $(REPORT_DIR)

.PHONY: clean
clean:
	@echo "Очистка результатов и отчетов Allure..."
	@rm -rf $(RESULT_DIR) $(REPORT_DIR)
