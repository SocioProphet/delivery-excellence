.PHONY: validate prophet-understand-smoke

validate: prophet-understand-smoke
	@echo "OK: delivery-excellence validate"

prophet-understand-smoke:
	python3 tools/smoke_prophet_understand_score.py
