.PHONY: validate prophet-understand-smoke computational-artifact-scoreboard-validate ioes-delivery-outcome-record-validate

validate: prophet-understand-smoke computational-artifact-scoreboard-validate ioes-delivery-outcome-record-validate
	@echo "OK: delivery-excellence validate"

prophet-understand-smoke:
	python3 tools/smoke_prophet_understand_score.py

computational-artifact-scoreboard-validate:
	python3 tools/validate_computational_artifact_scoreboard.py

ioes-delivery-outcome-record-validate:
	python3 tools/validate_ioes_delivery_outcome_record.py
