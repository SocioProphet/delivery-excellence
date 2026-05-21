.PHONY: validate prophet-understand-smoke computational-artifact-scoreboard-validate

validate: prophet-understand-smoke computational-artifact-scoreboard-validate
	@echo "OK: delivery-excellence validate"

prophet-understand-smoke:
	python3 tools/smoke_prophet_understand_score.py

computational-artifact-scoreboard-validate:
	python3 tools/validate_computational_artifact_scoreboard.py
